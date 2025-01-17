from __future__ import absolute_import, unicode_literals

from builtins import object
from typing import Tuple

try:
    from typing import SimpleNamespace
except ImportError:
    class SimpleNamespace(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def __repr__(self):
            keys = sorted(self.__dict__)
            items = ('{}={!r}'.format(k, self.__dict__[k]) for k in keys)
            return '{}({})'.format(type(self).__name__, ', '.join(items))

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

CommandResult = Tuple[int, str]
