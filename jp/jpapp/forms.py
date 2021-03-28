from django import forms
from django.contrib.auth.models import User

from .models import Company

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ("company_name",)