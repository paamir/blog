from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Blog


# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="amir")
        cls.blog1 = Blog.objects.create(
            title='test1',
            text='test text',
            author=cls.user,
            status=Blog.STATUS_CHOICES[0][0]
        )
        cls.blog2 = Blog.objects.create(
            title='test2',
            text='test text text',
            author=cls.user,
            status=Blog.STATUS_CHOICES[1][0]
        )

    # def setUp(self):
    #     self.user = User.objects.create(username="amir")
    #     self.blog1 = Blog.objects.create(
    #         title='test1',
    #         text='test text',
    #         author=self.user,
    #         status=Blog.STATUS_CHOICES[0][0]
    #     )
    #     self.blog2 = Blog.objects.create(
    #         title='test2',
    #         text='test text text',
    #         author=self.user,
    #         status=Blog.STATUS_CHOICES[1][0]
    #     )

    def test_check_blog_list_by_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_check_blog_list_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_check_page_contains_blogs(self):
        response = self.client.get(reverse('blogs'))
        self.assertContains(response, self.blog1.title)

    def test_not_show_draft_blogs(self):
        response = self.client.get(reverse('blogs'))
        self.assertNotContains(response, self.blog2.title)

    def test_blog_detail_page_url_by_name(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog1.id]))
        self.assertEqual(response.status_code, 200)

    def test_check_details_in_blog_details_page(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog1.id]))
        self.assertContains(response, self.blog1.title)
        self.assertContains(response, self.blog1.text)

    def test_404_page_when_blog_does_not_exist(self):
        response = self.client.get(reverse('blog_detail', args=[99999999]))
        self.assertEqual(response.status_code, 404)

    def test_blog_model_str(self):
        self.assertEqual(str(self.blog1), self.blog1.title)

    def test_blog_create_view(self):
        response = self.client.post(reverse('create_blog'), {
            'author': self.user.id,
            'status': 'pub',
            'title': 'test title 22',
            'text': 'test text 22',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.last().title, 'test title 22')
        self.assertEqual(Blog.objects.last().text, 'test text 22')

    def test_blog_update_view(self):
        response = self.client.post(reverse('edit_blog', args=[self.blog1.id]), {
            'status': 'pub',
            'title': 'test title 22 updated',
            'text': 'test text 22 updated',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.get(pk=self.blog1.id).title, 'test title 22 updated')

    def test_blog_delete_view(self):
        response = self.client.post(reverse('delete_blog', args=[self.blog1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.get(pk=self.blog1.id).status, 'drf')
