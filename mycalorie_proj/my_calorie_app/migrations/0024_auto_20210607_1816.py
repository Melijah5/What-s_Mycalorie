# Generated by Django 3.2.3 on 2021-06-08 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0023_auto_20210607_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='food',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='food',
            name='meal',
            field=models.CharField(default='Lunch', max_length=255),
        ),
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='food',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]