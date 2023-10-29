import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from source.models import Source

from .models import AirQuality


class AirQualityViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.source = Source.objects.create(name="Test Source", location="Test Location")

        # Create a sample AirQuality record
        self.air_quality_record = AirQuality.objects.create(
            pm2_5_value=35.0,
            pm10_value=50.0,
            source_id=self.source.id,
        )

    def test_list_air_quality_records(self):
        response = self.client.get(reverse("api:airquality-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        # self.assertEqual(response.data[0]['id'], str(self.air_quality_record.id))
        self.assertEqual(any(record["source_id"] == str(self.source.id) for record in response.data["results"]), True)

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
        data = {
            "pm2_5_value": 35.0,
            "pm10_value": 50.0,
            "source_id": uuid.uuid4(),
        }
        response = self.client.post("/api/airquality/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AirQuality.objects.count(), 2)

    def test_create_air_quality_record_with_invalid_payload(self):
        data = '{"pm2_5_value": "\
43.20","pm10_value": "9.90","source_id": "01893941-73eb-ad05-a57b-f23c971bea61"}'
        response = self.client.post("/api/airquality/", data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AirQuality.objects.count(), 2)
