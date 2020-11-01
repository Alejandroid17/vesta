from django.db import models


class HistoryDescriptor(object):
    def __init__(self, model):
        self.model = model

    def __get__(self, instance, owner):
        if instance is None:
            return LoggableManager(self.model)
        return LoggableManager(self.model, instance)


class LoggableManager(models.Manager):
    def __init__(self, model, instance=None):
        super(LoggableManager, self).__init__()
        self.model = model
        self.instance = instance

    def get_super_queryset(self):
        return super(LoggableManager, self).get_queryset()

    def get_queryset(self):
        qs = self.get_super_queryset()
        if self.instance is None:
            return qs

        key_name = self.instance._meta.model_name
        return self.get_super_queryset().filter(**{key_name: self.instance.pk})
