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

import sys
import os
import argparse
import json

import colubrid
colubrid
from colubrid.parser import create_json
from colubrid.types.module import Module

argparser = argparse.ArgumentParser(prog='colubridc',
        description='Colubrid Compiler')
argparser.add_argument('source', metavar='SOURCE')
argparser.add_argument('-o', '--output', metavar='DEST',
                        help='Specify output file destination')
argparser.add_argument('-s', '--steps', choices=['json', 'tree'],
                        default='tree')
args = argparser.parse_args(sys.argv[1:])

name, ext = os.path.splitext(args.source)

if args.steps == 'json':
    sourcefile = open(args.source, 'r')
    source = sourcefile.read()
    output = source if ext == 'colubrid-json' else create_json(source)
    dest = args.output or '.'.join([name, 'colubrid-json'])
else:
    module = Module(args.source)
    dest = args.output or '.'.join([name, 'colubrid-tree'])
    output = json.dumps(module.content)

output_file = open(dest, 'w')
output_file.write(output)
output_file.close()
