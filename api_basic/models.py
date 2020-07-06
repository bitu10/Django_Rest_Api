from django.db import models
import pytz
# Create your models here.

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(max_length = 100)
    end_time = models.DateTimeField()


class User(models.Model):
    real_name= models.CharField(max_length=100)
    timezonechoices = [(i, i) for i in pytz.all_timezones]
    tz = models.CharField(max_length =200, choices=timezonechoices)
    activity_periods = models.ManyToManyField(ActivityPeriod)




    

