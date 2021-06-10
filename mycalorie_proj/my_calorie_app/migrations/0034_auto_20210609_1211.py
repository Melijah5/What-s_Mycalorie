# Generated by Django 3.2.3 on 2021-06-09 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_calorie_app', '0033_auto_20210609_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='my_calorie_app.profilesetting'),
        ),
        migrations.AddField(
            model_name='profilesetting',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ProfileSettings', to='my_calorie_app.user'),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='activity',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='age',
            field=models.IntegerField(default=None, verbose_name=3),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='height',
            field=models.FloatField(default=None, verbose_name=10),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='profile_pic',
            field=models.FileField(default='/static/css/image/default.png', upload_to='user_image'),
        ),
        migrations.AlterField(
            model_name='profilesetting',
            name='weight',
            field=models.FloatField(default=None, verbose_name=10),
        ),
    ]