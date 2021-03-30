from django import forms
from django.contrib.auth.models import User

from .models import Company
from .models import Todo

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ("company_name","location", "capital","total_employee","establishd","description")


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("task","memo","duedate")