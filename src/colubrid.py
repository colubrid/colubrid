#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

# @CLENV@

import argparse
from colubrid.core import macros
import colubrid
#from pyrp.core import args

parser = argparse.ArgumentParser(description=macros.name, prefix_chars='+',
                                 add_help=False)
interp_grp = parser.add_argument_group('Interpreter options')
group = interp_grp.add_mutually_exclusive_group()
interp_grp.add_argument('file', metavar='FILE', help='File to be interpreted')
group.add_argument('+j', '++json', action='store_true',
                   help='Read source file in json format')
group.add_argument('+t', '++tree', action='store_true',
                   help='Read source file in colubrid tree format')
general_opts = parser.add_argument_group('General options')
general_opts.add_argument('+h', '++help', action='help')
general_opts.add_argument('+v', '++version', action='version',
                    version='%s %s' % (macros.name, macros.version))
args = parser.parse_args(sys.argv[1:])

colubrid.main(args.file, args.json, args.tree)
