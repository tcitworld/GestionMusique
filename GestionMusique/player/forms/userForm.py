from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

class RegisterForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']