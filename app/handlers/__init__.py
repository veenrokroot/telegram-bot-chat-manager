from aiogram import Dispatcher

import loggers
from . import (private, group, channel)

__all__ = ['setup']


def setup(dispatcher: Dispatcher):
    for module in (private, group, channel):
        module.setup(dispatcher)

    loggers.handlers.debug('Setup handlers.')
