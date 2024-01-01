from django import forms 
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories', 'tags', 'published']
        
    content = forms.CharField(widget=CKEditorWidget())