# Generated by Django 3.1.7 on 2021-04-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpapp', '0003_auto_20210411_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.IntegerField(blank=True, choices=[(0, '北海道'), (1, '東北'), (2, '関東'), (3, '中部'), (4, '近畿'), (5, '中国'), (6, '四国'), (7, '九州'), (8, '沖縄')], null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='route',
            field=models.IntegerField(blank=True, choices=[(0, 'スクール'), (1, 'wantedly'), (2, 'GREEN'), (3, 'リクナビ'), (4, 'マイナビ転職'), (5, 'doda'), (6, '直応募'), (7, 'その他')], null=True),
        ),
    ]