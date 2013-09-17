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

from colubrid.types.function import Function


class WhileLoop(Function):
    __colubridname__ = 'while'
    build_args = False

    def function(self, parent, *args, **kwargs):
        wtdo = self.master.create_object(args[-1])
        while self.master.create_object(args[0]):
            wtdo(self)


While = WhileLoop()


class ForLoop(Function):
    __colubridname__ = 'for'
    build_args = False

    def function(self, parent, *args, **kwargs):
        wtdo = self.master.create_object(kwargs['do'])
        self.master.create_object(args[0]) # Start
        while self.master.create_object(args[1]): # Condition
            wtdo(self)
            self.master.create_object(args[2]) # Update


For = ForLoop()

loops = [For, While]
