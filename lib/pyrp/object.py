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

from pyrp.core import log


class PyRPObject:
    __pyrpname__ = 'object'
    __converttype__ = None

    def __init__(self, parent):
        self.logger_name = '%s:%s' % (parent.logger_name, self.__pyrpname__)\
                            if parent is not None else self.__pyrpname__
        self.logger = log.get_logger(self.logger_name)
        self.objects = {}

    def build_objects(self):
        from pyrp import builtin # Builtin types are pyrp objects
        for i in builtin.objects:
            self.objects[i] = builtin.objects[i]

    def create_object(self, expression):
        try:
            if type(expression) == list:  # This object needs to be built.
                args = map(self.create_object, expression[1])
                kwargs = self.create_kwargs(expression[2])
                return self.objects[expression[0]](self, *args, **kwargs)
            else:  # This object is already built
                return expression
        except:
            log.raise_traceback('Unknown error when executing expression %s\n\
{tracemsg}' % expression, self.logger)

    def create_kwargs(self, kwargs):
        kwdict = {}
        for key in kwargs:
            kwdict[key] = self.create_object(kwargs[key])
        return kwdict
