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

from pyrp.object import PyRPObject


class String(PyRPObject):
    __pyrpname__ = 'str'
    __converttype__ = unicode

    def __init__(self, module, *args, **kwargs):
        PyRPObject.__init__(self, module)
        self.string = args[0]

    def __str__(self):
        return self.string

    def __cmp__(self, other):
        a = self.string
        b = other.string
        return 0 if a == b else -1 if a < b else 1
