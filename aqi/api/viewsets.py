import re, json

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from aqi.models import AirQuality
from .serializers import AirQualitySerializer

class AirQualityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = AirQuality.objects.all().order_by('-created_at')
    serializer_class = AirQualitySerializer

    def create(self, request, *args, **kwargs):
        data = re.sub(r'[\n\r]', '', request.body.decode('utf-8'))
        serializer = self.serializer_class(data=json.loads(data))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)