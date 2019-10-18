from __future__ import absolute_import, unicode_literals

from builtins import str
from hashlib import md5


def make_baseline(path, context, code, line):
    # type: (str, str, str, int) -> str
    digest = md5()
    digest.update(path.lstrip('./').encode())
    digest.update((context or str(line)).strip().encode())
    digest.update(code.encode())
    return digest.hexdigest()
