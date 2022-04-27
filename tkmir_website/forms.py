from django import forms
from .models import PostsCreation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class PostsCreationForm(forms.ModelForm):
	class Meta:
		model = PostsCreation
		fields = ['title', 'content']
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	roll_no = forms.CharField(max_length = 20)
	mobile = forms.CharField(max_length = 20)
	college = forms.CharField(max_length = 50)
	department = forms.CharField(max_length = 30)
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username']
