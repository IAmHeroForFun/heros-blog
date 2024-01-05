from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .forms import ContactForm


class HomeViewsAndTemplateTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('home:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_about_view_status_code(self):
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_blog_view_status_code(self):
        response = self.client.get(reverse('home:blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/blog.html')


class HomeContextAndRedirect(TestCase):
    def test_home_context(self):
        url = reverse('home:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Portfolio')

    def test_blog_context(self):
        url = reverse('home:blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blog")

    def test_contact_context(self):
        url = reverse("home:contact")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact me')

    def test_about_context(self):
        url = reverse("home:about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Me ")


class HomeModelTest(TestCase):
    def setUp(self):
        self.contact1 = Contact.objects.create(
            name='hero', email='hero@gmail.com', subject='test', message='this is test case.')

    def test_feedback_creation(self):
        self.assertEqual(self.contact1.name, 'hero')
        self.assertEqual(self.contact1.email, 'hero@gmail.com')

    def test_str_method(self):
        self.assertEqual(str(self.contact1), 'hero - test')


class HomeFormsTest(TestCase):
    def test_form_valid_check(self):
        form_data = {
            'name': 'hero',
            'email': 'hero@gmail.com',
            'subject': 'test',
            'message': 'mes2sage',
        }
        form = ContactForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_check(self):
        form_data = {
            'name': 'hero',
        }
        form = ContactForm(form_data)
        self.assertFalse(form.is_valid())

    def test_form_submission_check(self):
        form_data = {
            'name': 'hero',
            'email': 'hero@gmail.com',
            'subject': 'test',
            'message': 'mes2sage',
        }
        form = ContactForm(form_data)
        self.assertTrue(form.is_valid())