# -*- coding: utf-8 -*-

"""
IServ API
~~~~~~~~~~~~~~~~~~~
Eine IServ Benutzer API
:copyright: (c) 2021 CaptainSword123
:license: MIT, see LICENSE for more details.
"""

__title__ = 'iserv'
__author__ = 'CaptainSword123'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 CaptainSword123'
__version__ = '0.0.0'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from collections import namedtuple
import logging

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=0, micro=0, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
