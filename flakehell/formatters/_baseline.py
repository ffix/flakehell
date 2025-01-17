from __future__ import absolute_import, unicode_literals

from flake8.formatting.base import BaseFormatter

from .._logic import make_baseline


class BaseLineFormatter(BaseFormatter):
    def format(self, error):
        filename = error.filename
        if filename.startswith('./'):
            filename = filename[2:]
        return make_baseline(
            path=filename,
            code=error.code,
            line=error.line_number,
            context=error.physical_line,
        )
