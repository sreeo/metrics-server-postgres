from rest_framework import viewsets

from aqi.models import AirQuality
from .serializers import AirQualitySerializer

class AirQualityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = AirQuality.objects.all()
    serializer_class = AirQualitySerializer
