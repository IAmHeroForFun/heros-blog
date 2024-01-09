from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.ModelForm):  # Its to fill in from front-end
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    # Crispy form for better look on front-end with bootstraps5
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


class SearchForm(forms.Form):  # search data in the site with this
    query = forms.CharField(label='Search')
