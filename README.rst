=============================
vatno-validator
=============================

.. image:: https://badge.fury.io/py/django-vatno-validator.png
    :target: https://badge.fury.io/py/django-vatno-validator

.. image:: https://travis-ci.org/productgang/django-vatno-validator.png?branch=master
    :target: https://travis-ci.org/productgang/django-vatno-validator

A Django validator that validates European VAT numbers

Documentation
-------------

The full documentation is at https://django-vatno-validator.readthedocs.org.

Quickstart
----------

Install vatno-validator::

    pip install django-vatno-validator

Then use it in a project::

    from django.db import models
    from vatno_validator.validators import VATNoValidator

    class MyModel(models.Model):
        vat_no = models.CharField(validators=[VATNoValidator(allowed_countries=[
            'DE',
            'AT',
            'GB',
        ])])




Features
--------

* Validates all 28 European member's VAT numbers according to http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
* It does not actually query the VIES, it only performs a format-check

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-text.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/pydanny/cookiecutter-djangopackage
