from django.contrib.auth.models import User
from django.db import models

import datetime
from django.utils import timezone

CHOICE1 = ((0, '書類選考'),
          (1, 'カジュアル面談'),
          (2, '一次面接'),
          (3, '二次面接'),
          (4, '三次面接'),
          (5, '四次面接'),
          (6, '内定'),
          (7, 'お見送り'))

class Company(models.Model):
    company_name = models.CharField(max_length=200,)
    url = models.URLField(blank=True,null=True,)
    route = models.CharField(max_length=200,blank=True,null=True,)
    business_form = models.TextField(blank=True,null=True,)
    location = models.TextField(blank=True,null=True,)
    description = models.TextField(blank=True,null=True,)
    phase = models.IntegerField(
      choices = CHOICE1,
      default='0',
    )
    application_date = models.DateField(blank=True,null=True,)

    #ForeignKey は一対多を表現するリレーションシップ型
    #CASCADE ユーザー削除時に同時にリストも削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

CHOICE2 = ((0, 'カジュアル面談'),
          (1, '一次面接'),
          (2, '二次面接'),
          (3, '三次面接'))

class Interview(models.Model):
    interview_phase = models.IntegerField(
      choices = CHOICE2,
      default='0'
    )
    interview_datetime = models.DateTimeField()
    interview_description = models.TextField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.interview_phase

class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_memo = models.TextField()
    duedate = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

def board_list(request):
    object_list = Board.objects.all()
    return render(request, 'jpapp/boards/list.html', {'object_list':object_list})

class Board(models.Model):
    board_title = models.CharField(max_length=100)
    board_content = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.board_title

class Comment(models.Model):
   text = models.TextField('コメント')
   board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField('投稿日', default=timezone.now)
   def __str__(self):
       return self.text
