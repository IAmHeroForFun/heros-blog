from django.test import TestCase
from django.urls import reverse
from .models import Contact
from .forms import ContactForm


class HomeViewsAndTemplateTest(TestCase):
    def test_home_view_status_code(self): # home view test with template
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contact_view_status_code(self): # contact view test with template
        response = self.client.get(reverse('home:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_about_view_status_code(self): # about view test with template
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_blog_view_status_code(self): # blog view test with template
        response = self.client.get(reverse('home:blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/blog.html')


class HomeContextAndRedirect(TestCase):
    def test_home_context(self): # home page context test
        url = reverse('home:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Portfolio')

    def test_blog_context(self):
        url = reverse('home:blog') # blog page context test
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blog")

    def test_contact_context(self): # contact page context test
        url = reverse("home:contact")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact me')

    def test_about_context(self): # about page context test
        url = reverse("home:about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Me ")


class HomeModelTest(TestCase):
    def setUp(self): # model data 
        self.contact1 = Contact.objects.create(
            name='hero', email='hero@gmail.com', subject='test', message='this is test case.')

    def test_feedback_creation(self): 
        self.assertEqual(self.contact1.name, 'hero')
        self.assertEqual(self.contact1.email, 'hero@gmail.com')

    def test_str_method(self): # show output data only name and subject
        self.assertEqual(str(self.contact1), 'hero - test')


class HomeFormsTest(TestCase):
    def setUp(self): # form data for the Contact/feedback model
        self.form_data = {
            'name': 'Hero',
            'email': 'hero@hero.com',
            'subject': 'test',
            'message': 'This is test.'
        }
    
    def test_valid_form(self): # test if the form is valid
        form = ContactForm(data=self.form_data) # imported whole data as it is checking if all fields are valid
        self.assertTrue(form.is_valid()) # making sure all fields are there and working
    
    def test_invalid_form_missing_email(self):# provide invalid form data if email is missing
        invalid_form_data = self.form_data.copy() # imported whole data as it is checking if all fields are valid
        del invalid_form_data['email'] # deleting email to make it invalid
        
    def test_invalid_form_empty_name(self):
        invalid_form_data = self.form_data.copy() # imported whole data as it is checking if all fields are valid
        invalid_form_data['name'] = '' # if name empty 
        form = ContactForm(data=invalid_form_data) # check with provided data
        self.assertFalse(form.is_valid()) # it should be false when empty
    
    def test_invalid_form_invalid_email(self):
        invalid_form_data = self.form_data.copy() # imported whole data as it is checking if all fields are valid
        invalid_form_data['email'] = 'invalid-email' # if bad email 
        form = ContactForm(data=invalid_form_data) # check with provided data 
        self.assertFalse(form.is_valid()) # bad email is bad 
    
    def test_invalid_form_empty_message(self):
        invalid_form_data = self.form_data.copy() # imported whole data as it is checking if all fields are valid
        invalid_form_data['message'] = '' # checking if msg empty
        form = ContactForm(data=invalid_form_data) # check with provided data
        self.assertFalse(form.is_valid()) # empty msg is bad 