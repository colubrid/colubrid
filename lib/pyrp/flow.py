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


class IfConditional(Function):
    __pyrpname__ = 'if'

    def function(self, module, *args, **kwargs):
        if args[0] and kwargs.has_key(u'do'):
            kwargs['do'](self)


class IfCache(IfConditional):
    def __init__(self):
        IfConditional.__init__(self)
        self.instances = {}

    def __call__(self, module, *args, **kwargs):
        if not module in self.instances:
            self.instances[module] = IfConditional(module)
        return self.instances[module](module, *args, **kwargs)

If = IfCache()
