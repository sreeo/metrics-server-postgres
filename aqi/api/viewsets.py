from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from aqi.models import AirQuality

from .serializers import AirQualitySerializer


class AirQualityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = AirQuality.objects.all().order_by("-created_at")
    serializer_class = AirQualitySerializer

    # Disable other methods by raising a MethodNotAllowed exception
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT")

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH")

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

