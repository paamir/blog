from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views import generic
from .models import Blog
from .forms import AddBlogForm
# Create your views here.


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(status='pub').order_by('-datetime_modified')

# def blogs_list_view(request):
#     blogs = Blog.objects.filter(status=Blog.STATUS_CHOICES[0][0]).order_by('-datetime_modified')
#     context = {
#         'blogs': blogs
#     }
#     return render(request, 'blogs/index.html', context)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blogs/blog_details.html'
    context_object_name = 'blog'

# def blog_details_view(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     context = {
#         'blog': blog,
#     }
#     return render(request, 'blogs/blog_details.html', context)


# def blog_create_view(request):
#     if request.method == 'POST':
#         form = AddBlogForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blogs')
            # form = AddBlogForm()
        # blog_title = request.POST.get('title')
        # blog_text = request.POST.get('text')
        # user = User.objects.all()[0]
        # Blog.objects.create(title=blog_title, text=blog_text, status='pub', author=user)
        # return render(request, 'blogs/add_blog.html')
    # else:
    #     form = AddBlogForm
    # return render(request, 'blogs/add_blog.html', context={'testform':form})


class BlogCreateView(generic.CreateView):
    form_class = AddBlogForm
    template_name = 'blogs/add_blog.html'
    context_object_name = 'form'


# def blog_edit_view(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     form = AddBlogForm(request.POST or None, instance=blog)
#     context = {
#         'form': form,
#     }
#     if form.is_valid():
#         form.save()
#         return redirect('blogs')
#     if request.method == 'POST':
        # if form.is_valid():
            # form.save()
            # return redirect('blogs')
    # else:
    #     return render(request, 'blogs/edit_blog.html', context=context)

class BlogEditView(generic.UpdateView):
    model = Blog
    form_class = AddBlogForm
    template_name = 'blogs/edit_blog.html'
    context_object_name = 'blog'


def blog_delete_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.status = Blog.STATUS_CHOICES[1][0]
    blog.save()
    return redirect('blogs')


# class BlogDeleteView(generic.DeleteView):
#     model = Blog
#
#     def get_success_url(self):
#         return reverse('')
