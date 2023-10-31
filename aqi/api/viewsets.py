import json
import re

from rest_framework import status, viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from aqi.models import AirQuality, PMMetricsSummaryHourlyView

from .serializers import AirQualitySerializer, AirQualitySummarySerializer


class AirQualityViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = AirQuality.objects.all().order_by("-created_at")
    serializer_class = AirQualitySerializer

    def create(self, request, *args, **kwargs):
        data = re.sub(r"[\n\r]", "", request.body.decode("utf-8"))
        serializer = self.serializer_class(data=json.loads(data))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Disable other methods by raising a MethodNotAllowed exception
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT")

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH")

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

    def list(self, request, *args, **kwargs):
        queryset = PMMetricsSummaryHourlyView.objects.order_by("source_id", "-bucket").distinct("source_id")
        serializer = AirQualitySummarySerializer(queryset, many=True)
        return Response(serializer.data)
