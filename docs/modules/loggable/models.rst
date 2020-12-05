Model
=====

Loggable
--------

For each model that implements ``Loggable()`` a table in the data base will be created. The
name of the table will be ``<app>_loggable<model_name>``.

The fields will be:

* **<foreign_key_field_name>**: Foreign key of the main model.
* **created**: Date and time when the log was created.
* **level**: Log level.
* **message**: Log message.