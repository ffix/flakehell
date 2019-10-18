from __future__ import absolute_import, unicode_literals

from ast import AST
from builtins import dict, object, super
from typing import Sequence

from pylint.__pkginfo__ import version
from pylint.lint import Run
from pylint.reporters import BaseReporter

STDIN = 'stdin'


class Reporter(BaseReporter):
    def __init__(self):
        self.errors = []
        super().__init__()

    def _display(self, layout):
        pass

    def handle_message(self, msg):
        self.errors.append(dict(
            row=msg.line,
            col=msg.column,
            text='{} {}'.format(msg.msg_id, msg.msg or ''),
            code=msg.msg_id,
        ))


class PyLintChecker(object):
    name = 'pylint'
    version = version

    def __init__(self, tree, file_tokens, filename=STDIN):
        # type: (AST, Sequence[tuple], str) -> None
        self.tree = tree
        self.filename = filename
        self.file_tokens = file_tokens

    def run(self):
        reporter = Reporter()
        try:
            Run([self.filename], reporter=reporter, do_exit=False)  # noqa
        except TypeError:
            Run([self.filename], reporter=reporter, exit=False)  # noqa

        for error in reporter.errors:
            yield error['row'], error['col'], error['text'], type(self)
