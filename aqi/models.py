from django.db import models
from django.utils.timezone import now


class AirQuality(models.Model):
    pm2_5_value = models.FloatField()
    pm10_value = models.FloatField()
    source_id = models.UUIDField()
    created_at = models.DateTimeField(default=now, primary_key=True)

    class Meta:
        ordering = ["created_at"]
