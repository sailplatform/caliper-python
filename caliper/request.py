# -*- coding: utf-8 -*-
# Caliper-python package, request module
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements.
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

from __future__ import absolute_import


import collections
import datetime
import json
import requests
import uuid

from caliper.base import CaliperSerializable, HttpOptions

class EventStoreEnvelope(CaliperSerializable):
    def __init__(self,
            content_data=None,
            content_type=None,
            envelope_id=None,
            time=None):
        CaliperSerializable.__init__(self)
        self._set_obj_prop('data', content_data)
        self._set_str_prop('id', envelope_id)
        self._set_str_prop('time', time)
        self._set_str_prop('type', content_type)
        
    @property
    def envelope_id(self):
        return self._get_prop('envelope_id')
    @envelope_id.setter
    def envelope_id(self, v):
        self._set_str_prop('id', v)
    
    @property
    def time(self):
        return self._get_prop('time')
    @time.setter
    def time(self, v):
        self._set_str_prop('time', v)

    @property
    def content_data(self):
        return self._get_prop('data')
    @content_data.setter
    def content_data(self, v):
        self._set_obj_prop('data', v)

    @property
    def content_type(self):
        return self._get_prop('type')
    @content_type.setter
    def content_type(self, v):
        self._set_str_prop('type', v)
        

class EventStoreRequestor(object):

    def send(self, caliper_object=None):
        raise NotImplementedError('Instance must implement EventStoreRequester.send()')

    def send_batch(self, caliper_object_list=None):
        raise NotImplementedError('Instance must implement EventStoreRequester.send_batch()')

    def _generate_payload(self,
            caliper_object = None,
            caliper_id = None,
            send_time = None):
        c_id = caliper_id if caliper_id else 'caliper-java_{0}'.format(str(uuid.uuid4()))
        st = send_time if send_time else str(datetime.datetime.now())

        return {'type':'application/json',
                'data':self._get_payload_json(caliper_object, c_id, st)}

    def _get_payload_json(self,
            caliper_object = None,
            caliper_id = None,
            send_time = None):
        envelope = EventStoreEnvelope(
            content_data = caliper_object,
            envelope_id = caliper_id,
            time = send_time,
            content_type = 'caliperEvent')
        
        return envelope.as_json()

class HttpRequestor(EventStoreRequestor):

    def __init__(self,
            options = None,
            **kwargs):
        if not options:
            self._options = HttpOptions()
        elif not( isinstance(options, HttpOptions)):
            raise TypeError('options must implement base.HttpOptions')
        else:
            self._options = options

    def send(self, caliper_object=None):
        return self.send_batch(caliper_object_list=[caliper_object])[0]

    def send_batch(self, caliper_object_list=None):
        results = []

        if isinstance(caliper_object_list, collections.MutableSequence):
            if all( isinstance(item, CaliperSerializable) for item in caliper_object_list):
                s = requests.Session()
                for item in caliper_object_list:
                    payload = self._generate_payload(caliper_object=item)
                    r = s.post(self._options.HOST,
                               data=payload['data'],
                               headers={'Content-Type':payload['type']} )
                    if (r.status_code is requests.codes.ok):
                        results.append(True)
                    else:
                        results.append(False)
                s.close()

        return results
