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
from future.utils import raise_with_traceback
from builtins import *

import copy, collections, importlib

from caliper.base import is_valid_URI, is_valid_date
from caliper.constants import CALIPER_CLASSES


def from_caliper_envelope(d):
    r = None
    if (is_valid_URI(d.get('sensor')) and is_valid_date(d.get('sendTime')) and
            isinstance(d.get('data'), collections.MutableSequence)):
        r = from_json_list(d.get('data'))
    return r


def from_json_dict(d):
    t = d.get('type')
    if t and not CALIPER_CLASSES.get(t):
        return copy.deepcopy(d)
    type_path = CALIPER_CLASSES.get(t) or d.__class__.__name__

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
        if CALIPER_CLASSES.get(t) and k in ['extensions']:
            value = v
        elif k in ['@context']:
            value = v
        elif isinstance(v, collections.MutableSequence):
            value = from_json_list(v)
        elif isinstance(v, collections.MutableMapping) and CALIPER_CLASSES.get(v.get('type')):
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


def from_json_list(l):
    r = []
    for item in l:
        if isinstance(item, collections.MutableSequence):
            r.append(from_json_list(item))
        elif isinstance(item, collections.MutableMapping):
            r.append(from_json_dict(item))
        else:
            r.append(item)
    return r or None

