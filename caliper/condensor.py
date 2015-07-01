# -*- coding: utf-8 -*-
# Caliper-python package, condensor module
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements. See the NOTICE file distributed with this
# work for additional information.
#
# IMS Caliper is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# IMS Caliper is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from builtins import *

import collections, importlib

from caliper.constants import CALIPER_CLASSES

def from_json_dict(d):
    type_path = CALIPER_CLASSES.get(d.get('@type'))
    if not type_path:
        raise ValueError('Unknown @type')

    r = {}
    for k,v in d.items():

        # transmogrify key or move to next item
        if k  in ['@type','@context']:
            continue
        else:
            key = k

        # recursively condense value if complex, otherwise use value
        if isinstance(v, collections.MutableSequence):
            value = from_json_list(v)
        elif isinstance(v, collections.MutableMapping) and v.get('@type'):
            value = from_json_dict(v)
        else:
            value = v

        r.update({key:value})

    m,c = type_path.rsplit('.',1)
    TheClass = getattr(importlib.import_module(m),c)

    return TheClass(entity_id=r.get('@id'), **r)


def from_json_list(l):
    r = []
    for item in l:
        if isinstance(item, collections.MutableSequence):
            r.append(from_json_list(item))
        elif isinstance(item, collections.MutableMapping) and item.get('@type'):
            r.append(from_json_dict(item))
        else:
            r.append(item)
    return r or None
