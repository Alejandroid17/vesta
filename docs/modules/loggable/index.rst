Loggable
========

This app allows you to keep a log for each object in your model.

How to use
----------

Define a manager in your model (``logs``)::

   from loggable.models import Loggable

   class MyModel(...):
       field1 = ...
       field2 = ...

       logs = Loggable()

Now you can write a log using ``log`` method::

   from loggable.constants import LoggingLevel

   my_object = MyModel.objects.first()
   my_object.log('This is a new message', LoggingLevel.INFO)

Log levels
^^^^^^^^^^

The differents logs available are emumerate in ``LoggingLevel`` class.

.. automodule:: loggable.constants
   :members:

More
----

.. toctree::
   :maxdepth: 10

   models
