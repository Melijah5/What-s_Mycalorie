# Generated by Django 3.2.3 on 2021-06-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0020_profilesetting_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='potassium_mg',
            field=models.FloatField(default=0),
        ),
    ]
