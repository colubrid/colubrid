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

import os
import json
from pyrp.core import log
from pyrp.parser import create_json
from pyrp.parser import parse
from pyrp.types.code import Code
from pyrp.types.object import INDEP
from pyrp.types.object import PyRPObject


class Module(PyRPObject):
    __relation__ = INDEP

    def __init__(self, filepath, main=False, isjson=False, tree=False):
        self.__pyrpname__ = os.path.basename(filepath)
        PyRPObject.__init__(self, None)

        file_object = open(filepath, 'r')
        script = file_object.read()
        file_object.close()

        if not tree:
            if not isjson:
                script = create_json(script)
            content = json.loads(script)
            self.content = []

            for i in content:
                checked = parse(self, i, line=True)
                if checked:
                    self.content.append(checked)
        else:
            self.content = json.loads(script)

        if main:
            self.run()

    def run(self):
        log.debug('Running', self.logger)
        Code(self, *self.content)(self)
