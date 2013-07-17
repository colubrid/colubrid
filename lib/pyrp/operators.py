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


def arithmetic(operation):
    def inner(module, *args, **kwargs):
        current = args[0]
        for i in args[1:]:
            current = operation(current, i)
        return current
    return inner


def comparator(operation):
    def inner(module, *args, **kwargs):
        first = args[0]
        for i in args[1:]:
            if not operation(first, i):
                return Boolean(module, False)
        return Boolean(module, True)
    return inner


@arithmetic
def addition(a, b):
    return a + b


@arithmetic
def substraction(a, b):
    return a - b


@arithmetic
def multiplication(a, b):
    return a * b


@arithmetic
def division(a, b):
    return a / b


@comparator
def bigger(a, b):
    return a > b


@comparator
def smaller(a, b):
    return a < b


@comparator
def equal(a, b):
    return a == b


operators = {
        # Arithmetic operators
        '+': addition,
        '-': substraction,
        '/': division,
        '*': multiplication,

        # Comparative operators
        '>': bigger,
        '<': smaller,
        '=': equal
}
