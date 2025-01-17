from __future__ import absolute_import, unicode_literals

from builtins import dict

from ._baseline import baseline_command
from ._code import code_command
from ._codes import codes_command
from ._lint import lint_command
from ._missed import missed_command
from ._plugins import plugins_command

__all__ = [
    'COMMANDS',

    'baseline_command',
    'code_command',
    'codes_command',
    'lint_command',
    'missed_command',
    'plugins_command',
]

COMMANDS = dict(
    baseline=baseline_command,
    code=code_command,
    codes=codes_command,
    lint=lint_command,
    missed=missed_command,
    plugins=plugins_command,
)
