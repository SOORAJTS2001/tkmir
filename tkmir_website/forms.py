from pickle import FALSE
from django import forms
from .models import PostsCreation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
username_validator = UnicodeUsernameValidator()

ROLE_CHOICES = [
    ('student', 'Student'),
    ('mentor', 'Mentor'),
    # ('mango', 'Mangoes'),
    # ('honeydew', 'Honeydews'),
]

INST_CHOICES = [
    ('tkmce', 'TKM College of Engineering'),
    ('tkmit', 'Thangal Kunju Musaliar Institute of Technology'),
    ('tkmcas', 'TKM College Of Arts & Science'),
    ('tkmim', 'TKM Institute of Management'),
    ('tkmsa', 'TKM School of Architecture'),
    ('tkmhss', 'TKM Higher Secondary School'),
    ('tkmchl', 'T.K.M Centre For Higher Learning'),
]



class PostsCreationForm(forms.ModelForm):
    class Meta:
        model = PostsCreation
        fields = ['title', 'content']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _(
            "Username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search'})
    )

    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': "form-control form-control-lg",'placeholder': 'Search'}))

    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': "form-control form-control-lg",'placeholder': 'Search'}), 
        strip=False, help_text=_("Enter the same password as before, for verification."))
    
    email = forms.EmailField(label=_('Email'), widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg",'placeholder': 'Search'}))

    first_name = forms.CharField(label=_("First Name"), max_length=20,  
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search'}))

    last_name = forms.CharField(label=_("Last Name"), max_length=20, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg",'placeholder': 'Search'}))

    role = forms.CharField(label=_('Role'), widget=forms.Select(
        choices=ROLE_CHOICES, attrs={'class': "form-select"}))

    roll_no = forms.CharField(required=False,max_length=20, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg",'placeholder': 'Search'}))

    mobile = forms.CharField(required=False, label=_('Mobile number'), max_length=20, 
       widget=forms.TextInput(attrs={'class': "form-control form-control-lg",'placeholder': 'Search'}))

    institution = forms.CharField(label=_('Institution'), widget=forms.Select(
        choices=INST_CHOICES, attrs={'class': "form-select"}))

    department = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg",'placeholder': 'Search'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
