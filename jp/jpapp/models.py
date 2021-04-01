from django.contrib.auth.models import User
from django.db import models

CHOICE = ((0, '書類選考'),
          (1, 'カジュアル面談'),
          (2, '一次面接'),
          (3, '二次面接'),
          (4, '三次面接'),
          (5, '四次面接'),
          (6, '内定'),
          (7, 'お見送り'))

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.TextField()
    capital = models.IntegerField()
    total_employee = models.IntegerField()
    establishd = models.DateField(null=True)
    description = models.TextField()
    phase = models.IntegerField(
      # max_length = 50,
      choices = CHOICE,
      default='0'
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

def board_list(request):
    object_list = Board.objects.all()
    return render(request, 'jpapp/boards/list.html', {'object_list':object_list})

class Board(models.Model):
    board_title = models.CharField(max_length=100)
    board_content = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.board_title

