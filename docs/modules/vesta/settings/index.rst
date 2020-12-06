Settings
========

Base settings
-------------

The base settings of the project can be found in ``vesta/settings/base.py``.

Local settings
--------------

If you want to overwrite the settings, you need to create a `local.py` file where you will 
write the settings that will be overwriten. The path will be: ``vesta/settings/local.py``.

App settings
------------

Comming soon

Third party settings
--------------------

Third-party settings can be found in ``vesta/settings/third_party`` folder. Each third party 
application will have its own file with its settings. These settings will be automatically 
imported using the `django-split-settings library <https://github.com/sobolevn/django-split-settings>`_.
