from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    Company_name = models.CharField(max_length=200)
    #ForeignKey は一対多を表現するリレーションシップ型
    #CASCADE ユーザー削除時に同時にリストも削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Company_name