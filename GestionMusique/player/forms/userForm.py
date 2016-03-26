from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(BaseForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets = {
			'password':forms.PasswordInput,
		}

class RegisterForm(BaseForm):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']
		widgets = {
			'password':forms.PasswordInput,
		}
