# Generated by Django 3.2 on 2022-01-25 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_datecompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datemade',
            new_name='datemadeandtime',
        ),
    ]
