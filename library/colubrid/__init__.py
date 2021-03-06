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

from colubrid import builtin
from colubrid.flow import conditionals
from colubrid.functions import functions
from colubrid.loop import loops
from colubrid.operators import operators
from colubrid.types import types
from colubrid.types.module import Module

builtin_objects = []
builtin_objects += conditionals
builtin_objects += functions
builtin_objects += loops
builtin_objects += operators
builtin_objects += types

for i in builtin_objects:
    builtin.add_object(i)


def main(filepath, isjson, tree):
    Module(filepath, main=True, isjson=isjson, tree=tree)
