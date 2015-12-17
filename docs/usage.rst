========
Usage
========

To use vatno-validator in a project::

    from django.db import models
    from vatno_validator.validators import VATNoValidator

    class MyModel(models.Model):
        vat_no = models.CharField(validators=[VATNoValidator(allowed_countries=[
            'DE',
            'AT',
            'GB',
        ])])


To allow all 28 countries, simply leave out the argument.
