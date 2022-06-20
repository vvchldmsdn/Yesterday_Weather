from django.db import models

# Create your models here.
class Weather(models.Model):
    temp = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    cloud = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    