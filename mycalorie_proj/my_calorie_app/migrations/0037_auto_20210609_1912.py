# Generated by Django 3.2.3 on 2021-06-10 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0036_auto_20210609_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilesetting',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
