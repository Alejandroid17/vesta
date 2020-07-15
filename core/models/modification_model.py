from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.middleware import get_current_user


class ModificationModel(models.Model):
    """An abstract base class model that provides self-updating ``created`` and ``modified`` fields with UUID as
    primary_key field.
    """
    modified_at = models.DateTimeField(_('Modified at'), auto_now=True, editable=False,
                                       help_text=_('Date when it was modified.'))
    modified_by = models.ForeignKey('user.User', verbose_name=_('Modified by'), null=True,
                                    related_name='modified_%(class)s', on_delete=models.CASCADE,
                                    help_text=_('User who modified it.'))

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.modified_by = get_current_user()
        super().save(force_insert, force_update, using, update_fields)
