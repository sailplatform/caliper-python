# -*- coding: utf-8 -*-
# Caliper-python package, events module
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

from caliper.constants import EVENT_TYPES, EVENT_CONTEXTS
from caliper.constants import ENTITY_TYPES
from caliper.constants import CALIPER_ACTIONS
from caliper.constants import (
    BASE_PROFILE_ACTIONS,
    ANNOTATION_PROFILE_ACTIONS,
    ASSESSMENT_PROFILE_ACTIONS,
    ASSESSMENT_ITEM_PROFILE_ACTIONS,
    ASSIGNABLE_PROFILE_ACTIONS,
    MEDIA_PROFILE_ACTIONS,
    OUTCOME_PROFILE_ACTIONS,
    READING_PROFILE_ACTIONS,
    SESSION_PROFILE_ACTIONS
    )
from caliper.base import BaseEntity, BaseEvent, ensure_type
from caliper import entities
from caliper.extern import foaf, schemadotorg

## Base event class
class Event(BaseEvent):

    def __init__(self,
            action = None,
            actor = None,
            edApp = None,
            event_object = None,
            eventTime = None,
            federatedSession = None,
            generated = None,
            group = None,
            membership = None,
            target = None):
        BaseEvent.__init__(self)
        self._set_base_context(EVENT_CONTEXTS['EVENT'])
        self._set_str_prop('@type', EVENT_TYPES['EVENT'])

        if action and (action not in CALIPER_ACTIONS.values()):
            raise ValueError('action must be in the list of Caliper actions')
        else:
            self._set_str_prop('action', action, req=True)
        self._set_obj_prop('actor', actor, t=entities.Agent, req=True)

        self._set_obj_prop('edApp', edApp, t=ENTITY_TYPES['SOFTWARE_APPLICATION'])                    
        self._set_date_prop('eventTime', eventTime, req=True)
        self._set_obj_prop('object', event_object, t=BaseEntity)
        self._set_id_prop('federatedSession', federatedSession, t=ENTITY_TYPES['SESSION'])
        self._set_obj_prop('generated', generated, t=entities.Generatable)
        self._set_obj_prop('group', group, t=ENTITY_TYPES['ORGANIZATION'])
        self._set_obj_prop('membership', membership, t=ENTITY_TYPES['MEMBERSHIP'])
        self._set_obj_prop('target', target, t=entities.Targetable)

    def as_minimal_event(self):
        return MinimalEvent(action=self.action,
                            actor=self.actor,
                            event_object=self.object,
                            eventTime=self.eventTime)

    @property
    def context(self):
        return self._unpack_context()

    @property
    def type(self):
        return self._get_prop('@type')

    @property
    def action(self):
        return self._get_prop('action')

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def edApp(self):
        return self._get_prop('edApp')

    @property
    def eventTime(self):
        return self._get_prop('eventTime')

    @property
    def federatedSession(self):
        return self._get_prop('federatedSession')

    @property
    def generated(self):
        return self._get_prop('generated')

    @property
    def group(self):
        return self._get_prop('group')
    
    @property
    def object(self):
        return self._get_prop('object')

    @property
    def target(self):
        return self._get_prop('target')


class MinimalEvent(BaseEvent):
    def __init__(self,
                 action=None,
                 actor=None,
                 event_object=None,
                 eventTime=None):
        BaseEvent.__init__(self)
        self._set_base_context(EVENT_CONTEXTS['EVENT'])
        self._set_str_prop('@type', EVENT_TYPES['EVENT'])
        self._set_str_prop('action', action, req=True)

        if action and (action not in CALIPER_ACTIONS.values()):
            raise ValueError('action must be in the list of Caliper actions')
        else:
            self._set_str_prop('action', action, req=True)

        if not isinstance(actor, entities.Agent):
            raise ValueError('actor must implement entities.Agent')
        else:
            d = actor.as_dict()            
            self._set_obj_prop('actor', { '@id': d.get('@id'), '@type': d.get('@type') } )

        self._set_date_prop('eventTime', eventTime, req=True)

        if event_object and not isinstance(event_object, BaseEntity):
            raise ValueError('event_object must implement BaseEntity')
        else:
            d = event_object.as_dict()
            self._set_obj_prop('object', { '@id': d.get('@id'), '@type': d.get('@type') } )

    @property
    def action(self):
        return self._get_prop('action')

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def eventTime(self):
        return self._get_prop('eventTime')

    @property
    def object(self):
        return self._get_prop('object')


## Derived Events
class AnnotationEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in ANNOTATION_PROFILE_ACTIONS.values():
            raise ValueError('action must be in the list of Annotation profile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.generated, ENTITY_TYPES['ANNOTATION'])

        self._set_base_context(EVENT_CONTEXTS['ANNOTATION'])
        self._set_str_prop('@type', EVENT_TYPES['ANNOTATION'])


class AssessmentEvent(Event):
    
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in ASSESSMENT_PROFILE_ACTIONS.values():        
            raise ValueError('action must be in the list of Assessment profile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSESSMENT'])
        ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'])

        self._set_base_context(EVENT_CONTEXTS['ASSESSMENT'])
        self._set_str_prop('@type', EVENT_TYPES['ASSESSMENT'])


class AssessmentItemEvent(Event):
    
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in ASSESSMENT_ITEM_PROFILE_ACTIONS.values():
            raise ValueError('action must be in the list of Assessment Item profile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSESSMENT_ITEM'])
        if self.action == ASSESSMENT_ITEM_PROFILE_ACTIONS['COMPLETED']:
            ensure_type(self.generated, ENTITY_TYPES['RESPONSE'])            
        else:
            ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'])

        self._set_base_context(EVENT_CONTEXTS['ASSESSMENT_ITEM'])
        self._set_str_prop('@type', EVENT_TYPES['ASSESSMENT_ITEM'])


class AssignableEvent(Event):
    
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in ASSIGNABLE_PROFILE_ACTIONS.values():
            raise TypeError('action must be in the list of Assignable profile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSIGNABLE_DIGITAL_RESOURCE'])
        ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'])

        self._set_base_context(EVENT_CONTEXTS['ASSIGNABLE'])
        self._set_str_prop('@type', EVENT_TYPES['ASSIGNABLE'])


class MediaEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in MEDIA_PROFILE_ACTIONS.values():
            raise TypeError('action must be in the list of Media profile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['MEDIA_OBJECT'])
        ensure_type(self.target, ENTITY_TYPES['MEDIA_LOCATION'])

        self._set_base_context(EVENT_CONTEXTS['MEDIA'])
        self._set_str_prop('@type', EVENT_TYPES['MEDIA'])


class NavigationEvent(Event):

    def __init__(self, navigatedFrom=None, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action != BASE_PROFILE_ACTIONS['NAVIGATED_TO']:
            raise ValueError('action must be ' + BASE_PROFILE_ACTIONS['NAVIGATED_TO'])
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.target, ENTITY_TYPES['DIGITAL_RESOURCE'])

        self._set_base_context(EVENT_CONTEXTS['NAVIGATION'])
        self._set_str_prop('@type', EVENT_TYPES['NAVIGATION'])
        self._set_obj_prop('navigatedFrom', navigatedFrom, t=ENTITY_TYPES['DIGITAL_RESOURCE'])

    @property
    def navigatedFrom(self):
        return self._get_prop('navigatedFrom')


class OutcomeEvent(Event):

    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in OUTCOME_PROFILE_ACTIONS.values():
            raise TypeError('action must be in the list of Outcome profile actions')
        ensure_type(self.object, ENTITY_TYPES['ATTEMPT'])
        ensure_type(self.generated, ENTITY_TYPES['RESULT'])
                
        self._set_base_context(EVENT_CONTEXTS['OUTCOME'])
        self._set_str_prop('@type', EVENT_TYPES['OUTCOME'])


class ReadingEvent(Event):

    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in READING_PROFILE_ACTIONS.values():
            raise TypeError('action must be in the list of Reading profile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.target, ENTITY_TYPES['FRAME'])

        self._set_base_context(EVENT_CONTEXTS['READING'])
        self._set_str_prop('@type', EVENT_TYPES['READING'])


class SessionEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action == SESSION_PROFILE_ACTIONS['LOGGED_IN']:        
            ensure_type(self.actor, ENTITY_TYPES['PERSON'])
            ensure_type(self.edApp, ENTITY_TYPES['SOFTWARE_APPLICATION'], optional=True)
            ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.generated, ENTITY_TYPES['SESSION'], optional=True)
            ensure_type(self.target, ENTITY_TYPES['DIGITAL_RESOURCE'], optional=True)
        elif self.action == SESSION_PROFILE_ACTIONS['LOGGED_OUT']:        
            ensure_type(self.actor, ENTITY_TYPES['PERSON'])
            ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.target, ENTITY_TYPES['SESSION'], optional=True)
        elif self.action == SESSION_PROFILE_ACTIONS['TIMED_OUT']:
            ensure_type(self.actor, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.object, ENTITY_TYPES['SESSION'])
        else:
            raise ValueError('action must be in the list of Session profile actions')

        self._set_base_context(EVENT_CONTEXTS['SESSION'])
        self._set_str_prop('@type', EVENT_TYPES['SESSION'])


class ViewEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in READING_PROFILE_ACTIONS.values():        
            raise TypeError('action must be in the list of ReadingProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])

        self._set_base_context(EVENT_CONTEXTS['VIEW'])
        self._set_str_prop('@type', EVENT_TYPES['VIEW'])


            
