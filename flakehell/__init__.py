"""Flake8 wrapper to make it nice and configurable
"""
from __future__ import absolute_import, unicode_literals

from ._cli import entrypoint, flake8_entrypoint


__version__ = '0.3.0'
__all__ = ['entrypoint', 'flake8_entrypoint']
