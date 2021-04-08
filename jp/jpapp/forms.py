from django import forms
from django.contrib.auth.models import User

from .models import Company,Interview, Task, Board, Comment

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CompanyForm(forms.ModelForm):
    route = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        choices=(
            (0, "スクール"),(1, "wantedly"),(2, "GREEN"),(3, "リクナビ"),
            (4, "マイナビ転職"),(5, "doda"),(6, "その他"),
        ),
    )
    business_form = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        choices=(
            (0, "自社開発"),(1, "受託開発"),(2, "SES"),
        ),
    )

    location = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        choices=(
            (0, "北海道"),(1, "東北"),(2, "関東"),(3, "中部"),
            (4, "近畿"),(5, "中国"),(6, "四国"),(7, "九州"),(8, "沖縄"),
        ),
    )

    class Meta:
        model = Company
        fields = ("company_name", "url","route","business_form","location","description","phase","application_date")

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