from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from aqi.api.viewsets import AirQualityViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("airquality", AirQualityViewSet)

app_name = "api"
urlpatterns = router.urls
