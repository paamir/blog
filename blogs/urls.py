from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, blog_delete_view

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('edit/<int:pk>', BlogEditView.as_view(), name='edit_blog'),
    path('delete/<int:pk>', blog_delete_view, name='delete_blog')
]