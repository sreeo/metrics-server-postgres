import uuid
from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from source.models import Source

from .models import AirQuality


class AirQualityViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.source = Source.objects.create(name="Test Source", location="Test Location")
        self.source2 = Source.objects.create(name="Test Source2", location="Test Location2")

        # Create a sample AirQuality record
        self.air_quality_record = AirQuality.objects.create(
            pm2_5_value=35.0,
            pm10_value=50.0,
            source_id=self.source.id,
            created_at=datetime.now(),
        )
        self.air_quality_record1 = AirQuality.objects.create(
            pm2_5_value=45.0,
            pm10_value=60.0,
            source_id=self.source.id,
            created_at=datetime.now(),
        )
        self.air_quality_record2 = AirQuality.objects.create(
            pm2_5_value=55.0,
            pm10_value=70.0,
            source_id=self.source.id,
            created_at=datetime.now(),
        )
        self.air_quality_record3 = AirQuality.objects.create(
            pm2_5_value=65.0,
            pm10_value=70.0,
            source_id=self.source.id,
            created_at=datetime(2021, 1, 1, 1, 1, 1),
        )

        # Create a sample AirQuality record
        self.air_quality_record = AirQuality.objects.create(
            pm2_5_value=10.0,
            pm10_value=20.0,
            source_id=self.source2.id,
            created_at=datetime.now(),
        )
        self.air_quality_record1 = AirQuality.objects.create(
            pm2_5_value=20.0,
            pm10_value=30.0,
            source_id=self.source2.id,
            created_at=datetime.now(),
        )
        self.air_quality_record2 = AirQuality.objects.create(
            pm2_5_value=30.0,
            pm10_value=40.0,
            source_id=self.source2.id,
            created_at=datetime.now(),
        )

    def deleteAll(self):
        AirQuality.objects.all().delete()

    def test_list_air_quality_records(self):
        response = self.client.get(reverse("api:airquality-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 7)

    def test_retrieve_air_quality_record(self):
        response = self.client.get(reverse("api:airquality-detail", args=[str(self.air_quality_record.source_id)]))

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_air_quality_record(self):
        data = {
            "pm2_5_value": 35.0,
            "pm10_value": 50.0,
            "source_id": uuid.uuid4(),
        }
        response = self.client.put(reverse("api:airquality-detail", args=[str(data["source_id"])]))

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(reverse("api:airquality-detail", args=[str(data["source_id"])]))

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_air_quality_record(self):
        self.deleteAll()
        data = {
            "pm2_5_value": 35.0,
            "pm10_value": 50.0,
            "source_id": uuid.uuid4(),
        }
        response = self.client.post("/api/airquality/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AirQuality.objects.count(), 1)
