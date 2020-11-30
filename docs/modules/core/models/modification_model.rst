Modification model
==================

An abstract base class model that provides self-updating ``modified_at`` and ``modified_by`` fields. These fields are updated when the object has been changed.

Example::

    from core.models import ModificationModel

    class MyCustomModel(ModificationModel):
        ....
        ....