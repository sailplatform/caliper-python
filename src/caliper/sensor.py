# -*- coding: utf-8 -*-
# Caliper-python package, sensor module
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

from .base import HttpDefaults, Options
from .entities import Entity
from .events import Event
from .request import EventStoreRequestor, HttpRequestor
from .util.stats import Stats

class Client(object):

    def __init__(self,
            config_options=HttpDefaults(),
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
            self._stats = stats

        self._stats = stats
            

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

    def describe(self, entity=None):
        if entity and not( isinstance(entity, Entiity)):
            raise TypeError('entity must implement entities.Entity')
        else:
            requestor.send(entity)

    def send(self, event=None):
        if event and not( isinstance(event, Event)):
            raise TypeError('event must implement events.Event')
        else:
            requestor.send(event)

