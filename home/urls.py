from django.urls import path 
from . import views
from .views import Blog, ContactView

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', Blog.as_view(), name='blog'),
    # path('contact/', views.contact, name='contact'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', views.about, name='about'),
    path('newsletter/', views.newsletter, name='newsletter'),
]