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

from pyrp.function import Function
from pyrp.string import String


class Print(Function):
    __pyrpname__ = 'print'

    def __call__(self, module, *args, **kwargs):
        arguments = map(lambda arg: str(arg), args)
        print ' '.join(arguments)


class Input(Function):
    __pyrpname__ = 'input'

    def __call__(self, module, *args, **kwargs):
        prompt = str(args[0]) + ' '
        return String(module, raw_input(prompt))


class Set(Function):
    __pyrpname__ = 'set'

    def __call__(self, module, *args, **kwargs):
        module.objects[str(args[0])] = args[1]


class Get(Function):
    __pyrpname__ = 'get'

    def __call__(self, module, *args, **kwargs):
        return module.objects[str(args[0])]


functions = [
    Get(),
    Set(),

    Input(),
    Print()
]
