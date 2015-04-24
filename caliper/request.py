# -*- coding: utf-8 -*-
# Caliper-python package, request module
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

from __future__ import absolute_import


import collections
import datetime
import json
import requests
import uuid

from caliper.base import CaliperSerializable, HttpOptions

class EventStoreEnvelope(CaliperSerializable):
    def __init__(self,
            data = None,
            envelope_id = None,
            envelope_type = 'http://purl.imsglobal.org/caliper/v1/Envelope',
            send_time = None,
            sensor = None):
        CaliperSerializable.__init__(self)
        self._set_str_prop('@id', envelope_id)
        self._set_str_prop('@type', envelope_type)

        if data and isinstance(data, collections.MutableSequence):
            if all( isinstance(item, CaliperSerializable) for item in data):
                self._set_list_prop('data', data)
            else:
                raise TypeError('data must be a list of caliper entites or events')
        else:
            self._set_list_prop('data', data)

        self._set_str_prop('sendTime', send_time)
        self._set_id_prop('sensor', sensor)
        
    @property
    def data(self):
        return self._get_prop('data')
    @data.setter
    def data(self, new_data):
        if new_data and isinstance(new_data, collections.MutableSequence):
            if all( isinstance(item, CaliperSerializable) for item in new_data):
                self._set_list_prop('data', new_data)
            else:
                raise TypeError('new_data must be a list of caliper entites or events')
        else:
            self._set_list_prop('data', new_data)

    @property
    def envelope_id(self):
        return self._get_prop('@id')
    @envelope_id.setter
    def envelope_id(self, v):
        self._set_str_prop('@id', v)
    
    @property
    def sendTime(self):
        return self._get_prop('sendTime')
    @sendTime.setter
    def sendTime(self, v):
        self._set_str_prop('sendTime', v)

    @property
    def sensor(self):
        return self._get_prop('sensor')


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
            data = caliper_object,

            send_time = send_time)
                
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
