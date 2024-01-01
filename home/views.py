from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')