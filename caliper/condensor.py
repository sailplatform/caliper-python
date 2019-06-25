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

try:
    from collections.abc import MutableSequence, MutableMapping
except ImportError:
    from collections import MutableSequence, MutableMapping

import copy
import importlib

from caliper.base import is_valid_context, is_valid_datetime, is_valid_URI
from caliper.constants import CALIPER_CLASSES, CALIPER_CORE_CONTEXT, CALIPER_TYPES, EVENT_TYPES


def from_caliper_envelope(d, strict=False):
    r = None
    if (is_valid_URI(d.get('sensor')) and is_valid_datetime(d.get('sendTime'))
            and isinstance(d.get('data'), MutableSequence)):
        r = from_json_list(d.get('data'), strict=strict)
    return r


def from_json_dict(d, strict=False):
    ctxt = d.get('@context')
    id = d.get('id')
    typ = d.get('type')

    if strict and not is_valid_context(ctxt, CALIPER_CORE_CONTEXT):
        raise ValueError('While strictly parsing, encountered unknown context: {}'.format(ctxt))
    else:
        ctxt = ctxt or CALIPER_CORE_CONTEXT
    if strict and typ not in CALIPER_TYPES.values():
        raise ValueError('While strictly parsing, encountered unknown type: {}'.format(typ))
    if strict and typ in EVENT_TYPES.values() and not id:
        raise ValueError('While strictly parsing, encountered event with no id: {}'.format(typ))

    if typ and not CALIPER_CLASSES.get(typ):
        return copy.deepcopy(d)
    type_path = CALIPER_CLASSES.get(typ) or d.__class__.__name__

    r = {}
    for k, v in d.items():

        # transmogrify key or move to next item
        if k in ['type']:
            continue
        elif k in ['@context']:
            key = 'context'
        else:
            key = k

        # recursively condense value if complex, otherwise use value
        if CALIPER_CLASSES.get(typ) and k in ['extensions']:
            value = v
        elif k in ['@context']:
            value = v
        elif isinstance(v, MutableSequence):
            value = from_json_list(v)
        elif isinstance(v, MutableMapping) and CALIPER_CLASSES.get(v.get('type')):
            value = from_json_dict(v)
        else:
            value = v

        r.update({key: value})

    if '.' not in type_path:
        m = 'builtins'
        c = type_path
    else:
        m, c = type_path.rsplit('.', 1)

    TheClass = getattr(importlib.import_module(m), c)

    return TheClass(**r)


def from_json_list(l, strict=False):
    r = []
    for item in l:
        if isinstance(item, MutableSequence):
            r.append(from_json_list(item, strict=strict))
        elif isinstance(item, MutableMapping):
            r.append(from_json_dict(item, strict=strict))
        else:
            r.append(item)
    return r or None
