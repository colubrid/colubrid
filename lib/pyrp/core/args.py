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

import os

from sys import argv
from pyrp.core import macros
from pyrp.core import log

usage = """
Usage:
    %s FILE -- Execute a PyRP file.
""" % argv[0]

helpmsg = """Interpreter options:
  -j, --json     Read source file in json format
  -t, --tree     Read source file in pyrp tree format.

PyRP Options:
  -h, --help     Show this help message and exit.
  -l, --log=PATH Set the PATH to save an output log file.
  -u, --usage    Show program's usage message and exit.
  -v, --version      Show program's version number and exit.
"""


def showhelp(name=True, usagemsg=True, options=True, code=0):
    if name:
        print macros.full_name
    if usagemsg:
        print usage
    if options:
        print helpmsg
    exit(code)

if len(argv) <= 1:
    showhelp(code=1)

isjson = False
tree = False

def set_json():
    global isjson
    isjson = True

def set_tree():
    global tree
    tree = True


booleans = [('-h', '--help', showhelp),
            ('-u', '--usage', lambda: showhelp(name=False, options=False)),
            ('-v', '--version',
                lambda: showhelp(usagemsg=False, options=False)),
            ('-j', '--json', set_json),
            ('-t', '--tree', set_tree)
            ]

strings = [('-l', '--log=', log.set_file)]

argument = argv[1]
index = 1

while argument[:1] == '-':
    found = False
    for i in booleans:
        if argument == i[0] or argument == i[1]:
            i[2]()
            found = True
            break
    if not found:
        for i in strings:
            if argument == i[0]:
                index += 1
                i[2](argv[index])
                found = True
            elif argument.startswith(i[1]):
                i[2](argument.split('=')[1])
                found = True
    if not found:
        log.error('Unknown argument %s' % argument)
        showhelp(code=1)
    index += 1
    argument = argv[index]

if not os.path.exists(argument) or not os.path.isfile(argument):
    log.error("%s: file not found" % argument, stop=True)
else:
    filepath = argument
