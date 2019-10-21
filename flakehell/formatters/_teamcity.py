from __future__ import absolute_import, unicode_literals

from builtins import super

from flake8.formatting.base import BaseFormatter

escaped_values = {"'": "|'", '|': '||', '\n': '|n', '\r': '|r', '[': '|[', ']': '|]'}


def escape_value(value):
    """
    Escape values for teamcity
    """
    return ''.join(escaped_values.get(v, v) for v in value)


class TeamCityFormatter(BaseFormatter):
    """
    Show count of every code occurance
    """

    level = 'ERROR'

    def after_init(self):
        super().after_init()
        self._write("##teamcity[compilationStarted compiler='flake8']")

    def format(self, error):
        message = '{0}:{1}:{2}: {3} {4}'.format(
            error.filename,
            error.line_number,
            error.column_number,
            error.code,
            error.text,
        )
        return "##teamcity[message text='{0}' status='{1}']".format(
            escape_value(message),
            self.level,
        )

    def stop(self):
        self._write("##teamcity[compilationFinished compiler='flake8']")


class TeamCityFormatterWarning(TeamCityFormatter):
    level = 'WARNING'
