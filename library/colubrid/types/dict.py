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


class Dict(ColubridObject):
    __colubridname__ = 'dict'

    def __init__(self, module, *args, **kwargs):
        ColubridObject.__init__(self, module)
        self.dictionary = self.create_kwargs(kwargs)

    def __repr__(self):
        return '[\'dict\', (), %s]' % self.dictionary.__repr__()

    def __str__(self):
        return str(self.dictionary)

    def __getitem__(self, item):
        return self.dictionary(item)

    def __len__(self):
        try:
            return len(self.dictionary)
        except:
            return 0
