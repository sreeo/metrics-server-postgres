from django.db import models
from core import BaseModel

from django.db import models

class AirQuality(BaseModel):
    pm2_5_value = models.FloatField()
    pm10_value = models.FloatField()
    source_id = models.UUIDField()

    class Meta:
        ordering = ['created_at']
