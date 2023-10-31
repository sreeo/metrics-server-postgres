from asgiref.sync import sync_to_async
from django.shortcuts import render

from source.models import Source

from .models import PMMetricsSummaryHourlyView


@sync_to_async
def get_metrics_summary():
    return list(
        PMMetricsSummaryHourlyView.objects.order_by("source_id", "-bucket")
        .distinct("source_id")
        .select_related("source")
    )


async def air_quality_view(request):
    location_queryset = Source.objects.all()
    air_quality_data = await get_metrics_summary()
    return render(request, "air_quality.html", {"locations": location_queryset, "air_quality_data": air_quality_data})
