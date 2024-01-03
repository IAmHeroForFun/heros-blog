from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

from post.models import BlogPost


# Will be updated to class based views so no comment for specifics details yet.
def home(request):
    return render(request, 'index.html')

class Blog(generic.ListView):
    model = BlogPost
    template_name = 'home/blog.html'
    context_object_name = 'blogpost'
    ordering = '-pub_date'


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')

def newsletter(request):
    return render(request, 'home/newsletter.html')
