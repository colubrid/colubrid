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
from pyrp.objects import function


class Module:
    def __init__(self, filepath, main=False):
        self.filename = os.path.basename(filepath)
        self.logger = logging.getLogger(self.filename)
        file_object = open(filepath, 'r')
        content = json.load(file_object)
        self.content = []
        file_object.close()

        for i in content:
            self.parse_line(i)

        if main:
            self.run()

    def parse_line(self, line):
        log.debug('Parsing line %s' % str(line), self.logger)
        word = str(line[0])
        function_type = function.search_function(word)
        if function_type:
            log.debug('Checking arguments for %s' % word, self.logger)
            args = line[1]
            kwargs = line[2]
            for i in args:
                self.check_object(i)
            for i in kwargs:
                self.check_object(kwargs[i])
            self.content.append(['call', function_type, word, args, kwargs])

    def check_object(self, expression):
        if type(expression) == unicode:
            return True
        else:
            log.error('Syntax error in %s' % expression, self.logger)

    def run(self):
        for i in self.content:
            if i[0] == 'call':
                if i[1] == 'builtin':
                    function.run_builtin(i[2], i[3], i[4])
