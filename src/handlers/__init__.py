"""list of all dispatchers"""
from typing import Iterable

from telegrinder import Dispatch

from . import custom_name, hello

dps: Iterable["Dispatch"] = (hello.dp, custom_name.dp)
