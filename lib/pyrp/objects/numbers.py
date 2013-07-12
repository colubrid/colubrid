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


class Number:
    overtypes = []

    def __init__(self, module):
        self.module = module

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        if isinstance(other, Number):
            return make_number(self.module, self.number + other.number)
        super(Number, self).__add__(other)

    def __sub__(self, other):
        if isinstance(other, Number):
            return make_number(self.module, self.number - other.number)
        super(Number, self).__add__(other)

    def __mul__(self, other):
        if isinstance(other, Number):
            return make_number(self.module, self.number * other.number)
        super(Number, self).__mul__(other)

    def __div__(self, other):
        if isinstance(other, Number):
            return make_number(self.module, self.number / other.number)
        super(Number, self).__div__(other)


class Int(Number):
    def __init__(self, module, *args, **kwargs):
        Number.__init__(self, module)
        self.number = int(args[0])


class Float(Number):
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
