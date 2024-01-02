from django import forms 
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost # model from models.py
        fields = ['title', 'content', 'categories', 'tags', 'published', 'author'] # show needed fields
        
    content = forms.CharField(widget=CKEditorWidget())