import binascii
import os
import time
import uuid

from django.db import models
from django.utils.timezone import now


def generate_ulid():
    timestamp = int(time.time() * 1000)
    timestamp_hex = f"{timestamp:012x}"

    random_bytes = os.urandom(10)
    random_hex = binascii.hexlify(random_bytes).decode()

    ulid = timestamp_hex + random_hex

    return uuid.UUID(ulid)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_ulid, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = now()
        return super().save(*args, **kwargs)
