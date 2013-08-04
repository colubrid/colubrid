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

from pyrp.boolean import Boolean
from pyrp.function import Function


class Operator(Function):
    def __init__(self, name, operation):
        self.__pyrpname__ = name
        self.operation = operation


class Arithmetic(Operator):
    def function(self, module, *args, **kwargs):
        current = args[0]
        for i in args[1:]:
            current = self.operation(current, i)
        return current


class Comparator(Operator):
    def function(self, module, *args, **kwargs):
        first = args[0]
        for i in args[1:]:
            if not self.operation(first, i):
                return Boolean(module, False)
        return Boolean(module, True)


class LogicalBin(Operator):
    def function(self, module, *args, **kwargs):
        current = args[0]
        for i in args[1:]:
            current = Boolean(module, self.operation(current, i))
        return current


class LogicalUn(Operator):
    def function(self, module, *args, **kwargs):
        for i in args:
            if not self.operation(i):
                return Boolean(module, False)
        return Boolean(module, True)


operators = [
             Arithmetic('+', lambda a, b: a + b),
             Arithmetic('-', lambda a, b: a - b),
             Arithmetic('*', lambda a, b: a * b),
             Arithmetic('/', lambda a, b: a / b),

             Comparator('>', lambda a, b: a > b),
             Comparator('<', lambda a, b: a < b),
             Comparator('=', lambda a, b: a == b),

             LogicalBin('and', lambda a, b: a and b),
             LogicalBin('or', lambda a, b: a or b),
             LogicalUn('not', lambda a: not a)
]
