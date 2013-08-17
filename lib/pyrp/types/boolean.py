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

from pyrp.types.object import PyRPObject


class Boolean(PyRPObject):
    __pyrpname__ = 'bool'
    __converttype__ = bool

    def __init__(self, module, *args, **kwargs):
        PyRPObject.__init__(self, module)
        self.module = module
        self.value = bool(args[0])

    def __str__(self):
        return 'true' if self.value else 'false'

    def __repr__(self):
        return self.__str__()

    def __nonzero__(self):
        return self.value