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
from future.utils import raise_with_traceback
from builtins import str

try:
    from collections.abc import MutableSequence
except ImportError:
    from collections import MutableSequence

from caliper.base import CaliperSerializable, Options, HttpOptions, deprecation, ensure_list_type
from caliper.entities import Entity
from caliper.events import Event
from caliper.request import EventStoreRequestor, HttpRequestor
from caliper.util.stats import Statistics, SimpleStatistics


class Client(object):
    def __init__(self, config_options=None, requestor=None, stats=None, **kwargs):

        self._debug = []

        if config_options is None:
            config_options = Options()

        if config_options and not (isinstance(config_options, Options)):
            raise_with_traceback(TypeError('config_options must implement base.Options'))
        self._config = config_options

        if requestor and not (isinstance(requestor, EventStoreRequestor)):
            raise_with_traceback(TypeError('requestor must implement request.EventStoreRequestor'))
        else:
            self._requestor = HttpRequestor(options=self._config)

        if stats and not (isinstance(stats, Statistics)):
            raise_with_traceback(TypeError('stats must implement stats.Stats'))
        else:
            self._stats = Statistics()

    def _reset(self):
        self._stats = Statistics()
        self._debug = []

    @property
    def config(self):
        return self._config

    @property
    def debug(self):
        return self._debug

    @property
    def stats(self):
        return self._stats

    @property
    def apiKey(self):
        return self._config.API_KEY

    @apiKey.setter
    def apiKey(self, new_key):
        self._config.API_KEY = new_key

    def _process_results(self, results, update_func):
        for r in results:
            if r:
                self._stats.update_successful(1)
            else:
                self._stats.update_failed(1)
            update_func(1)

    def describe(self, entities=None, sensor_id=None):
        identifiers = None
        if ensure_list_type(entities, Entity):
            results, identifiers, debug = self._requestor.describe(caliper_entity_list=entities,
                                                                   sensor_id=sensor_id,
                                                                   debug=self._config.DEBUG)
            self._process_results(results, self.stats.update_describes)
        if self._config.DEBUG:
            self.debug.append(debug)
        return identifiers

    def get_config(self):
        return self._requestor.get_config()

    def send(self, events=None, described_objects=None, sensor_id=None):
        identifiers = None
        if ensure_list_type(events, Event):
            results, identifiers, debug = self._requestor.send(caliper_event_list=events,
                                                               described_objects=described_objects,
                                                               sensor_id=sensor_id,
                                                               debug=self._config.DEBUG)
            self._process_results(results, self.stats.update_measures)
        if self._config.DEBUG:
            self.debug.append(debug)
        return identifiers


class SimpleSensor(object):
    def __init__(self, config_options=None, sensor_id=None):
        if not config_options:
            self._config = HttpOptions(optimize_serialization=True)
        elif not (isinstance(config_options, HttpOptions)):
            raise_with_traceback(TypeError('config_options must implement HttpOptions'))
        else:
            self._config = config_options
        self._id = sensor_id
        self._requestor = HttpRequestor(options=self._config)
        self._stats = SimpleStatistics()
        self._status_code = None
        self._debug = []

    @staticmethod
    def fashion_simple_sensor(config_options=None, sensor_id=None):
        s = SimpleSensor(config_options=config_options, sensor_id=sensor_id)
        return s

    def _reset(self):
        self._stats = SimpleStatistics()
        self._status_code = None
        self._debug = []

    def _dispatch(self, caliper_objects, sensor_id, described_objects):
        identifiers = []
        if ensure_list_type(caliper_objects, CaliperSerializable):
            results, identifiers, debug = self._requestor.send(caliper_event_list=caliper_objects,
                                                               described_objects=described_objects,
                                                               sensor_id=sensor_id,
                                                               debug=True)
            self._process_results(results, self._stats.update_sent)
            self._status_code = debug.status_code
            if self._config.DEBUG:
                self._debug.append(debug)
        return identifiers

    def _process_results(self, results, update_func):
        for r in results:
            if r:
                self._stats.update_successful(1)
            else:
                self._stats.update_failed(1)
            update_func(1)

    def get_config(self):
        return self._requestor.get_config()

    def send(self, caliper_objects, described_objects=None):
        v = caliper_objects
        if not isinstance(v, MutableSequence):
            v = [v]
        identifiers = self._dispatch(v, self.id, described_objects)
        return identifiers

    @property
    def apiKey(self):
        return self._config.API_KEY

    @apiKey.setter
    def apiKey(self, new_key):
        self._config.API_KEY = new_key

    @property
    def config(self):
        return self._config

    @property
    def debug(self):
        return self._debug

    @property
    def id(self):
        return self._id

    @property
    def statistics(self):
        return [self._stats]

    @property
    def status_code(self):
        return self._status_code


class Sensor(object):
    def __init__(self, sensor_id=None):
        self._id = sensor_id
        self._clients = {}

    @staticmethod
    def fashion_default_sensor_with_client(client=None, sensor_id=None):
        if not (isinstance(client, Client)):
            raise_with_traceback(TypeError('client must implement Client'))
        s = Sensor(sensor_id=sensor_id)
        s.register_client('default', client)
        return s

    @staticmethod
    def fashion_sensor_with_config(config_options=None, sensor_id=None):
        if not (isinstance(config_options, HttpOptions)):
            raise_with_traceback(TypeError('config_options must implement HttpOptions'))
        s = Sensor(sensor_id=sensor_id)
        s.register_client('default', Client(config_options=config_options))
        return s

    def describe(self, entities=None, entity=None):
        identifiers = {}
        v = entities
        if entity and not entities:
            deprecation('Sensor.describe(e) deprecated; use Sensor.describe(entities=e).')
            v = entity
        if not isinstance(v, MutableSequence):
            v = [v]
        for k, client in self.client_registry.items():
            identifiers.update({k: client.describe(entities=v, sensor_id=self.id)})
        return identifiers

    def get_config(self):
        cfgs = {}
        for k, client in self.client_registry.items():
            cfgs.update({k: client.get_config()})
        return cfgs

    def send(self, events=None, event=None, described_objects=None):
        identifiers = {}
        v = events
        if event and not events:
            deprecation('Sensor.send(event=e) deprecated; use Sensor.send(events=e).')
            v = event
        if not isinstance(v, MutableSequence):
            v = [v]
        for k, client in self.client_registry.items():
            identifiers.update(
                {k: client.send(events=v, described_objects=described_objects, sensor_id=self.id)})
        return identifiers

    def describe_batch(self, entity_list=None):
        deprecation(
            'Sensor.describe_batch(entity_list=e) deprecated; use Sensor.describe(entities=e).')
        self.describe(entities=entity_list)

    def send_batch(self, event_list=None, described_objects=None):
        deprecation('Sensor.send_batch(event_list=e) deprecated; use Sensor.send(events=e).')
        self.send(events=event_list, described_objects=described_objects)

    @property
    def id(self):
        return self._id

    @property
    def statistics(self):
        return [client.stats for client in self._clients.values()]

    @property
    def client_registry(self):
        return self._clients

    def register_client(self, key, client):
        if not (isinstance(client, Client)):
            raise_with_traceback(TypeError('client must implement Client'))

        if not (isinstance(key, str)):
            raise_with_traceback(
                ValueError('key must be a string to use as a client registration key'))

        self._clients.update({key: client})

    def unregister_client(self, key):
        if key in self._clients:
            del self._clients[key]
