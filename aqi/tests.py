from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import AirQuality
from source.models import Source

class AirQualityViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.source = Source.objects.create(name='Test Source', location='Test Location')

        # Create a sample AirQuality record
        self.air_quality_record = AirQuality.objects.create(
            pm2_5_value=35.0,
            pm10_value=50.0,
            source_id=self.source.id,
        )

    def test_list_air_quality_records(self):
        response = self.client.get(reverse('api:airquality-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.air_quality_record.id))

    def test_retrieve_air_quality_record(self):
        response = self.client.get(reverse('api:airquality-detail', args=[str(self.air_quality_record.id)]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.air_quality_record.id))
        self.assertEqual(response.data['pm2_5_value'], self.air_quality_record.pm2_5_value)
        self.assertEqual(response.data['pm10_value'], self.air_quality_record.pm10_value)
        self.assertEqual(response.data['source_id'], str(self.air_quality_record.source_id))

    def test_create_air_quality_record(self):
        import uuid
        data = {
            'pm2_5_value': 35.0,
            'pm10_value': 50.0,
            'source_id': uuid.uuid4(),
        }
        response = self.client.post(reverse('api:airquality-list'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AirQuality.objects.count(), 2)