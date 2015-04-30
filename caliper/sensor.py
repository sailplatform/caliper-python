# -*- coding: utf-8 -*-
# Caliper-python package, sensor module
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
import six
import uuid

from caliper.base import Options, HttpOptions
from caliper.entities import Entity
from caliper.events import Event
from caliper.request import EventStoreRequestor, HttpRequestor
from caliper.util.stats import Statistics

class Client(object):

    def __init__(self,
            config_options = Options(),
            requestor = None,
            stats = None,
            **kwargs):

        if config_options and not( isinstance(config_options, Options)):
            raise TypeError ('config_options must implement base.Options')
        self._config = config_options

        if requestor and not( isinstance(requestor, EventStoreRequestor)):
            raise TypeError('requestor must implement request.EventStoreRequestor')
        else:
            self._requestor = HttpRequestor(options=self._config)

        if stats and not( isinstance(stats, Stats)):
            raise TypeError('stats must implement stats.Stats')
        else:
            self._stats = Statistics()

    @property
    def config(self):
        return self._config

    @property
    def stats(self):
        return self._stats

    @property
    def apiKey(self):
        return self._config['API_KEY']
    @apiKey.setter
    def apiKey(self, new_key):
        self._config['API_KEY']=new_key

    def _process_results(self,results,update_func):
        for r in results:
            if r:
                self._stats.update_successful(1)
            else:
                self._stats.update_failed(1)
            update_func(1)
        
    def describe(self, entity=None, sensor_id=None):
        self.describe_batch(entity_list=[entity], sensor_id=None)
        
    def describe_batch(self, entity_list=None, sensor_id=None):
        if isinstance(entity_list, collections.MutableSequence):
            if all( isinstance(item, Entity) for item in entity_list):
                results = self._requestor.send_batch(caliper_object_list=entity_list, sensor_id=sensor_id)
                self._process_results(results,self.stats.update_describes)
            else:
                raise TypeError('entity_list must be a list of entities.Entity')
        else:
            raise TypeError('entity_list should be a list')

    def send(self, event=None, sensor_id=None):
        self.send_batch(event_list=[event], sensor_id=sensor_id)
        
    def send_batch(self, event_list=None, sensor_id=None): 
        if isinstance(event_list, collections.MutableSequence):
            if all( isinstance(item, Event) for item in event_list):
                results = self._requestor.send_batch(caliper_object_list=event_list, sensor_id=sensor_id)
                self._process_results(results,self.stats.update_measures)
            else:
                raise TypeError('event_list must be a list of entities.Event')
        else:
            raise TypeError('event_list should be a list')
       
                    
class Sensor(object):

    def __init__(self, sensor_id=None):
        self._id = sensor_id
        self._clients = {}

    @staticmethod
    def fashion_default_sensor_with_client(client=None, sensor_id=None):
        if not( isinstance(client, Client)):
            raise TypeError('client must implement Client')
        s = Sensor(sensor_id=sensor_id)
        s.register_client('default',client)
        return s

    @staticmethod
    def fashion_sensor_with_config(config_options=None, sensor_id=None):
        if not( isinstance(config_options, HttpOptions)):
            raise TypeError('config_options must implement HttpOptions')
        s = Sensor(sensor_id=sensor_id)
        s.register_client('default',Client(config_options=config_options))
        return s

    def send(self, event=None):
        for client in self._clients.values():
            client.send(event=event, sensor_id=self.id)

    def send_batch(self, event_list=None):
        for client in self._clients.values():
            client.send_batch(event_list=event_list, sensor_id=self.id)

    @property
    def id(self):
        return self._id

    @property
    def statistics(self):
        return [ client.stats for client in self._clients.values() ]

    @property
    def client_registry(self):
        return self._clients

    def register_client(self, key, client):
        if not( isinstance(client, Client)):
            raise TypeError('client must implement Client')

        if not( isinstance(key, six.string_types)):
            raise ValueError('key must be a string to use as a client registration key')

        self._clients.update({key:client})

    def unregister_client(self,key):
        if key in self._clients:
            del self._clients[key]
