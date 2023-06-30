from django.db import models
from core.models import BaseModel

class SourceType(models.TextChoices):
    AQI = 'AQI', 'Air Quality Index'
    PMI = 'PMI', 'Particulate Matter Index'
    # Add more source types as needed

class Source(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=3, choices=SourceType.choices, default=SourceType.AQI)
    location = models.CharField(max_length=200)

