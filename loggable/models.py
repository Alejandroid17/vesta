from __future__ import unicode_literals

import copy
import importlib
import threading
import uuid
import warnings

import django
import six
from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import ManyToManyField, Q
from django.db.models.fields.proxy import OrderWrt
from django.forms.models import model_to_dict
from django.urls import reverse
from django.utils.text import format_lazy
from django.utils import timezone


from django.utils.translation import gettext_lazy as _
from django.utils.encoding import smart_str

from loggable.manager import HistoryDescriptor, LoggableManager
from loggable.constants import LoggingLevel


registered_models = {}


class Loggable(object):

    def __init__(self):

        self.inherit = False
        self.bases = (models.Model,)

    def get_meta_options(self, model):
        """
        Returns a dictionary of fields that will be added to
        the Meta inner class of the historical record model.
        """
        meta_fields = {}
        meta_fields['verbose_name'] = format_lazy(
            'loggable {}', smart_str(model._meta.verbose_name))
        meta_fields['indexes'] = [
            models.Index(fields=['created']),
            models.Index(
                fields=[self._get_loggable_field_name(model), 'level']),
            models.Index(
                fields=[self._get_loggable_field_name(model), 'created'])
        ]
        return meta_fields

    def get_loggable_model_name(self, model):
        return 'Loggable{}'.format(model._meta.object_name)

    def _get_loggable_field_name(self, model):
        return model.__name__.lower()

    def create_loggable_model(self, model):

        attrs = {
            '__module__': self.module,
            self._get_loggable_field_name(model): models.ForeignKey('{}.{}'.format(model._meta.app_label, model.__name__),
                                                                    related_name='%(class)s',
                                                                    on_delete=models.CASCADE,
                                                                    db_index=True,
                                                                    verbose_name=_('user')),
            'created': models.DateTimeField(_('created'),
                                            default=timezone.now,
                                            editable=False),
            'level': models.IntegerField(_('level'),
                                         choices=[(level.value, level.name) for level in LoggingLevel]),
            'message': models.CharField(_('message'), max_length=600),
            '__str__': lambda self: '{id} | {model_id} | {level} | {created}'.format(id=self.id,
                                                                                     model_id=getattr(
                                                                                         self, self._get_loggable_field_name()),
                                                                                     level=LoggingLevel(
                                                                                         self.level).name,
                                                                                     created=self.created)
        }

        attrs.update(Meta=type(str('Meta'), (), self.get_meta_options(model)))

        # Set as the default then check for overrides
        name = self.get_loggable_model_name(model)

        registered_models[model._meta.db_table] = model

        loggable_model = type(str(name), self.bases, attrs)
        return (loggable_model)

    def contribute_to_class(self, cls, name):
        self.manager_name = name
        self.module = cls.__module__
        self.cls = cls
        models.signals.class_prepared.connect(self.finalize, weak=False)
        self._add_extra_methods(cls)

    def finalize(self, sender, **kwargs):
        if self.cls is not sender:  # set in concrete
            return not issubclass(sender, self.cls)

        if hasattr(sender._meta, 'loggable_manager_attribute'):
            raise Exception('{}.{} registered multiple times'.format(
                sender._meta.app_label, sender._meta.object_name))
        loggable_model = self.create_loggable_model(sender)

        module = importlib.import_module(self.module)
        setattr(module, loggable_model.__name__, loggable_model)

        descriptor = HistoryDescriptor(loggable_model)
        setattr(sender, self.manager_name, descriptor)
        sender._meta.loggable_manager_attribute = self.manager_name

    def _add_extra_methods(self, cls):

        def log(self):
            print('Comming soon...')

        setattr(cls, 'log', log)
