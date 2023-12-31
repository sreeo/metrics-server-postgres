# Generated by Django 4.2.2 on 2023-06-29 19:27

import core.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=core.models.generate_ulid, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "source_type",
                    models.CharField(
                        choices=[("AQI", "Air Quality Index"), ("PMI", "Particulate Matter Index")],
                        default="AQI",
                        max_length=3,
                    ),
                ),
                ("location", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
