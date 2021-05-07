from django import forms
from django.contrib.auth.models import User

from .models import Company, Task, Board, Comment, Tag, Schedule

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CompanyForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Company
        fields = ("company_name", "url","route","location","description","phase","application_date", "tag")

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

class BS4ScheduleForm(forms.ModelForm):
    """Bootstrapに対応するためのModelForm"""

    class Meta:
        model = Schedule
        fields = ('summary', 'description','date','start_time', 'end_time','company', 'interview_phase', )
        widgets = {
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'end_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_end_time(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time <= start_time:
            raise forms.ValidationError(
                '終了時間は、開始時間よりも後にしてください'
            )
        return end_time


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(BS4ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(user=user)


class CompanySearchForm(forms.Form):
    """企業検索フォーム。"""
    key_word = forms.CharField(
        label='検索キーワード',
        required=False,
    )

    tag_name = forms.ModelMultipleChoiceField(
        label='タグでの絞り込み',
        required=False,
        queryset=Tag.objects.order_by('tag_name'),
    )
