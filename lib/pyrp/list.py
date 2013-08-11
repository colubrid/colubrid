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


class List(PyRPObject):
    __pyrpname__ = 'list'

    def __init__(self, module, *args, **kwargs):
        PyRPObject.__init__(self, module)
        self.array = map(module.create_object, args)

    def __repr__(self):
        return '[\'list\', (%s)]' % self.array.__repr__()[1:-1]

    def __getitem__(self, item):
        return self.array(item)

    def __len__(self):
        return len(self.array)
