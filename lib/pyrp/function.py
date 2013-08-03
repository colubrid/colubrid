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

from pyrp.object import DEP
from pyrp.object import PyRPObject


class Function(PyRPObject):
    __relation__ = DEP
    build_args = True

    def __init__(self, parent=None):
        self.__name__ = self.__pyrpname__
        PyRPObject.__init__(self, parent)
        self.master = self

    def __call__(self, module, *args, **kwargs):
        if module:
            self.master = module
        if self.build_args:
            argv = map(self.master.create_object, args)
            kwargv = self.master.create_kwargs(kwargs)
        else:
            argv = args
            kwargv = kwargs
        return self.function(module, *argv, **kwargv)
