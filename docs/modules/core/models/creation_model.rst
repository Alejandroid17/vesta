Creation model
==============

An abstract base class model that provides self-updating ``created_at`` and ``created_by`` fields. These fields are updated when the object is created.

Example::

    from core.models import CreationModel

    class MyCustomModel(CreationModel):
        ....
        ....