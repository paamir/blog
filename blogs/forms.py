from django.forms import ModelForm
from .models import Blog


class AddBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'text', 'title', 'status']
