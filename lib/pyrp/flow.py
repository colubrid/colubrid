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


class Cache:
    def __init__(self, func):
        self.instances = {}
        self.func = func

    def __call__(self, module, *args, **kwargs):
        if not module in self.instances:
            self.instances[module] = self.func(module)
        return self.instances[module](module, *args, **kwargs)


class IfConditional(Function):
    __pyrpname__ = 'if'

    def function(self, module, *args, **kwargs):
        if args[0] and kwargs.has_key('do'):
            kwargs['do'](self)
        else:
            if kwargs.has_key(u'else'):
                kwargs['else'](self)


class AskConditional(Function):
    __pyrpname__ = '?'
    build_args = False

    def function(self, module, *args, **kwargs):
        if self.create_object(args[0]):
            return self.create_object(kwargs['if'])
        else:
            return self.create_object(kwargs['else'])


class IfCache(Cache, IfConditional):
    def __init__(self):
        Cache.__init__(self, IfConditional)


class AskCache(Cache, AskConditional):
    def __init__(self):
        Cache.__init__(self, AskConditional)


If = IfCache()
Ask = AskCache()

conditionals = [If, Ask]
