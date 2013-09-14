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

from colubrid.core import log
from colubrid import builtin

def create_json(script):
        script = script.replace('\'', '"')
        script = script.replace('(', '[')
        script = script.replace(')', ']')
        return script


def parse(parent, expression, line=False):
        expression_type = type(expression)
        try:
            if expression_type == list:
                length = len(expression)
                if length == 1:
                    return ['get', [expression[0]], {}]
                elif length > 1:
                    name = expression[0]
                    line = name == ''
                    if type(name) != str:
                        name = parse(parent, name)
                    args = map(lambda arg: parse(parent, arg, line=line),
                               expression[1])
                    kwargs = parse_kwargs(parent,
                                          expression[2]) if length == 3 \
                                                         else {}
                    return [name, args, kwargs]
            elif line:
                if expression_type == dict:
                    kwargs = parse_kwargs(parent, expression)
                    return ['set', [], kwargs]
                elif expression_type == str:
                    return
            elif expression_type in builtin.types:
                return [builtin.types[expression_type], [expression], {}]
            else:
                log.error('Syntax error in %s' % expression,
                            parent.logger, stop=True)
        except:
            log.raise_traceback(
            'Unknown error when parsing object type %s of %s.\n{tracemsg}' %
             (str(expression), expression_type.__name__), log=parent.logger)


def parse_kwargs(parent, kwargs):
    kwdict = {}
    for key in kwargs:
        kwdict[key] = parse(parent, kwargs[key])
    return kwdict
