# -*- coding: utf-8 -*-
# Caliper-python package, sensor module
#
# Copyright (c) 2015 IMS Global Learning Consortium, Inc. All Rights Reserved.
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
import six
import uuid

from .base import Options, HttpOptions
from .entities import Entity
from .events import Event
from .request import EventStoreRequestor, HttpRequestor
from .util.stats import Statistics

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
        
    def describe(self, entity=None):
        self.describe_batch([entity])
        
    def describe_batch(self, entity_list=None):
        if isinstance(entity_list, collections.MutableSequence):
            if all( isinstance(item, Entity) for item in entity_list):
                results = self._requestor.send_batch(caliper_object_list=entity_list)
                self._process_results(results,self.stats.update_describes)
            else:
                raise TypeError('entity_list must be a list of entities.Entity')
        else:
            raise TypeError('entity_list should be a list')

    def send(self, event=None):
        self.send_batch([event])
        
    def send_batch(self, event_list=None): 
        if isinstance(event_list, collections.MutableSequence):
            if all( isinstance(item, Event) for item in event_list):
                results = self._requestor.send_batch(caliper_object_list=event_list)
                self._process_results(results,self.stats.update_measures)
            else:
                raise TypeError('event_list must be a list of entities.Event')
        else:
            raise TypeError('event_list should be a list')
       
                    
class Sensor(object):

    def __init__(self):
        self._clients = {}

    @staticmethod
    def fashion_default_sensor_with_config(config_options=None):
        if not( isinstance(config_options, HttpOptions)):
            raise TypeError('config_options must implement HttpOptions')
        s = Sensor()
        s.register_client('default',Client(config_options=config_options))
        return s

    @staticmethod
    def fashion_default_sensor_with_client(client=None):
        if not( isinstance(client, Client)):
            raise TypeError('client must implement Client')
        s = Sensor()
        s.register_client('default',client)
        return s

    def describe(self, entity=None):
        for client in self._clients.values():
            client.describe(entity=entity)

    def describe_batch(self, entity_list=None):
        for client in self._clients.values():
            client.describe_batch(entity_list=entity_list)

    def send(self, event=None):
        for client in self._clients.values():
            client.send(event=event)

    def send_batch(self, event_list=None):
        for client in self._clients.values():
            client.send_batch(event_list=event_list)

    ## Do we really need this now that a Sensor has a list of clients?
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
