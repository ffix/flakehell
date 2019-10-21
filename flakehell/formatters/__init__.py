from __future__ import absolute_import, unicode_literals

from builtins import dict

from ._baseline import BaseLineFormatter
from ._colored import ColoredFormatter
from ._grouped import GroupedFormatter
from ._json import JSONFormatter
from ._stat import StatFormatter
from ._teamcity import TeamCityFormatter, TeamCityFormatterWarning

FORMATTERS = dict(
    baseline=BaseLineFormatter,
    colored=ColoredFormatter,
    grouped=GroupedFormatter,
    json=JSONFormatter,
    stat=StatFormatter,
    teamcity=TeamCityFormatter,
    teamcity_warning=TeamCityFormatterWarning,
)
