from rest_framework import serializers

from ..models import AirQuality


class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQuality
        fields = ["pm2_5_value", "pm10_value", "source_id", "created_at"]
