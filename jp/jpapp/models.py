from django.contrib.auth.models import User
from django.db import models

CHOICE = (('light', 'document_screening'),
          ('light', 'information_session'),
          ('alert', 'first_interview'),
          ('alert', 'second_interview'),
          ('alert', 'third_interview'),
          ('alert', 'fourth_interview'),
          ('danger', 'pass'),
          ('dark', 'failure'))

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.TextField()
    capital = models.IntegerField()
    total_employee = models.IntegerField()
    establishd = models.DateField()
    description = models.TextField()
    phase = models.CharField(
      max_length = 50,
      choices = CHOICE
    )

    #ForeignKey は一対多を表現するリレーションシップ型
    #CASCADE ユーザー削除時に同時にリストも削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_memo = models.TextField()
    duedate = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    