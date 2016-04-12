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
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from builtins import *


import collections
import uuid

from caliper.base import Options, HttpOptions, deprecation, ensure_list_type
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
        return self._config.API_KEY
    @apiKey.setter
    def apiKey(self, new_key):
        self._config.API_KEY=new_key

    def _process_results(self,results,update_func):
        for r in results:
            if r:
                self._stats.update_successful(1)
            else:
                self._stats.update_failed(1)
            update_func(1)

    def describe(self, entities=None, sensor_id=None):
        identifiers = None
        if ensure_list_type(entities, Entity):
            results, identifiers = self._requestor.describe(caliper_entity_list=entities,
                                                            sensor_id=sensor_id)
            self._process_results(results, self.stats.update_describes)
        return identifiers
        
    def send(self, events=None, described_entities=None, sensor_id=None):
        identifiers = None
        if ensure_list_type(events, Event):
            results, identifiers = self._requestor.send(caliper_event_list=events,
                                                        described_entities=described_entities,
                                                        sensor_id=sensor_id)
            self._process_results(results, self.stats.update_measures)
        return identifiers

                    
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

    def describe(self, entities=None, entity=None):
        identifiers={}
        v = entities
        if entity and not entities:
            deprecation('Sensor.describe(e) deprecated; use Sensor.describe(entities=e).')
            v = entity
        if not isinstance(v, collections.MutableSequence):
            v = [v]
        for k, client in self.client_registry.items():
            identifiers.update( {k: client.describe(entities=v,
                                                    sensor_id=self.id)} )
        return identifiers

    def send(self, events=None, event=None, described_entities=None):
        identifiers = {}
        v = events
        if event and not events:
            deprecation('Sensor.send(event=e) deprecated; use Sensor.send(events=e).')
            v = event
        if not isinstance(v, collections.MutableSequence):
            v = [v]
        for k, client in self.client_registry.items():
            identifiers.update( {k: client.send(events=v,
                                                described_entities=described_entities,
                                                sensor_id=self.id)} )
        return identifiers

    def describe_batch(self, entity_list=None):
        deprecation('Sensor.describe_batch(entity_list=e) deprecated; use Sensor.describe(entities=e).')
        self.describe(entities=entity_list)

    def send_batch(self, event_list=None, described_entities=None):
        deprecation('Sensor.send_batch(event_list=e) deprecated; use Sensor.send(events=e).')
        self.send(events=event_list, described_entities=described_entities)

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

        if not( isinstance(key, str)):
            raise ValueError('key must be a string to use as a client registration key')

        self._clients.update({key:client})

    def unregister_client(self,key):
        if key in self._clients:
            del self._clients[key]
