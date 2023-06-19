from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
