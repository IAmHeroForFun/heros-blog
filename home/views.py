from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader

from django.contrib import messages
from .models import Contact
from post.models import BlogPost
from .forms import ContactForm

# Will be updated to class based views so no comment for specifics details yet.
def home(request):
    return render(request, 'index.html')

class Blog(generic.ListView):
    model = BlogPost
    template_name = 'home/blog.html'
    context_object_name = 'blogpost'
    ordering = '-pub_date'


# def contact(request):
#     return render(request, 'home/contact.html')
class ContactView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home:contact')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thank you for using me!!!")
        return response

def about(request):
    return render(request, 'home/about.html')

def newsletter(request):
    return render(request, 'home/newsletter.html')
