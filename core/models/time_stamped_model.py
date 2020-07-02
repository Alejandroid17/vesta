from django.db import models
from django_currentuser.db.models import CurrentUserField


class TimeStampedModel(models.Model):
    """An abstract base class model that provides self-updating ``created`` and ``modified`` fields with UUID as
    primary_key field.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = CurrentUserField()
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
