from django.db import models
from django_currentuser.db.models import CurrentUserField


class CreationModel(models.Model):
    """An abstract base class model that provides self-updating ``created`` and ``modified`` fields with UUID as
    primary_key field.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = CurrentUserField(related_name='created_%(class)s')

    class Meta:
        abstract = True
