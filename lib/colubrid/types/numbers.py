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

from colubrid.types.object import ColubridObject


class Number(ColubridObject):
    overtypes = []

    def __init__(self, module):
        ColubridObject.__init__(self, module)
        self.module = module

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return self.number.__repr__()

    def binary_operator(func):
        def inner(self, b):
            if isinstance(b, Number):
                return func(self.module, self.number, b.number)
            else:
                # TODO: Create type checking function
                print "Operation not supported"
                exit()
        return inner

    def numeric_operation(func):
        return lambda m, a, b: make_number(m, func(a, b))

    @binary_operator
    @numeric_operation
    def __add__(a, b):
        return a + b

    @binary_operator
    @numeric_operation
    def __sub__(a, b):
        return a - b

    @binary_operator
    @numeric_operation
    def __mul__(a, b):
        return a * b

    @binary_operator
    @numeric_operation
    def __div__(a, b):
        return a / b

    @binary_operator
    def __cmp__(module, a, b):
        return 0 if a == b else 1 if a > b else -1


class Int(Number):
    __colubridname__ = 'int'
    __converttype__ = int

    def __init__(self, module, *args, **kwargs):
        Number.__init__(self, module)
        self.number = int(args[0])


class Float(Number):
    __colubridname__ = 'float'
    __converttype__ = float
    overtypes = [Int]

    def __init__(self, module, *args, **kwargs):
        Number.__init__(self, module)
        self.number = float(args[0])


numbers = {'int': (int, Int),
           'float': (float, Float)}


def make_number(module, number):
    number_type = type(number)
    for i in numbers:
        if number_type == numbers[i][0]:
            return numbers[i][1](module, number)
