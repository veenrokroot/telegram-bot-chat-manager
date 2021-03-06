from aiogram import Dispatcher
from . import (info_user, mute, ban, kick)
__all__ = ['setup']


def setup(dispatcher: Dispatcher, *args, **kwargs):
    for module in (info_user, mute, ban, kick):
        module.setup(dispatcher, *args, **kwargs)
