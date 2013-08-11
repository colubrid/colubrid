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

INDEP = 1
DEP = 0
PART = -1


class PyRPObject:
    __pyrpname__ = 'object'
    __converttype__ = None
    __relation__ = PART

    def __init__(self, parent):
        self.logger_name = '%s:%s' % (parent.logger_name, self.__pyrpname__)\
                            if parent is not None else self.__pyrpname__
        self.logger = log.get_logger(self.logger_name)
        self.objects = {}
        if parent:
            self.build_objects(parent)

    def build_objects(self, parent):
        if self.__relation__ == PART:
            self.objects = parent.objects
        elif self.__relation__ == DEP:
            for i in parent.objects:
                self.objects[i] = parent.objects[i]

    def create_object(self, expression):
        from pyrp.functions import rpget
        try:
            if type(expression) == list:  # This object needs to be built.
                name, args, kwargs = expression
                return rpget(self, name)(self, *args, **kwargs)
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

    def __str__(self):
        return self.__repr__()
