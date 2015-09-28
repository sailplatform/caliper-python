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
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from builtins import *

import collections, copy, datetime, json, requests, uuid

from caliper.base import CaliperSerializable, HttpOptions

class Envelope(CaliperSerializable):

    def __init__(self,
            data = None,
            send_time = None,
            sensor_id = None,
            **kwargs):
        CaliperSerializable.__init__(self)
        self._set_list_prop('data',data,t=CaliperSerializable)
        self._set_str_prop('sendTime', send_time)
        self._set_str_prop('sensor', sensor_id)

    @property
    def data(self):
        return self._get_prop('data')
    @data.setter
    def data(self, new_data):
        self._set_list_prop('data',data,t=CaliperSerializable)        

    @property
    def sendTime(self):
        return self._get_prop('sendTime')
    @sendTime.setter
    def sendTime(self, v):
        self._set_str_prop('sendTime', v)

    @property
    def sensor(self):
        return self._get_prop('sensor')

    # override because Envelopes should only specially serialize
    # their data property's contents
    def as_dict(self,
                described_entities=None,
                thin_context=False,
                thin_props=False):
        return copy.deepcopy({'sendTime': self.sendTime,
                           'sensor': self.sensor,
                           'data': self._unpack_list(self.data,
                                          described_entities=described_entities or [],
                                          thin_context=thin_context,
                                          thin_props=thin_props) })


class EventStoreRequestor(object):

    def describe(self, caliper_entity=None, sensor_id=None):
        raise NotImplementedError('Instance must implement EventStoreRequester.describe()')

    def describe(self, caliper_entity_list=None, sensor_id=None):
        raise NotImplementedError('Instance must implement EventStoreRequester.describe_batch()')
    
    def send(self, caliper_event=None, described_entities=None, sensor_id=None):
        raise NotImplementedError('Instance must implement EventStoreRequester.send()')

    def send_batch(self, caliper_event_list=None, described_entities=None, sensor_id=None):
        raise NotImplementedError('Instance must implement EventStoreRequester.send_batch()')

    def _get_time(self):
        return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'        

    def _generate_payload(self,
            caliper_objects = None,
            described_entities = None,
            optimize = False,
            send_time = None,
            sensor_id = None):
        st = send_time if send_time else self._get_time()
        payload,ids = self._get_payload_json(caliper_objects,
                                             described_entities,
                                             optimize,
                                             st,
                                             sensor_id)
        return {'type':'application/json', 'data': payload}, ids

    def _get_payload_json(self,
            caliper_objects = None,
            described_entities = None,
            optimize = False,
            send_time = None,
            sensor_id = None):
        envelope = Envelope(
            data = caliper_objects,
            send_time = send_time,
            sensor_id = sensor_id)
                
        return envelope.as_json_with_ids(described_entities=described_entities,
                                         thin_context=optimize,
                                         thin_props=optimize)

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

    def _dispatch(self, caliper_objects=None, described_entities=None, sensor_id=None):
        results = []
        identifiers = []

        if isinstance(caliper_objects, collections.MutableSequence):
            s = requests.Session()
            payload,ids = self._generate_payload(caliper_objects=caliper_objects,
                                                 described_entities=described_entities,
                                                 optimize=self._options.OPTIMIZE_SERIALIZATION,
                                                 sensor_id=sensor_id)
            r = s.post(self._options.HOST,
                       data=payload['data'],
                       headers={'Authorization': self._options.API_KEY,
                                'Content-Type': payload['type']} )
            if (r.status_code is requests.codes.ok):
                v = True
                identifiers += ids
            else:
                v = False
            results += len(caliper_objects) * [v]
            s.close()

        return results,identifiers

    def describe(self, caliper_entity=None, sensor_id=None):
        results, ids = self.describe_batch(caliper_entity_list=[caliper_entity],sensor_id=sensor_id)
        return results[0], ids

    def describe_batch(self, caliper_entity_list=None, sensor_id=None):
        results, ids = self._dispatch(caliper_objects=caliper_entity_list, sensor_id=sensor_id)
        return results, ids

    def send(self, caliper_event=None, described_entities=None, sensor_id=None):
        results, ids = self.send_batch(caliper_event_list=[caliper_event],
                                       described_entities=described_entities,
                                       sensor_id=sensor_id)
        return results[0], ids

    def send_batch(self, caliper_event_list=None, described_entities=None, sensor_id=None):
        results, ids = self._dispatch(caliper_objects=caliper_event_list,
                                      described_entities=described_entities,
                                      sensor_id=sensor_id)
        return results, ids
