# Generated by Django 3.2.3 on 2021-05-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0004_auto_20210528_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=123456789, max_length=255),
        ),
    ]
