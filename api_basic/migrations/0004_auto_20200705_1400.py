# Generated by Django 2.2.6 on 2020-07-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_auto_20200705_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='activity_periods',
            field=models.ManyToManyField(to='api_basic.ActivityPeriod'),
        ),
    ]
