import uuid

from django.contrib.auth.models import Group
from django.db import models

Group.add_to_class('uuid', models.UUIDField(db_index=True, editable=False, default=uuid.uuid4, unique=True))
Group.add_to_class('label', models.CharField(max_length=150))
