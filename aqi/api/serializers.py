from rest_framework import serializers

from ..models import AirQuality


class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQuality
        fields = ["pm2_5_value", "pm10_value", "source_id", "created_at"]


class AirQualitySummarySerializer(serializers.Serializer):
    source_id = serializers.UUIDField()
    bucket = serializers.DateTimeField()
    pm2_5_value_avg = serializers.FloatField()
    pm2_5_value_max = serializers.FloatField()
    pm2_5_value_min = serializers.FloatField()
    pm10_value_avg = serializers.FloatField()
    pm10_value_max = serializers.FloatField()
    pm10_value_min = serializers.FloatField()
