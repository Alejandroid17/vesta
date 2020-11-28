import inspect

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class SignalManager(models.Manager):

    def contribute_to_class(self, model, name):
        super(SignalManager, self).contribute_to_class(model, name)
        self._add_signal_field_dispacher_methods(model)

        models.signals.post_save.connect(receiver=model._post_save_field_signal, sender=model,
                                         dispatch_uid='post_save_{}_field_signal'.format(model.__name__.lower()))

    # def _add_signal_field_dispacher_methods(self, model):

    #     def _post_save_field_signal(sender, update_fields, created, instance, **kwargs):
    #         print('_post_save_field_signal')
    #         for field in update_fields:
    #             print('field', field)
    #             post_save_method = getattr(
    #                 instance, '_on_post_save_{}'.format(field), None)
    #             if post_save_method is not None and inspect.isfunction(post_save_method):
    #                 post_save_method(sender, update_fields, created, **kwargs)

    #     setattr(model, '_post_save_field_signal', _post_save_field_signal)


class SignalModel(models.Model):

    # signal = SignalManager()

    # def __init__(self, *args, **kwargs):
    # super(SignalModel, self).__init__(*args, **kwargs)
    # print('hola')

   # @classmethod
   # def __init_subclass__(cls, **kwargs):
   #     super().__init_subclass__(**kwargs)
   #     models.signals.post_save.connect(post_save_field_signal,
   #                                      weak=False,
   #                                      sender=cls,
   #                                      dispatch_uid='post_save_{}_field_signal'.format(cls.__name__.lower()))

    class Meta:
        abstract = True


@receiver(post_save, sender=SignalModel)
def post_save_field_signal(sender, update_fields, created, instance, **kwargs):
    print('_post_save_field_signal')
    for field in update_fields:
        print('field', field)
        post_save_method = getattr(
            instance, '_on_post_save_{}'.format(field), None)
        if post_save_method is not None and inspect.isfunction(post_save_method):
            post_save_method(sender, update_fields, created, **kwargs)
