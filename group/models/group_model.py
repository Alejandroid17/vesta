import uuid

from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_user

Group.add_to_class('uuid', models.UUIDField('UUID', db_index=True, editable=False, default=uuid.uuid4, unique=True))
Group.add_to_class('label', models.CharField(_('Label'), max_length=150, help_text=_('Label of the group.')))
# CreationModel
Group.add_to_class('created_at', models.DateTimeField(_('Created at'), auto_now_add=True, editable=False,
                                                      help_text=_('Date when it was created.')))
Group.add_to_class('created_by', CurrentUserField(verbose_name=_('Created by'), related_name='created_%(class)s',
                                                  help_text=_('User who created it.')))
# ModificationModel
Group.add_to_class('modified_at', models.DateTimeField(_('Modified at'), auto_now=True, editable=False,
                                                       help_text=_('Date when it was modified.')))
Group.add_to_class('modified_by',
                   models.ForeignKey('user.User', verbose_name=_('Modified by'), related_name='modified_%(class)s',
                                     on_delete=models.CASCADE, help_text=_('User who modified it.'))
                   )


def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    """"Overrides Group save method."""
    self.modified_by = get_current_user()
    super(Group, self).save(force_insert, force_update, using, update_fields)


Group.add_to_class('save', save)
