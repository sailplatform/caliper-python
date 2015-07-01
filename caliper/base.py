# -*- coding: utf-8 -*-
# Caliper-python package, base module
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
from future.utils import with_metaclass
from builtins import *


import collections, copy, importlib, json
from oauthlib import uri_validate as oauthlib_uri_validate

from caliper.constants import CALIPER_CLASSES

## convenience functions
def is_valid_URI(uri):
    if isinstance(uri, str) and oauthlib_uri_validate.is_uri(uri):
        return True
    else:
        return False

def is_subtype(tname1, tname2):
    m1,c1 = CALIPER_CLASSES.get(tname1).rsplit('.',1)
    m2,c2 = CALIPER_CLASSES.get(tname2).rsplit('.',1)    
    return issubclass( getattr(importlib.import_module(m1),c1),
                       getattr(importlib.import_module(m2),c2))

### Default configuration values ###
class Options(object):
    _config = {
        'API_KEY': None,
        'CONNECTION_REQUEST_TIMEOUT': None,
        'CONNECTION_TIMEOUT': None,
        'HOST' : None,
        'SOCKET_TIMEOUT': None,
        }

    def __init__(self):
        pass

    @property
    def API_KEY(self):
        return self._config['API_KEY']
    @API_KEY.setter
    def API_KEY(self, new_key):
        if isinstance(new_key, str):
            self._config['API_KEY'] = new_key
        else:
            raise ValueError('new key value must be a string')

    @property
    def CONNECTION_REQUEST_TIMEOUT(self):
        return self._config['CONNECTION_REQUEST_TIMEOUT']
    @CONNECTION_REQUEST_TIMEOUT.setter
    def CONNECTION_REQUEST_TIMEOUT(self, new_timeout):
        if int(new_timeout) >= 1000:
            self._config['CONNECTION_REQUEST_TIMEOUT'] = int(new_timeout)
        else:
            raise ValueError('new timeout value must be at least 1000 milliseconds')
        
    @property
    def CONNECTION_TIMEOUT(self):
        return self._config['CONNECTION_TIMEOUT']
    @CONNECTION_TIMEOUT.setter
    def CONNECTION_TIMEOUT(self, new_timeout):
        if int(new_timeout) >= 1000:
            self._config['CONNECTION_TIMEOUT'] = int(new_timeout)
        else:
            raise ValueError('new timeout value must be at least 1000 milliseconds')

    @property
    def HOST(self):
        return self._config['HOST']
    @HOST.setter
    def HOST(self,new_host):
        if is_valid_URI(new_host):
            self._config['HOST'] = str(new_host)

    @property
    def SOCKET_TIMEOUT(self):
        return self._config['SOCKET_TIMEOUT']
    @SOCKET_TIMEOUT.setter
    def SOCKET_TIMEOUT(self, new_timeout):
        if int(new_timeout) >= 1000:
            self._config['SOCKET_TIMEOUT'] = int(new_timeout)
        else:
            raise ValueError('new timeout value must be at least 1000 milliseconds')
        
class HttpOptions(Options):
    def __init__(self,
            api_key='CaliperKey',
            connection_request_timeout=10000,
            connection_timeout=10000,
            host='http://httpbin.org/post',
            socket_timeout=10000,
            ):
        Options.__init__(self)
        self.API_KEY=api_key
        self.CONNECTION_REQUEST_TIMEOUT=connection_request_timeout
        self.CONNECTION_TIMEOUT=connection_timeout
        self.HOST=host
        self.SOCKET_TIMEOUT=socket_timeout

### Caliper serializable base class for all caliper objects that need serialization ###
class CaliperSerializable(object):
    def __init__(self):
        self._objects = {}
        self._props = {}

    def _set_object(self,k,v):
        self._objects.update({k:v})

    def _set_prop(self,k,v):
        self._props.update({k:v})

    def _set_float_prop(self,k,v):
        if v == None:
            self._set_prop(k,None)
        else:
            self._set_prop(k,float(v))

    def _set_bool_prop(self,k,v):
        if v == None:
            self._set_prop(k,None)
        else:
            self._set_prop(k,bool(v))

    def _set_id_prop(self,k,v,t):
        val = None
        if is_valid_URI(v):
            val = v
        elif (isinstance(v, CaliperSerializable)
              and is_subtype(v.type,t) ):
            val = v.id
            self._set_object(k,v)
        elif (isinstance(v, collections.MutableMapping)
              and is_subtype(v.get('@type'),t)
              and is_valid_URI(v.get('@id')) ):
            val = v.get('@id')
            self._set_object(k,v)
        self._set_str_prop(k,val)
            
    def _set_int_prop(self,k,v):
        if v == None:
            self._set_prop(k,None)
        else:
            self._set_prop(k,int(v))

    def _set_list_prop(self,k,v):
        self._set_prop(k,v or [])

    def _append_list_prop(self,k,v):
        if (not k in self._props) or (self._props[k] is None):
            self._set_list_prop(k,[v])
        elif isinstance(self._props[k], collections.MutableSequence):
            self._props[k].append(v)
        else:
            raise ValueError('attempt to append to a non-list property')

    def _set_obj_prop(self,k,v):
        self._set_prop(k,v)

    def _set_str_prop(self,k,v):
        if v == None:
            self._set_prop(k,None)
        else:
            self._set_prop(k,str(v))

    def _get_prop(self,k):
        return self._objects.get(k) or self._props.get(k)

    def _unpack_list(self,l,
                     no_deep_context=False,
                     no_nulls=False,
                     no_objects=False):
        r = []
        for item in l:
            if isinstance(item, collections.MutableSequence):
                r.append(self._unpack_list(item,
                                           no_deep_context=no_deep_context,
                                           no_nulls=no_nulls,
                                           no_objects=no_objects))
            elif isinstance(item, CaliperSerializable):
                r.append(item.as_dict(no_deep_context=no_deep_context,
                                      no_nulls=no_nulls,
                                      no_objects=no_objects))
            else:
                r.append(item)
        return r

    def as_dict(self,
                no_deep_context=False,
                no_nulls=False,
                no_objects=False):
        r = {}
        for k,v in self._props.items():

            # handle value based on its type: list, composite, or basic type
            if no_nulls and v == None:
                continue
            elif no_deep_context and k == '@context':
                continue
            elif isinstance(v, collections.MutableSequence):
                value = self._unpack_list(v,
                                          no_deep_context=no_deep_context,
                                          no_nulls=no_nulls,
                                          no_objects=no_objects)
            elif isinstance(v, CaliperSerializable):
                value = v.as_dict(no_deep_context=no_deep_context,
                                  no_nulls=no_nulls,
                                  no_objects=no_objects)
            elif isinstance(v, collections.MutableMapping):
                if no_nulls and not v:
                    continue
                value = v
            elif not(no_objects) and (k in self._objects):
                value = self._objects[k]
            else:
                value = v
            r.update({k:value})
            
        return copy.deepcopy(r)

    def as_json(self,no_deep_context=False,no_nulls=False):
        r = self.as_dict(no_deep_context=no_deep_context,
                         no_objects=True,
                         no_nulls=no_nulls)
        if '@context' in self._props:
            r.update({'@context':self._props['@context']})
        return json.dumps(r,sort_keys=True)

### Profiles ###
class MetaProfile(type):
    @property
    def Actions(cls):
        return cls._actions

class BaseProfile(with_metaclass(MetaProfile, object)):
    pass

### Roles ###
class MetaRole(type):
    @property
    def Roles(cls):
        return cls._roles

class BaseRole(with_metaclass(MetaRole, object)):
    pass

### Statuses ###
class MetaStatus(type):
    @property
    def Statuses(cls):
        return cls._statuses

class BaseStatus(with_metaclass(MetaStatus, object)):
    pass

