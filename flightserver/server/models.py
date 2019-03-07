from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


# Create your models here.
class Specification(models.Model):
    program = models.CharField(max_length=5, primary_key=True)
    capacity = models.CharField(max_length=50, null=True)


class Flight(models.Model):
    msn = models.CharField(max_length=10)
    fprogram = models.ForeignKey(Specification, on_delete=models.CASCADE)
    harness_length = models.CharField(max_length=50, null=True)
    gross_weight = models.CharField(max_length=50, null=True)
    atmospheric_pressure = models.CharField(max_length=50, null=True)
    room_temperature = models.CharField(max_length=50, null=True)
    airport = models.CharField(max_length=30, null=True)
    fuelcap_left = models.CharField(max_length=50, null=True)
    fuelcap_right = models.CharField(max_length=50, null=True)
    fuelquant_left = models.CharField(max_length=50, null=True)
    fuelquant_right = models.CharField(max_length=50, null=True)
    max_altitude = models.CharField(max_length=50, null=True)
    flight_no = models.CharField(max_length=20)
    date = AutoDateTimeField(default=timezone.now)
    holiday_flag = models.CharField(max_length=20, default=None, null=True)
