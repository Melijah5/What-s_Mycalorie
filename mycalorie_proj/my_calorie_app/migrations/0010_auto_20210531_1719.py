# Generated by Django 3.2.3 on 2021-06-01 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0009_rename_activity_profilesetting_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilesetting',
            name='height',
            field=models.FloatField(verbose_name=10),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='weight',
            field=models.FloatField(verbose_name=10),
        ),
    ]
