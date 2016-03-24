from django.db import models
from django.forms import ModelForm

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']