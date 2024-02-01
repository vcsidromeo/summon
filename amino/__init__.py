__title__ = 'Dick.py'
__author__ = 'Bakugo'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020-2021 Slimakoi'
__version__ = '1.6.6'

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .socket import Callbacks, SocketHandler
from .lib.util import exceptions, headers, helpers, objects
from requests import get
from json import loads
