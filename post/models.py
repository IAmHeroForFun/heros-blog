from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model): # blog category like tech/life/adventure
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    details = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model): # tag the posts to different same posts
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    details = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class BlogPost(models.Model): # Posts from here 
    title = models.CharField(max_length=255)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    