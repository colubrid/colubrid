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

from pyrp.strings import String
from pyrp.numbers import numbers
from pyrp.boolean import Boolean

from pyrp.function import variable_get
from pyrp.function import variable_set

from pyrp.function import pyrp_print
from pyrp.function import pyrp_input

from pyrp.operators import operators


types = {
    unicode: 'str',
    bool: 'bool'
}

objects = {
    # Types
    'str': String,
    'bool': Boolean,

    # Functions
    'get': variable_get,
    'set': variable_set,

    'print': pyrp_print,
    'input': pyrp_input
}

# Add operators

objects = dict(objects.items() + operators.items())

# Add  number types
for i in numbers:
    types[numbers[i][0]] = i
    objects[i] = numbers[i][1]
