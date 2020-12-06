UUID model
==========

All model must inherit from the abstract model :code:`UUIDModel`. This model provides the UUID field that will be used as unique model indentifier.

Example::

    from core.models import UUIDModel

    class MyCustomModel(UUIDModel):
        ....
        ....