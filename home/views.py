from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from django.views.generic.edit import FormView
from django.contrib import messages
from .models import Contact
from post.models import BlogPost
from .forms import ContactForm, SearchForm

# Will be updated to class based views so no comment for specifics details yet.


def home(request):
    return render(request, 'index.html')


class Blog(generic.ListView):
    model = BlogPost
    template_name = 'home/blog.html'
    context_object_name = 'blogpost'
    ordering = '-pub_date'


class ContactView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home:contact')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thank you for using me!!!")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_message'] = getattr(self, 'success_message', None)
        return context


def about(request):
    return render(request, 'home/about.html')


def newsletter(request):
    return render(request, 'home/newsletter.html')


def search_view(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        # search logic
        results = BlogPost.objects.filter(title__icontains=query)
    return JsonResponse({'results': [{'title': result.title} for result in results]})
