from django.contrib import admin
from .models import Category, Tag, BlogPost
from django.db import models
from .forms import BlogPostForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'published')
    list_filter = ('categories', 'tags', 'pub_date', 'published')
    search_fields = ('title', 'content', 'categories__name', 'tags__name')
    form = BlogPostForm