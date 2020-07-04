import uuid

from django.db import models


class UUIDModel(models.Model):
    """An abstract base class model that makes primary key `id` as UUID instead of default auto incremented number.
    """
    uuid = models.UUIDField('UUID', db_index=True, editable=False, default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True
