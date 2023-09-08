from django.contrib import admin
from .models import Blog

# Register your models here.


@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status=Blog.STATUS_CHOICES[0][0])


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'datetime_created', 'status']
    date_hierarchy = "datetime_created"
    actions = [make_published]

