from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.TextField()
    capital = models.IntegerField()
    total_employee = models.IntegerField()
    establishd = models.DateField()
    description = models.TextField()

    #ForeignKey は一対多を表現するリレーションシップ型
    #CASCADE ユーザー削除時に同時にリストも削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
        return self.location
        return self.capital
        return self.total_employee
        return self.establishd
        return self.description

class Todo(model.Model):
    task = models.CharField(max_length=100)
    memo = TextField()
    duedate = model.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    