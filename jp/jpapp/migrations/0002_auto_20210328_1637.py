# Generated by Django 3.1.7 on 2021-03-28 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Company_name',
            new_name='company_name',
        ),
    ]