from builtins import str
from past.builtins import basestring
from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.six import with_metaclass
from .constants import DEFAULT_NUMBER_BITS
from .version import Version
from .utils import convert_version_string_to_int, convert_version_int_to_string
from . import forms


class VersionField(with_metaclass(models.SubfieldBase, models.BigIntegerField)):
    """
    A Field where version numbers are input/output as strings (e.g. 3.0.1)
    but stored in the db as converted integers for fast indexing
    """
    description = "A version number (e.g. 3.0.1)"

    def __init__(self, number_bits=DEFAULT_NUMBER_BITS, *args, **kwargs):
        self.number_bits = number_bits
        super(VersionField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, Version):
            return int(value)

        if isinstance(value, basestring):
            return Version(value, self.number_bits)

        if value is None:
            return None

        return Version(convert_version_int_to_string(value, self.number_bits), self.number_bits)

    def get_prep_value(self, value):
        if isinstance(value, basestring):
            return int(Version(value, self.number_bits))

        if value is None:
            return None

        return int(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.VersionField,
            'number_bits': self.number_bits
        }
        defaults.update(kwargs)
        return super(VersionField, self).formfield(**defaults)

    @python_2_unicode_compatible
    def __str__(self, value):
        return str(value)


try:
    from south.modelsinspector import add_introspection_rules

    rules = [
        (
            (VersionField,),
            [],
            {
                "number_bits": ["number_bits", {"default": DEFAULT_NUMBER_BITS}],
            },
        )
    ]
    add_introspection_rules(rules, ["^versionfield"])
except ImportError:
    # looks like we aren't using south
    pass
