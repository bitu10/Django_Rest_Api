# Generated by Django 2.2.6 on 2020-07-05 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activity_periods',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api_basic.User'),
        ),
    ]
