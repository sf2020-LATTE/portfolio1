# Generated by Django 3.1.7 on 2021-04-11 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpapp', '0002_auto_20210409_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='route',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
