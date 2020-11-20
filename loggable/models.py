from __future__ import unicode_literals

import importlib

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_str
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _

from loggable.constants import LoggingLevel
from loggable.manager import LoggableDescriptor

registered_models = {}


class Loggable(object):

    def __init__(self, log_type='database', max_entries=1000):

        self.inherit = False
        self.bases = (models.Model,)
        self.foreign_key_field_name = None
        self.log_type = getattr(
            settings, 'LOGGABLE_LOG_TYPE', None) or log_type
        self.max_entries = getattr(
            settings, 'LOGGABLE_MAX_ENTRIES', None) or max_entries

    def get_meta_options(self, model):
        """Gets a dictionary with the fields that will be added to 
        the Meta inner class of the loggable model.
        """
        meta_fields = {}
        meta_fields['verbose_name'] = format_lazy(
            'loggable {}', smart_str(model._meta.verbose_name))
        meta_fields['indexes'] = [
            models.Index(fields=['created']),
            models.Index(
                fields=[self.foreign_key_field_name, 'level']),
            models.Index(
                fields=[self.foreign_key_field_name, 'created'])
        ]
        return meta_fields

    def get_loggable_model_name(self, model):
        """Gets the model name."""
        return 'Loggable{}'.format(model._meta.object_name)

    def create_loggable_model(self, model):
        """Creates the loggable model that will be related with the main model."""

        attrs = {
            '__module__': self.module,
            self.foreign_key_field_name: models.ForeignKey('{}.{}'.format(model._meta.app_label, model.__name__),
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
                                                                                         self, model.__name__.lower()),
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
        self.foreign_key_field_name = cls.__name__.lower()
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

        descriptor = LoggableDescriptor(loggable_model)
        setattr(sender, self.manager_name, descriptor)
        sender._meta.loggable_manager_attribute = self.manager_name
        models.signals.post_save.connect(
            self.rotate_log, sender=loggable_model, weak=False, dispatch_uid='post_save_{}_loggable_signal'.format(sender.__name__.lower()))

    def rotate_log(self, sender, instance, created, using=None, **kwargs):
        """If the number of entries per `foreign_key_field_name` object is exceeded, the oldest ones are deleted."""
        id_list = sender.objects.filter(**{self.foreign_key_field_name: getattr(
            instance, self.foreign_key_field_name)}).order_by('-created').values_list('id', flat=True)[self.max_entries:]
        sender.objects.filter(id__in=id_list).delete()

    def _add_extra_methods(_self, cls):
        """Add extra methods to the related model."""

        def log(self, message, level=LoggingLevel.INFO):
            """Add a log entry with the message and log level.

            Args:
                self (:class:): model that use the `Loggable` class.
                message (str): message to be saved.
                level (:enum: `~loggable.constants.LoggingLevel`): Log level.

            """
            getattr(self, _self.manager_name).create(
                user=self, level=level, message=message)

        setattr(cls, 'log', log)
