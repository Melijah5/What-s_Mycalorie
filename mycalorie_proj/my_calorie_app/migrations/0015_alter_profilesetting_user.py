# Generated by Django 3.2.3 on 2021-06-05 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0014_profilesetting_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilesetting',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_calorie_app.user'),
        ),
    ]
