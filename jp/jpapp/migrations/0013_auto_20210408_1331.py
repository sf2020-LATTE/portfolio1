# Generated by Django 3.1.7 on 2021-04-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpapp', '0012_interview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='company',
            name='establishd',
        ),
        migrations.RemoveField(
            model_name='company',
            name='total_employee',
        ),
        migrations.AddField(
            model_name='company',
            name='business_form',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='route',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.TextField(null=True),
        ),
    ]
