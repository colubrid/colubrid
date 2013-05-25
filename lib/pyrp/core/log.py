# Copyright (C) 2013 S. Daniel Francis <francis@sugarlabs.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import logging
from pyrp.core import macros
import os

if os.path.exists('pyrp.log'):
    os.remove('pyrp.log')
logging.basicConfig(filename='pyrp.log',
        level=logging.DEBUG if macros.status <= 1 else logging.INFO)
logger = logging.getLogger('core')

def log(debugger):
    def inner(*args, **kwargs):
        if 'stop' in kwargs:
            stop = (kwargs['stop'], True)
            del(kwargs['stop'])
        else:
            stop = (True, False)
        end = debugger(*args, **kwargs)
        if end and stop[1]:
            return
        elif stop[0]:
            exit(1)
    return inner

@log
def critical(message='Unknown error', log=logger):
    log.critical(message)
    print 'CRITICAL: %s' % message

@log
def error(message='Unknown error', log=logger):
    log.error(message)
    print 'ERROR: %s' % message
    return False

@log
def debug(message='', log=logger):
    log.debug(message)
    return
