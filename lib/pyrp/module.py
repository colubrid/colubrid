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
import json
from pyrp.core import log
from pyrp import builtin
from pyrp.types.code import Code
from pyrp.types.object import INDEP
from pyrp.types.object import PyRPObject


class Module(PyRPObject):
    __relation__ = INDEP

    def __init__(self, filepath, main=False):
        self.__pyrpname__ = os.path.basename(filepath)
        PyRPObject.__init__(self, None)

        file_object = open(filepath, 'r')
        script = file_object.read()
        file_object.close()
        script = script.replace('\'', '"')
        script = script.replace('(', '[')
        script = script.replace(')', ']')
        content = json.loads(script)
        self.content = []

        for i in content:
            checked = self.check_object(i, line=True)
            if checked:
                self.content.append(checked)

        if main:
            self.run()

    def check_object(self, expression, line=False):
        expression_type = type(expression)
        try:
            if expression_type == list:
                length = len(expression)
                if length == 1:
                    return ['get', [expression[0]], {}]
                elif length > 1:
                    name = expression[0]
                    line = name == ''
                    if type(name) != str:
                        name = self.check_object(name)
                    args = map(lambda arg: self.check_object(arg, line=line),
                               expression[1])
                    kwargs = self.check_kwargs(expression[2]) if length == 3 \
                                    else {}
                    return [name, args, kwargs]
            elif line:
                if expression_type == dict:
                    kwargs = self.check_kwargs(expression)
                    return ['set', [], kwargs]
                elif expression_type == str:
                    return
            elif expression_type in builtin.types:
                return [builtin.types[expression_type], [expression], {}]
            else:
                log.error('Syntax error in %s' % expression,
                            self.logger, stop=True)
        except:
            log.raise_traceback('Unknown error when parsing object type %s of %s.\n{tracemsg}' %
                         (str(expression), expression_type.__name__), log=self.logger)

    def check_kwargs(self, kwargs):
        kwdict = {}
        for key in kwargs:
            kwdict[key] = self.check_object(kwargs[key])
        return kwdict

    def run(self):
        log.debug('Running', self.logger)
        Code(self, *self.content)(self)
