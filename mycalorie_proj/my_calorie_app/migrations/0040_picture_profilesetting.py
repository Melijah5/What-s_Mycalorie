# Generated by Django 3.2.3 on 2021-06-10 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0039_remove_food_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='profilesetting',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='my_calorie_app.profilesetting'),
        ),
    ]
