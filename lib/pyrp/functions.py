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

from pyrp import builtin
from pyrp.types.function import Function
from pyrp.types.string import String


class Print(Function):
    __pyrpname__ = 'print'

    def function(self, module, *args, **kwargs):
        arguments = map(lambda arg: str(arg), args)
        print ' '.join(arguments)


class Input(Function):
    __pyrpname__ = 'input'

    def function(self, module, *args, **kwargs):
        prompt = str(args[0]) + ' '
        return String(module, raw_input(prompt))


class Set(Function):
    __pyrpname__ = 'set'

    def function(self, parent, *args, **kwargs):
        for name in kwargs:
            parent.set_object(str(name), kwargs[name])


class Get(Function):
    __pyrpname__ = 'get'

    def function(self, parent, *args, **kwargs):
        name = str(args[0])
        exists = parent.has_object(name)
        if exists:
            return parent.get_object(name, exists)
        else:
            return builtin.objects[name]

rpget = Get()
rpset = Set()
rpinput = Input()
rpprint = Print()

functions = [
    rpget,
    rpset,

    rpinput,
    rpprint
]
