from django import forms
from django.contrib.auth.models import User

from .models import Company,Task, Board

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ("company_name","location", "capital","total_employee","establishd","description","phase")

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("task_title","task_memo","duedate")

class BoardModelForm(forms.ModelForm):

    class Meta:
        model = BoardModel
        fields = ("board_title","board_content")
