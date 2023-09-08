import datetime

from django.db import models
from django.urls import reverse


# Create your models here.

class Blog(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft')
    )

    title = models.CharField(max_length=50)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])
