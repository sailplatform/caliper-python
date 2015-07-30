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

import collections, copy, importlib, json, re
from oauthlib import uri_validate as oauthlib_uri_validate

from caliper.constants import CALIPER_CLASSES

## Convenience functions
def is_valid_URI(uri):
    if not uri:
        return False
    elif isinstance(uri, str) and oauthlib_uri_validate.is_uri(uri):
        return True
    else:
        return False

def is_subtype(type_1, type_2):
    if (type_1 == None) or (type_2 == None):
        return False
    if isinstance(type_1, type):
        m1 = type_1.__module__
        c1 = type_1.__name__
    else:
        m1,c1 = CALIPER_CLASSES.get(type_1).rsplit('.',1)
    if isinstance(type_2, type):
        m2 = type_2.__module__
        c2 = type_2.__name__
    else:
        m2,c2 = CALIPER_CLASSES.get(type_2).rsplit('.',1)
    return issubclass( getattr(importlib.import_module(m1),c1),
                       getattr(importlib.import_module(m2),c2))

def ensure_type(p,t):
    # exception or True
    if t == None:
        raise ValueError("type cannot be None type")
    if not( (isinstance(p, BaseEntity) and is_subtype(p.type,t)) or
            (isinstance(p, collections.MutableMapping) and is_subtype(p['@type'],t)) or
            (isinstance(p,t)) ):
        raise TypeError("Property must be of type {0}".format(str(t)))
    return True

def ensure_list_type(l,t):
    # exception or True
    for i in l:
        ensure_type(i,t)
    return True


### Default configuration values ###
class Options(object):
    _config = {
        'API_KEY': None,
        'CONNECTION_REQUEST_TIMEOUT': None,
        'CONNECTION_TIMEOUT': None,
        'HOST' : None,
        'OPTIMIZE_SERIALIZATION': False,
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
    def OPTIMIZE_SERIALIZATION(self):
        return self._config['OPTIMIZE_SERIALIZATION']
    @OPTIMIZE_SERIALIZATION.setter
    def OPTIMIZE_SERIALIZATION(self, optimize):
        if optimize:
            self._config['OPTIMIZE_SERIALIZATION'] = True
        else:
            self._config['OPTIMIZE_SERIALIZATION'] = False

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
            optimize_serialization=False,
            socket_timeout=10000,
            ):
        Options.__init__(self)
        self.API_KEY=api_key
        self.CONNECTION_REQUEST_TIMEOUT=connection_request_timeout
        self.CONNECTION_TIMEOUT=connection_timeout
        self.HOST=host
        self.OPTIMIZE_SERIALIZATION=optimize_serialization
        self.SOCKET_TIMEOUT=socket_timeout


### Caliper serializable base class for all caliper objects that need serialization ###
class CaliperSerializable(object):
    def __init__(self):
        self._objects = {}
        self._props = {}
        self._context = {'base': None, 'local': [] }

    # these methods are the only ones that directly touch the object's underlying
    # property/object cache
    def _get_prop(self,k):
        return self._objects.get(k) or self._props.get(k)
    
    def _update_objects(self,k,v,req=False):
        if req and (v == None):
            pass
        elif k:
            self._objects.update({k:v})

    def _update_props(self,k,v,req=False):
        if req and (v == None):
            raise ValueError('{0} must have a non-null value'.format(str(k)))
        if k:
            self._props.update({k:v})

    def _update_base_context(self,v):
        if v:
            self._context['base']=v

    def _update_local_context(self,v):
        if v:
           self._context['local'].append(v)

    def _is_in_local_context(self,k):
        for item in self._context['local']:
            if ( self._context['local'][item] == k or
                 ( isinstance(self._context['local'][item], collections.MutableMapping) and
                   k in self._context['local'][item] ) ):
                return True
        else:
            return False


    # protected base-type setters that inheriting classes use internally to set
    # underlying state
    def _set_bool_prop(self,k,v,req=False):
        if v == None:
            self._update_props(k,None,req=req)
        else:
            self._update_props(k,bool(v),req=req)

    def _set_int_prop(self,k,v,req=False):
        if v == None:
            self._update_props(k,None,req=req)
        else:
            self._update_props(k,int(v),req=req)

    def _set_float_prop(self,k,v,req=False):
        if v == None:
            self._update_props(k,None,req=req)
        else:
            self._update_props(k,float(v),req=req)

    def _set_str_prop(self,k,v,req=False):
        if v == None:
            self._update_props(k,None,req=req)
        else:
            self._update_props(k,str(v),req=req)

    # protected complex-type setters
    def _set_base_context(self,v):
        if v and not is_valid_URI(v):
            raise ValueError('Base context must be a valid URI')
        self._update_base_context(v)
        
    def _set_id_prop(self,k,v,t,req=False):
        val = None
        if is_valid_URI(v):
            val = v
        elif (isinstance(v, BaseEntity) 
              and is_subtype(v.type,t) ):
            val = v.id
            self._update_objects(k,v,req=req)
        elif (isinstance(v, collections.MutableMapping)
              and is_subtype(v.get('@type'),t)
              and is_valid_URI(v.get('@id')) ):
            val = v.get('@id')
            self._update_objects(k,v,req=req)
        self._set_str_prop(k,val,req=req)
            
    def _set_list_prop(self,k,v,t=None,req=False):
        if req and (v==None):
            raise ValueError('{0} must have a non-null value'.format(str(k)))
        elif v:
            if not( isinstance(v, collections.MutableSequence)):
                raise ValueError('{0} must be a list'.format(str(k)))
            elif t:
                for item in v:
                    ensure_type(item,t)
        self._update_props(k,v or [],req=req)

    def _set_obj_prop(self,k,v,t=None,req=False,id_only=False):
        if req and (v==None):
            raise ValueError('{0} must have a non-null value'.format(str(k)))
        if isinstance(v, BaseEntity) and not(is_subtype(v.type,t)):
            self._update_props(k,None)
        else:
            if not id_only:
                self._update_props(k,v)
            else:
                the_type = getattr(v,'type', None)
                if the_type and not is_valid_URI(the_type):
                    raise ValueError("Value's type must be a valid URI")
                self._update_local_context( {k:{'@id':the_type, '@type':'@id'}} )
                self._set_id_prop(k,v)


    # protected unpacker methods, used by dict and json-string representation
    # public functions
    def _unpack_context(self,ctxt_bases=[]):
        r = []
        for item in self._context['local']:
            if item not in ctxt_bases:
                r.append(item)
        if self._context['base'] and (self._context['base'] not in ctxt_bases):
            if r:
                r.insert(0,self._context['base'])
            else:
                r = self._context['base']
        return copy.deepcopy(r)

    def _unpack_list(self,l,
                     ctxt_bases=[],
                     described_entities=[],
                     thin_context=False,
                     thin_props=False):
        r = []
        for item in l:
            if isinstance(item, collections.MutableSequence):
                r.append(self._unpack_list(item,
                                           ctxt_bases=ctxt_bases,
                                           described_entities=described_entities,
                                           thin_context=thin_context,
                                           thin_props=thin_props))
            elif isinstance(item, CaliperSerializable):
                r.append(item._unpack_object(ctxt_bases=ctxt_bases,
                                             described_entities=described_entities,
                                             thin_context=thin_context,
                                             thin_props=thin_props))
            else:
                r.append(copy.deepcopy(item))
        return r

    def _update_context(self,context,k,v):
        if not self._is_in_local_context(k):
            lc = {k:{'@id':v, '@type':'@id'}}
            if context == None:
                return [lc]
            elif isinstance(context,str):
                return [context,lc]
            elif isinstance(context, collections.MutableSequence):
                return context + [lc]
            else:
                return None

    def _unpack_object(self,
                       ctxt_bases = [],
                       described_entities=[],
                       thin_context=False,
                       thin_props=False):
        r = {}
        cb = copy.deepcopy(ctxt_bases)
        ctxt_prop = self._unpack_context(ctxt_bases=cb)
        if ctxt_prop:
            r.update({'@context':ctxt_prop})

        for k,v in sorted(self._props.items()):
            if thin_context and self._context['base']:
                cb.append(self._context['base'])
            else:
                cb = []

            # handle value based on its type: list, composite, or basic type
            if thin_props and ( v == None or v == {} or v == [] ):
                continue
            elif isinstance(v, collections.MutableSequence):
                value = self._unpack_list(v,
                                          ctxt_bases=cb,
                                          described_entities=described_entities,
                                          thin_context=thin_context,
                                          thin_props=thin_props)
            elif isinstance(v, BaseEntity):
                if v.id in described_entities:
                    r.update({'@context': self._update_context(r.get('@context'), k, v.type)})
                    value = v.id
                else:
                    value = v._unpack_object(ctxt_bases=cb,
                                             described_entities=described_entities,
                                             thin_context=thin_context,
                                             thin_props=thin_props)
            elif isinstance(v, CaliperSerializable):
                the_id = v._get_prop('@id')
                the_type = v._get_prop('@type')
                if (the_id and the_type) and (the_id in described_entities):
                    r.update({'@context': self._update_context(r.get('@context'), k, the_type)})
                    value = the_id
                else:
                    value = v._unpack_object(ctxt_bases=cb,
                                             described_entities=described_entities,
                                             thin_context=thin_context,
                                             thin_props=thin_props)
            elif isinstance(v, collections.MutableMapping):
                the_id = v.get('@id')
                the_type = v.get('@type')
                if (the_id and the_type) and (the_id in described_entities):
                    r.update({'@context': self._update_context(r.get('@context'), k, the_type)})
                    value = the_id
                else:
                    value = v
            else:
                value = v
            r.update({k:value})
            
        return copy.deepcopy(r)


    # public methods, to repr this event or entity as a dict or as a json-string
    def as_dict(self,
                described_entities=None,
                thin_context=False,
                thin_props=False):
        return self._unpack_object(described_entities=described_entities or [],
                                   thin_context=thin_context,
                                   thin_props=thin_props)

    def as_json(self,
                described_entities=None,
                thin_context=False,
                thin_props=False):
        r = self.as_dict(described_entities=described_entities,
                         thin_context=thin_context,
                         thin_props=thin_props)
        return json.dumps(r,sort_keys=True)

    def as_json_with_ids(self,
                described_entities=None,
                thin_context=False,
                thin_props=False):
        ret = self.as_json(described_entities=described_entities,
                           thin_context=thin_context,
                           thin_props=thin_props)
        return ret, re.findall(r'"@id": "(.+?(?="))"',
                               re.sub(r'"@context": \[.+?\],','', ret))

        


### Entities and Events ###
class BaseEntity(CaliperSerializable):
    def __init__(self):
        CaliperSerializable.__init__(self)

class BaseEvent(CaliperSerializable):
    def __init__(self):
        CaliperSerializable.__init__(self)

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

