from django.core.exceptions import ValidationError
from django.core.validators import _lazy_re_compile
from django.utils.deconstruct import deconstructible
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _


@deconstructible
class VATNoValidator(object):
    message = _('Enter a valid VAT number.')
    code = 'invalid'

    # Format according to
    # http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
    regexes = {
        'AT': _lazy_re_compile('^ATU\d{8}$'),  # Austria
        'BE': _lazy_re_compile('^BE0\d{9}$'),  # Belgium
        'BG': _lazy_re_compile('^BG\d{9,10}$'),  # Bulgaria
        'CY': _lazy_re_compile('^CY\d{8}\w$'),  # Cyprus
        'CZ': _lazy_re_compile('^CZ\d{8,10}$'),  # Czech Republic
        'DE': _lazy_re_compile('^DE\d{9}$'),  # Germany
        'DK': _lazy_re_compile('^DK\d{2} \d{2} \d{2} \d{2}$'),  # Denmark
        'EE': _lazy_re_compile('^EE\d{9}$'),  # Estonia
        'EL': _lazy_re_compile('^EL\d{9}$'),  # Greece
        'ES': _lazy_re_compile('^ES[\w\d]\d{7}[\w\d]$'),  # Spain
        'FI': _lazy_re_compile('^FI\d{8}$'),  # Finland
        'FR': _lazy_re_compile('^FR[\w\d]{2} \d{9}$'),  # France
        'GB': _lazy_re_compile(
            '^GB((\d{3} \d{4} \d{2})|(\d{3} \d{4} \d{2} \d{3})|\
((GD|HA)\d{3}))$'),  # United Kingdom
        'HR': _lazy_re_compile('^HR\d{11}$'),  # Croatia
        'HU': _lazy_re_compile('^HU\d{8}$'),  # Hungary
        'IE': _lazy_re_compile(
            '^IE((\d[\d\w\+\*]\d{5}\w)|(\d{7}WI))$'),  # Ireland
        'IT': _lazy_re_compile('^IT\d{11}$'),  # Italy
        'LT': _lazy_re_compile('^LT\d{9,12}$'),  # Lithuania
        'LU': _lazy_re_compile('^LU\d{8}$'),  # Luxembourg
        'LV': _lazy_re_compile('^LV\d{11}$'),  # Latvia
        'MT': _lazy_re_compile('^MT\d{8}$'),  # Malta
        'NL': _lazy_re_compile('^NL\d{9}B\d{2}$'),  # The Netherlands
        'PL': _lazy_re_compile('^PL\d{10}$'),  # Poland
        'PT': _lazy_re_compile('^PT\d{9}$'),  # Portugal
        'RO': _lazy_re_compile('^RO\d{2,10}$'),  # Romania
        'SE': _lazy_re_compile('^SE\d{12}$'),  # Sweden
        'SI': _lazy_re_compile('^SI\d{8}$'),  # Slovenia
        'SK': _lazy_re_compile('^SK\d{10}$'),  # Slovakia
    }

    allowed_countries = regexes.keys()

    def __init__(self, message=None, code=None, allowed_countries=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if allowed_countries is not None:
            self.allowed_countries = allowed_countries

    def __call__(self, value):
        value = force_text(value)

        # Can't be valid
        if len(value) < 2:
            raise ValidationError(self.message, code=self.code)

        # Check if country index exists
        if (value[:2] not in self.regexes) or (
                value[:2] not in self.allowed_countries):
            raise ValidationError(self.message, code=self.code)

        regex = self.regexes[value[:2]]

        if not regex.match(value):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, VATNoValidator) and
            (self.message == other.message) and
            (self.code == other.code)
        )
