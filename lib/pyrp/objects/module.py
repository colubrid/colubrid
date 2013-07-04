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
import logging
import json
from pyrp.core import log
from pyrp.objects import builtin


class Module:
    def __init__(self, filepath, main=False):
        self.filename = os.path.basename(filepath)
        self.logger = logging.getLogger(self.filename)

        self.objects = {}
        self.build_objects()

        file_object = open(filepath, 'r')
        content = json.load(file_object)
        self.content = []
        file_object.close()

        for i in content:
            self.parse_line(i)

        if main:
            self.run()

    def build_objects(self):
        for i in builtin.objects:
            self.objects[i] = builtin.objects[i]

    def parse_line(self, line):
        log.debug('Parsing line %s' % str(line), self.logger)
        line_type = type(line)

        if line_type == dict:
            self.content.append(self.check_object(['set', [], line]))
        else:
            self.content.append(self.check_object(line))

    def check_object(self, expression):
        expression_type = type(expression)
        if expression_type == list:
            length = len(expression)
            if length == 1:
                return ['get', [expression[0]], {}]
            elif length > 1:
                args = map(self.check_object, expression[1])
                kwargs = self.check_kwargs(expression[2])
                return [expression[0], args, kwargs]
        elif type(expression) == unicode:
            return ['str', [expression], {}]
        else:
            log.error('Syntax error in %s' % expression, self.logger, stop=True)

    def check_kwargs(self, kwargs):
        kwdict = {}
        for key in kwargs:
            kwdict[key] = self.check_object(kwargs[key])
        return kwdict

    def create_object(self, expression):
        if type(expression) == list:  # This object needs to be built.
            args = map(self.create_object, expression[1])
            kwargs = self.create_kwargs(expression[2])
            return self.objects[expression[0]](self, *args, **kwargs)
        else:  # This object is already built
            return expression

    def create_kwargs(self, kwargs):
        kwdict = {}
        for key in kwargs:
            kwdict[key] = self.create_object(kwargs[key])
        return kwdict

    def run(self):
        log.debug('Running', self.logger)
        for i in self.content:
            self.create_object(i)
