import uuid

from django.db import models


class UUIDModel(models.Model):
    """An abstract base class model that makes primary key `id` as UUID instead of default auto incremented number.
    """
    id = models.UUIDField(db_index=True, primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True
