Locale Middleware
=================

:code:`LocalMiddleware` is used to detect the user's language and it is used to internationalize the application.

The language selected will be based on (by order):

* The language selected in the :code:`language` user field.
* The language selected in the browser.
* The language selected in :code:`LANGUAGE_CODE` setting.

.. include:: source/core.middleware.locale

How to use
----------

Add it to the MIDDLEWARE list in your Django settings::

    MIDDLEWARE = [
        ...,
        'core.middleware.locale.LocaleMiddleware'
    ]