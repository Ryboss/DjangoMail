from django.db import models
from django import forms
# Create your models here.
class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=11)
    message = forms.CharField(max_length=1000)
    email = forms.EmailField()