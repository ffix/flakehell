from __future__ import absolute_import, unicode_literals

import re
from builtins import dict

from termcolor import colored


COLORS = dict(
    W='yellow',
    E='red',
    F='red',
    WPS='magenta',
)
REX_CODE = re.compile(r'([A-Z]+)([0-9]+)')
REX_TEXT = re.compile('[A-Z]+')
REX_NUMBER = re.compile('( [0-9]+)')
REX_PLACEHOLDER = re.compile(r'(\{[a-z0-9]+\}|\%[a-z])')
REX_QUOTES = re.compile(
    r"""
        (   # quotted text
            [\"\'\`]
            [\w\_\-\.\%\+\*]
            [\w\_\-\.\%\+\*\s\:]*
            [\"\'\`]
        )
        | (__[a-z]+__)                      # magic method
        | ([a-z\_]+\.py)                    # file name
        | (\:\s)([\w0-9]+$)                 # word after :
        | ([A-Z][a-z\.]+(?:[A-Z][a-z\.]+)+) # CamelCase
        | ([a-z_]+\(\))                     # function
    """,
    re.X,
)


def color_code(code):
    # type: (str) -> str
    match = REX_TEXT.match(code)
    color = 'blue'
    if match:
        color = COLORS.get(match.group(), color)
    return REX_CODE.sub(colored(r'\1', color) + colored(r'\2', 'cyan'), code)


def colorize_quotes(m):
    # https://bugs.python.org/issue1519638
    return '{0}{1}'.format(
        m.group(4) or '',
        colored(
            '{}{}{}{}{}{}'.format(
                m.group(1) or '',
                m.group(2) or '',
                m.group(3) or '',
                m.group(5) or '',
                m.group(6) or '',
                m.group(7) or '',
            ),
            'yellow',
        ),
    )

def color_description(text):
    # type: (str) -> str
    text = REX_NUMBER.sub(colored(lambda m: m.group(1), 'green'), text)
    text = REX_QUOTES.sub(colorize_quotes, text)
    text = REX_PLACEHOLDER.sub(colored(lambda m: m.group(1), 'green'), text)
    return text
