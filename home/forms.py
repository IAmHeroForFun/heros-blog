from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields = ['name', 'email', 'subject', 'message']
        
    def __init__(self, *args, **kwargs): # Crispy form for better look on front-end with bootstraps5
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        