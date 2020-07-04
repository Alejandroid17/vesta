import uuid

from django.contrib.auth.models import Group
from django.db import models
from django_currentuser.db.models import CurrentUserField

Group.add_to_class('uuid', models.UUIDField(db_index=True, editable=False, default=uuid.uuid4, unique=True))
Group.add_to_class('label', models.CharField(max_length=150))
Group.add_to_class('created_at', models.DateTimeField(auto_now_add=True, editable=False))
Group.add_to_class('created_by', CurrentUserField(related_name='created_%(class)s'))
Group.add_to_class('modified_at', models.DateTimeField(auto_now=True, editable=False))
Group.add_to_class('modified_by', models.ForeignKey('user.User', related_name='modified_%(class)s', on_delete=models.CASCADE))
