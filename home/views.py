from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader


# Will be updated to class based views so no comment for specifics details yet.
def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')

def newsletter(request):
    return render(request, 'home/newsletter.html')
