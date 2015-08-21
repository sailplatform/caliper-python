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

from caliper.base import is_valid_URI
from caliper.constants import CALIPER_CLASSES


def _parse_context(ctxt):
    r = {}
    if not isinstance(ctxt, collections.MutableSequence):
            return r
    for entry in ctxt:
            if not isinstance(entry, collections.MutableMapping):
                    continue
            for k,v in entry.items():
                    if (isinstance(v, collections.MutableMapping) and
                        v.get('@id') and
                        v.get('@type') == '@id'):
                            r.update({k:v['@id']})
    return r


def from_json_dict(d):
    t = d.get('@type')
    if t and not CALIPER_CLASSES.get(t):
        raise ValueError('Unknown @type: {0}'.format(t))
    type_path = CALIPER_CLASSES.get(t) or d.__class__.__name__


    local_ids = _parse_context(d.get('@context'))

    r = {}
    for k,v in d.items():

        # transmogrify key or move to next item
        if k  in ['@type','@context']:
            continue
        elif k == '@id':
            key = 'entity_id'
        elif k == 'object':
            key = 'event_object'
        else:
            key = k

        # recursively condense value if complex, otherwise use value
        if isinstance(v, collections.MutableSequence):
            value = from_json_list(v)
        elif isinstance(v, collections.MutableMapping) and v.get('@type'):
            value = from_json_dict(v)
        elif is_valid_URI(v) and k in local_ids:
            value = from_json_dict({'@id': v, '@type': local_ids[k]})
        else:
            value = v

        r.update({key:value})

    if '.' not in type_path:
        m = 'builtins'
        c = type_path
    else:
        m,c = type_path.rsplit('.',1)

    TheClass = getattr(importlib.import_module(m),c)

    return TheClass(**r)


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
