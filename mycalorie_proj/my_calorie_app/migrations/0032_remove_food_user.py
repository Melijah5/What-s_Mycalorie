# Generated by Django 3.2.3 on 2021-06-09 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0031_auto_20210609_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
    ]
