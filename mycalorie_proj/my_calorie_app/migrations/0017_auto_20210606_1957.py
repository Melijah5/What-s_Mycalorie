# Generated by Django 3.2.3 on 2021-06-07 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0016_remove_profilesetting_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='calorie',
        ),
        migrations.RemoveField(
            model_name='food',
            name='carbs',
        ),
        migrations.RemoveField(
            model_name='food',
            name='cholestrol',
        ),
        migrations.RemoveField(
            model_name='food',
            name='fiber',
        ),
        migrations.RemoveField(
            model_name='food',
            name='food_name',
        ),
        migrations.RemoveField(
            model_name='food',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='food',
            name='saturatedfat',
        ),
        migrations.RemoveField(
            model_name='food',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='food',
            name='suger',
        ),
        migrations.RemoveField(
            model_name='food',
            name='totalfat',
        ),
        migrations.RemoveField(
            model_name='food',
            name='transferfat',
        ),
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='carbohydrates_total_g',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='cholesterol_mg',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fat_saturated_g',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fat_total_g',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fiber_g',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='protein_g',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='serving_size_g',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='sodium_mg',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='sugar_g',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProfileSettings', to='my_calorie_app.user'),
        ),
    ]
