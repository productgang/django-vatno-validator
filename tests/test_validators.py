#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-vatno-validator
------------

Tests for `django-vatno-validator` validators module.
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from vatno_validator import validators


class TestVatno_validator(TestCase):

    def setUp(self):
        self.validator = validators.VATNoValidator()
        self.test_cases_valid = [
            'ATU99999999',
            'BE0999999999',
            'BG999999999',
            'BG9999999999',
            'CY99999999L',
            'CZ99999999',
            'CZ999999999',
            'CZ9999999999',
            'DE999999999',
            'DK99 99 99 99',
            'EE999999999',
            'EL999999999',
            'ESX99999999',
            'ES99999999X',
            'FI99999999',
            'FRXX 999999999',
            'FR99 999999999',
            'GB999 9999 99',
            'GB999 9999 99 999',
            'GBGD999',
            'GBHA999',
            'HR99999999999',
            'HU99999999',
            'IE9S99999L',
            'IE9999999WI',
            'IT99999999999',
            'LT999999999',
            'LT999999999999',
            'LU99999999',
            'LV99999999999',
            'MT99999999',
            'NL999999999B99',
            'PL9999999999',
            'PT999999999',
            'RO999999999',
            'SE999999999999',
            'SI99999999',
            'SK9999999999',
        ]
        self.test_cases_invalid = [
            'XY123',
            'ATU9999999',
            'BE1999999999',
            'BG99999999',
            'BG99999999',
            'CY9999D9994',
            'CZ9999999',
            'CZ9999999',
            'CZ9999d9999',
            'DE99999999',
            'DK9999 99 99',
            'EE99999999',
            'EL99999999',
            'ESXD9999999',
            'ES9F999999X',
            'FI9999999',
            'FRXX999999999',
            'FR99d999999999',
            'GB9999999 99',
            'GB99 9999 99 999',
            'GBGE999',
            'GBHD999',
            'HR9999999999',
            'HU9999999',
            'IE9S9999L',
            'IE999999WI',
            'IT9999999999',
            'LT999999d99',
            'LT9999s99999',
            'LU9999999',
            'LV999999999',
            'MT999999',
            'NL99999999D99',
            'PL999999999',
            'PT99999999',
            'RO99s99999',
            'SE99999999999',
            'SI9999999',
            'SK999999999',
        ]

    def test_valid(self):
        for test in self.test_cases_valid:
            try:
                self.validator(test)
            except ValidationError:
                self.fail("{0} is a false negative".format(test))

    def test_invalid(self):
        for test in self.test_cases_invalid:
            try:
                self.validator(test)
            except ValidationError:
                pass
            else:
                self.fail("{0} is a false positive".format(test))


    def test_allowed_countries(self):
        validator = validators.VATNoValidator(allowed_countries=['DE', 'AT'])
        try:
            validator('DE999999999')
            validator('ATU99999999')
        except ValidationError:
            self.fail('Failed in allowed_countries')

        try:
            validator('BE0999999999')
        except ValidationError:
            pass
        else:
            self.fail('Failed in allowed_countries')

