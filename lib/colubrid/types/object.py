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

from colubrid.core import log

INDEP = 1
DEP = 0
PART = -1


class ColubridObject:
    __colubridname__ = 'object'
    __converttype__ = None
    __relation__ = PART

    def __init__(self, parent):
        self.logger_name = '%s:%s' % (parent.logger_name, self.__colubridname__)\
                            if parent is not None else self.__colubridname__
        self.logger = log.get_logger(self.logger_name)
        self.objects = {}
        self.parent = parent

    def has_object(self, name):
        if name in self.objects:
            return 2
        if self.parent:
            if self.parent.has_object(name):
                return 1
        else:
            return 0

    def get_object(self, name, place=None):
        if place is None:
            place = self.has_object(name)
        if place > 0:
            if place == 1:
                return self.parent.get_object(name)
            else:
                return self.objects[name]
        else:
            return None

    def set_object(self, name, obj):
        where = self.has_object(name)
        here = False if self.__relation__ == PART else False\
                if self.__relation__ == DEP and where == 1 else True
        if here:
            self.objects[name] = obj
        else:
            self.parent.set_object(name, obj)

    def create_object(self, expression):
        from colubrid.functions import rpget
        try:
            if type(expression) == list:  # This object needs to be built.
                name, args, kwargs = expression
                name = self.create_object(name)
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
