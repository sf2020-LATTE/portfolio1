# Generated by Django 3.1.7 on 2021-04-29 12:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jpapp', '0006_auto_20210415_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='business_form',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_phase', models.IntegerField(choices=[(0, 'カジュアル面談'), (1, '一次面接'), (2, '二次面接'), (3, '三次面接')], default='0')),
                ('summary', models.CharField(max_length=50, verbose_name='概要')),
                ('description', models.TextField(blank=True, verbose_name='詳細な説明')),
                ('start_time', models.TimeField(default=datetime.time(7, 0), verbose_name='開始時間')),
                ('end_time', models.TimeField(default=datetime.time(7, 0), verbose_name='終了時間')),
                ('date', models.DateField(verbose_name='日付')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpapp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]