from __future__ import absolute_import, unicode_literals

from collections import namedtuple

from flake8.style_guide import Violation

# the same as in flake8, but with some additional fields
_Violation = namedtuple(
    'Violation',
    [
        'code',
        'filename',
        'line_number',
        'column_number',
        'text',
        'physical_line',

        # added fields
        'plugin',
    ],
)


class FlakeHellViolation(_Violation):
    """Patched flake8.style_guide.Violation

    We can't just inherit because Violation is a namedtuple,
    and we can't add new fields.
    """

    def is_inline_ignored(self, disable_noqa):
        values = self._asdict()
        del(values['plugin'])
        return Violation(**values).is_inline_ignored(disable_noqa)

    def is_in(self, diff):
        values = self._asdict()
        del(values['plugin'])
        return Violation(**values).is_in(diff)
