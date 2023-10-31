from django.db import models
from django.utils.timezone import now

from source.models import Source


class AirQuality(models.Model):
    pm2_5_value = models.FloatField()
    pm10_value = models.FloatField()
    source_id = models.UUIDField()
    created_at = models.DateTimeField(default=now, primary_key=True)

    class Meta:
        ordering = ["created_at"]


class PMMetricsSummaryHourlyView(models.Model):
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING)
    bucket = models.DateTimeField(primary_key=True)
    pm2_5_value_avg = models.FloatField()
    pm2_5_value_max = models.FloatField()
    pm2_5_value_min = models.FloatField()
    pm10_value_avg = models.FloatField()
    pm10_value_max = models.FloatField()
    pm10_value_min = models.FloatField()

    class Meta:
        managed = False
        db_table = "pm_metrics_summary_hourly"
        ordering = ["-bucket"]
