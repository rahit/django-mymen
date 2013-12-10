from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

__author__ = 'rahit'


class RahitRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RahitRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
        )
        self.helper.form_tag = False

    """
    Validate that the supplied email address is unique for the
    site.

    """
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError("Email already exists.")
        return email

    """
    Add additional field to the form and then save it

    """
    def save(self, commit=True):
        user = super(RahitRegistrationForm, self).save(commit=False)
        user.email = self.clean_email()
        user.is_active = False

        if commit:
            user.save()

        return user



class RahitLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username or email', max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email']
