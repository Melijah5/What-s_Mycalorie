# Generated by Django 3.2.3 on 2021-05-29 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0006_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='height',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='weight',
        ),
    ]
