from django import forms
from django.contrib.auth.models import User

from .models import Company,Interview, Task, Board, Comment, Tag

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CompanyForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple
    )

    business_form = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("自社開発", "自社開発"),("受託開発", "受託開発"),("SES", "SES"),
        ),
    )
    class Meta:
        model = Company
        fields = ("company_name", "url","route","business_form","location","description","phase","application_date", "tag")

class InterviewForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = ("company", "interview_phase", "interview_datetime", "interview_description")

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("task_title","task_memo","duedate")

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ("board_title","board_content")


class CommentForm(forms.ModelForm):    
   class Meta:
       model = Comment
       fields = ['text']