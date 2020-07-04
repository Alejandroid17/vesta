from django.db import models


class ModificationModel(models.Model):
    """An abstract base class model that provides self-updating ``created`` and ``modified`` fields with UUID as
    primary_key field.
    """
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey('user.User', related_name='modified_%(class)s', on_delete=models.CASCADE)

    class Meta:
        abstract = True
