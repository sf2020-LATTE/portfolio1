from django import forms
from django.contrib.auth.models import User

from .models import Company,Interview, Task, Board, Comment

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CompanyForm(forms.ModelForm):
    route = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("スクール", "スクール"),("wantedly", "wantedly"),("GREEN", "GREEN"),("GREEN", "GREEN"),
            ("マイナビ転職", "マイナビ転職"),("doda", "doda"),("その他", "その他"),
        ),
    )
    business_form = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("自社開発", "自社開発"),("受託開発", "受託開発"),("SES", "SES"),
        ),
    )

    location = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("北海道", "北海道"),("東北", "東北"),("関東", "関東"),("中部", "中部"),
            ("近畿", "近畿"),("中国", "中国"),("四国", "四国"),("九州", "九州"),("沖縄", "沖縄"),
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