# -*- coding: utf-8 -*-
# Caliper-python package, base module
#
# Copyright (c) 2014 IMS Global Learning Consortium, Inc. All Rights Reserved.
# Trademark Information- http://www.imsglobal.org/copyright.html

# IMS Global Caliper Analytics™ APIs are publicly licensed as Open Source
# Software via GNU General Public License version 3.0 GPL v3. This license
# contains terms incompatible with use in closed-source software including a
# copyleft provision.

# IMS Global also makes available an Alternative License based on the GNU Lesser
# General Public License. LGPL v3 Licensees (via the Alternative License) are
# required to be IMS Global members. Membership in IMS is a commitment by a
# supplier to the IMS community for ongoing support for achieving "plug and play"
# integration.  IMS Membership dues pay for ongoing maintenance for the
# Alternative License to be applicable to updates to the Caliper Analytics
# APIs. The rationale for this dual-license approach and membership component is
# to help assure a requisite level of ongoing development, project management,
# and support for the software.

# Licensees of IMS Global Caliper Analytics APIs are strongly encouraged to
# become active contributors to the Caliper Analytics project and other projects
# within IMS Global. Prospective licensees should understand that their initial
# base contribution and ongoing membership fees are insufficient to fully fund
# the ongoing development and maintenance of Caliper APIs and that voluntary
# contributions are the primary "fuel" ensuring any open source project's
# viability. Contributions can include development, bug fixing, bug reporting,
# performance analysis, and other aspects of the overall development process.

# Contributor status at the "github" level will be individual-based. Contributors
# will need to sign an IMS Global Contributor License Agreement (CLA) that grants
# IMS Global a license to contributions.

# If you are interested in licensing the IMS Global Caliper Analytics APIs please
# email licenses@imsglobal.org

import collections
import copy
import json
from rfc3987 import parse as rfc3987_parse
import six


### Default configuration values ###

class Options(object):
    _config = {
        'API_KEY': None,
        'HOST' : None,
        'CONNECTION_TIMEOUT': None,
        'SO_TIMEOUT': None,
        'CONNECTION_REQUEST_TIMEOUT': None,
        }

    def __init__(self):
        pass

    @property
    def API_KEY(self):
        return self._config['API_KEY']
    @API_KEY.setter
    def API_KEY(self, new_key):
        if isinstance(new_key, six.string_types):
            self._config['API_KEY'] = str(new_key)
        else:
            raise ValueError('new key value must be a string')
        
    @property
    def HOST(self):
        return self._config['HOST']
    @HOST.setter
    def HOST(self,new_host):
        if rfc3987_parse(new_host, rule='URI'):
            self._config['HOST'] = str(new_host)

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
    def SO_TIMEOUT(self):
        return self._config['SO_TIMEOUT']
    @SO_TIMEOUT.setter
    def SO_TIMEOUT(self, new_timeout):
        if int(new_timeout) >= 1000:
            self._config['SO_TIMEOUT'] = int(new_timeout)
        else:
            raise ValueError('new timeout value must be at least 1000 milliseconds')

    @property
    def CONNECTION_REQUEST_TIMEOUT(self):
        return self._config['CONNECTION_REQUEST_TIMEOUT']
    @CONNECTION_REQUEST_TIMEOUT.setter
    def CONNECTION_REQUEST_TIMEOUT(self, new_timeout):
        if int(new_timeout) >= 1000:
            self._config['CONNECTION_REQUEST_TIMEOUT'] = int(new_timeout)
        else:
            raise ValueError('new timeout value must be at least 1000 milliseconds')
        
class HttpOptions(Options):
    def __init__(self,
            api_key='CaliperKey',
            host='http://httpbin.org/post',
            connection_timeout=10000,
            so_timeout=10000,
            connection_request_timeout=10000):
        Options.__init__(self)
        self.API_KEY=api_key
        self.HOST=host
        self.CONNECTION_TIMEOUT=connection_timeout
        self.SO_TIMEOUT=so_timeout
        self.CONNECTION_REQUEST_TIMEOUT=connection_request_timeout

### Caliper serializable base class for all caliper objects that need serialization ###
class CaliperSerializable(object):
    def __init__(self):
        self._props = {}
        self._prop_name_map = {}

    def _set_prop(self,k,v,name=None):
        self._props.update({k:v})
        if name:
            self._prop_name_map.update({k:name})

    def _set_float_prop(self,k,v,name=None):
        if v == None:
            self._set_prop(k,None,name)
        else:
            self._set_prop(k, float(v), name)

    def _set_bool_prop(self,k,v,name=None):
        if v == None:
            self._set_prop(k, None, name)
        else:
            self._set_prop(k, bool(v), name)
            
    def _set_int_prop(self,k,v,name=None):
        if v == None:
            self._set_prop(k,None,name)
        else:
            self._set_prop(k, int(v), name)

    def _set_list_prop(self,k,v,name=None):
        self._set_prop(k,v or [],name)

    def _append_list_prop(self,k,v):
        if (not k in self._props) or (self._props[k] is None):
            self._set_list_prop(k,[v])
        elif isinstance(self._props[k], collections.MutableSequence):
            self._props[k].append(v)
        else:
            raise ValueError('attempt to append to a non-list property')

    def _set_obj_prop(self,k,v,name=None):
        self._set_prop(k,v,name)

    def _set_str_prop(self,k,v,name=None):
        if v == None:
            self._set_prop(k,None,name)
        else:
            self._set_prop(k, str(v), name)

    def _get_prop(self,k):
        try:
            return self._props[k]
        except KeyError:
            return None

    def _get_propname(self,k):
        try:
            return self._prop_name_map[k]
        except KeyError:
            return k

    def _unpack_list(self,l):
        r = []
        for item in l:
            if isinstance(item, collections.MutableSequence):
                r.append(self._unpack_list(item))
            elif isinstance(item, CaliperSerializable):
                r.append(item.as_dict())
            else:
                r.append(item)
        return r

    def as_dict(self):
        r = {}
        for k,v in self._props.items():

            # set default name and value for next item
            name = self._get_propname(k)
            value = None
            
            # handle value based on its type: list, composite, or basic type
            if isinstance(v, collections.MutableSequence):
                value = self._unpack_list(v)
            elif isinstance(v, CaliperSerializable):
                value = v.as_dict()
            else:
                value = v
            r.update({name:value})
            
        return copy.deepcopy(r)

    def as_json(self):
        return json.dumps(self.as_dict(),sort_keys=True)

### Entities ###
class MetaEntity(type):
    @property
    def Types(cls):
        return cls._types

@six.add_metaclass(MetaEntity)
class BaseEntity(CaliperSerializable):
    def __init__(self, **kwargs):
        CaliperSerializable.__init__(self)
    pass

### Events ###
class MetaEvent(type):
    @property
    def Types(cls):
        return cls._types

    @property
    def Contexts(cls):
        return cls._contexts

@six.add_metaclass(MetaEvent)
class BaseEvent(CaliperSerializable):
    def __init__(self, **kwargs):
        CaliperSerializable.__init__(self)

### Profiles ###
class MetaProfile(type):
    @property
    def Actions(cls):
        return cls._actions

@six.add_metaclass(MetaProfile)
class BaseProfile(CaliperSerializable):
    def __init__(self, **kwargs):
        CaliperSerializable.__init__(self)

