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
from caliper.base import BaseEntity, BaseEvent, ensure_type
from caliper import entities, profiles
from caliper.extern import foaf, schemadotorg

## Base event class
class Event(BaseEvent):

    def __init__(self,
            action = None,
            actor = None,
            duration = None,
            edApp = None,
            endedAtTime = None,
            event_object = None,
            federatedSession = None,
            generated = None,
            group = None,
            membership = None,
            startedAtTime = None,
            target = None):
        BaseEvent.__init__(self)
        self._set_base_context(EVENT_CONTEXTS['EVENT'])
        self._set_str_prop('@type', EVENT_TYPES['EVENT'])

        if action and (action not in profiles.CaliperProfile.Actions.values()):
            raise ValueError('action must be in the list of CaliperProfile actions')
        else:
            self._set_str_prop('action', action, req=True)
        self._set_obj_prop('actor', actor, entities.Agent, req=True)

        self._set_str_prop('duration', duration)
        self._set_obj_prop('edApp', edApp, ENTITY_TYPES['SOFTWARE_APPLICATION'])                    
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_obj_prop('object', event_object, BaseEntity)
        self._set_id_prop('federatedSession', federatedSession, ENTITY_TYPES['SESSION'])
        self._set_obj_prop('generated', generated, entities.Generatable)
        self._set_obj_prop('group', group, ENTITY_TYPES['ORGANIZATION'])
        self._set_obj_prop('membership', membership, ENTITY_TYPES['MEMBERSHIP'])
        self._set_str_prop('startedAtTime', startedAtTime, req=True)
        self._set_obj_prop('target', target, entities.Targetable)            

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
    def duration(self):
        return self._get_prop('duration')

    @property
    def edApp(self):
        return self._get_prop('edApp')

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')

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
    def startedAtTime(self):
        return self._get_prop('startedAtTime')

    @property
    def target(self):
        return self._get_prop('target')


## Derived Events
class AnnotationEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in profiles.AnnotationProfile.Actions.values():
            raise ValueError('action must be in the list of AnnotationProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.generated, ENTITY_TYPES['ANNOTATION'])

        self._set_base_context(EVENT_CONTEXTS['ANNOTATION'])
        self._set_str_prop('@type', EVENT_TYPES['ANNOTATION'])


class AssessmentEvent(Event):
    
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in profiles.AssessmentProfile.Actions.values():
            raise ValueError('action must be in the list of AssessmentProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSESSMENT'])
        ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'])

        self._set_base_context(EVENT_CONTEXTS['ASSESSMENT'])
        self._set_str_prop('@type', EVENT_TYPES['ASSESSMENT'])


class AssessmentItemEvent(Event):
    
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in profiles.AssessmentItemProfile.Actions.values():
            raise ValueError('action must be in the list of AssessmentItemProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSESSMENT_ITEM'])
        ensure_type(self.generated, entities.Generatable)

        self._set_base_context(EVENT_CONTEXTS['ASSESSMENT_ITEM'])
        self._set_str_prop('@type', EVENT_TYPES['ASSESSMENT_ITEM'])


class AssignableEvent(Event):
    
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in profiles.AssignableProfile.Actions.values():
            raise TypeError('action must be in the list of AssignableProfile actions')
        ensure_type(self.object, entities.Assignable)
        ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'])

        self._set_base_context(EVENT_CONTEXTS['ASSIGNABLE'])
        self._set_str_prop('@type', EVENT_TYPES['ASSIGNABLE'])


class MediaEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in profiles.MediaProfile.Actions.values():
            raise TypeError('action must be in the list of MediaProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['MEDIA_OBJECT'])
        ensure_type(self.target, ENTITY_TYPES['MEDIA_LOCATION'])

        self._set_base_context(EVENT_CONTEXTS['MEDIA'])
        self._set_str_prop('@type', EVENT_TYPES['MEDIA'])


class NavigationEvent(Event):

    def __init__(self, navigatedFrom=None, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action != profiles.CaliperProfile.Actions['NAVIGATED_TO']:
            raise ValueError('action must be ' + profiles.CaliperProfile.Actions['NAVIGATED_TO']
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.target, ENTITY_TYPES['DIGITAL_RESOURCE'])

        self._set_base_context(EVENT_CONTEXTS['NAVIGATION'])
        self._set_str_prop('@type', EVENT_TYPES['NAVIGATION'])
        self._set_obj_prop('navigatedFrom', navigatedFrom, ENTITY_TYPES['DIGITAL_RESOURCE'])

    @property
    def navigatedFrom(self):
        return self._get_prop('navigatedFrom')


class OutcomeEvent(Event):

    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in profiles.OutcomeProfile.Actions.values():
            raise TypeError('action must be in the list of OutcomeProfile actions')
        ensure_type(self.object, ENTITY_TYPES['ATTEMPT'])
        ensure_type(self.generated, ENTITY_TYPES['RESULT'])
                
        self._set_base_context(EVENT_CONTEXTS['OUTCOME'])
        self._set_str_prop('@type', EVENT_TYPES['OUTCOME'])


class ReadingEvent(Event):

    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in profiles.ReadingProfile.Actions.values():
            raise TypeError('action must be in the list of ReadingProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.target, ENTITY_TYPES['FRAME'])

        self._set_base_context(EVENT_CONTEXTS['READING'])
        self._set_str_prop('@type', EVENT_TYPES['READING'])


class SessionEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        end_time_req=False
        if self.action == profiles.SessionProfile.Actions['LOGGED_IN']:
            ensure_type(self.actor, ENTITY_TYPES['PERSON'])
            ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.generated, ENTITY_TYPES['SESSION'])
            ensure_type(self.target, ENTITY_TYPES['DIGITAL_RESOURCE'])
        elif self.action == profiles.SessionProfile.Actions['LOGGED_OUT']:
            ensure_type(self.actor, ENTITY_TYPES['PERSON'])
            ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.target, ENTITY_TYPES['SESSION'])
            end_time_req = True
        elif self.action == profiles.SessionProfile.Actions['TIMED_OUT']:
            ensure_type(self.actor, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.object, ENTITY_TYPES['SESSION'])
            end_time_req = True
        else:
            raise ValueError('action must be in the list of SessionProfile actions')
        if end_time_req and not self.endedAtTime:
            raise ValueError('endedAtTime is required')

        self._set_base_context(EVENT_CONTEXTS['SESSION'])
        self._set_str_prop('@type', EVENT_TYPES['SESSION'])


class ViewEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in profiles.ReadingProfile.Actions.values():
            raise TypeError('action must be in the list of ReadingProfile actions')
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])

        self._set_base_context(EVENT_CONTEXTS['VIEW'])
        self._set_str_prop('@type', EVENT_TYPES['VIEW'])


            
