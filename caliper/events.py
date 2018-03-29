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
from future.utils import raise_with_traceback
from builtins import *

import collections, uuid

from caliper.constants import EVENT_TYPES, MARKER_TYPES
from caliper.constants import ENTITY_TYPES
from caliper.constants import CALIPER_ACTIONS
from caliper.constants import (
    BASIC_EVENT_ACTIONS, ANNOTATION_EVENT_ACTIONS, ASSESSMENT_EVENT_ACTIONS,
    ASSESSMENT_ITEM_EVENT_ACTIONS, ASSIGNABLE_EVENT_ACTIONS, FORUM_EVENT_ACTIONS,
    GRADE_EVENT_ACTIONS, MEDIA_EVENT_ACTIONS, MESSAGE_EVENT_ACTIONS, NAVIGATION_EVENT_ACTIONS,
    SESSION_EVENT_ACTIONS, THREAD_EVENT_ACTIONS, TOOL_USE_EVENT_ACTIONS, VIEW_EVENT_ACTIONS)
from caliper.base import BaseEntity, BaseEvent, ensure_type

## Base event class
class Event(BaseEvent):
    def __init__(self,
                 id=None,
                 context=None,
                 profile=None,
                 action=None,
                 actor=None,
                 edApp=None,
                 object=None,
                 eventTime=None,
                 extensions=None,
                 federatedSession=None,
                 generated=None,
                 group=None,
                 membership=None,
                 referrer=None,
                 session=None,
                 sourcedId=None,
                 target=None):
        BaseEvent.__init__(self, context=context, profile=profile)
        self._set_id(id or 'urn:uuid:{}'.format(uuid.uuid4()))
        if action and (action not in CALIPER_ACTIONS.values()):
            raise_with_traceback(ValueError('action must be in the list of Caliper actions'))
        else:
            self._set_str_prop('action', action, req=True)
        self._set_obj_prop('actor', actor, t=ENTITY_TYPES['AGENT'], req=True)
        self._set_obj_prop('edApp', edApp, t=ENTITY_TYPES['SOFTWARE_APPLICATION'])
        self._set_date_prop('eventTime', eventTime, req=True)
        self._set_obj_prop('extensions', extensions)
        self._set_obj_prop('object', object, t=BaseEntity)
        self._set_obj_prop('federatedSession', federatedSession, t=ENTITY_TYPES['LTI_SESSION'])
        self._set_obj_prop('generated', generated, t=MARKER_TYPES['GENERATABLE'])
        self._set_obj_prop('group', group, t=ENTITY_TYPES['ORGANIZATION'])
        self._set_obj_prop('membership', membership, t=ENTITY_TYPES['MEMBERSHIP'])
        self._set_obj_prop('referrer', referrer, t=MARKER_TYPES['REFERRABLE'])
        self._set_obj_prop('session', session, t=ENTITY_TYPES['SESSION'])
        self._set_obj_prop('target', target, t=MARKER_TYPES['TARGETABLE'])

    def as_minimal_event(self):
        return MinimalEvent(
            id=self.id,
            action=self.action,
            actor=self.actor,
            object=self.object,
            eventTime=self.eventTime)

    @property
    def id(self):
        return self._get_prop('id')

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
    def extensions(self):
        return self._get_prop('extensions')

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
    def referrer(self):
        return self._get_prop('referrer')

    @property
    def session(self):
        return self._get_prop('session')

    @property
    def target(self):
        return self._get_prop('target')


class MinimalEvent(BaseEvent):
    def __init__(self, id=None, action=None, actor=None, object=None, eventTime=None):
        BaseEvent.__init__(self)
        self._set_id(id or 'urn:uuid:{}'.format(uuid.uuid4()))
        self._set_str_prop('action', action, req=True)
        self._set_obj_prop('actor', actor, t=ENTITY_TYPES['AGENT'], req=True)
        self._set_date_prop('eventTime', eventTime, req=True)
        self._set_obj_prop('object', object, t=ENTITY_TYPES['ENTITY'])

        if action and (action not in BASIC_EVENT_ACTIONS.values()):
            raise_with_traceback(ValueError('action must be in the list of Caliper actions'))
        else:
            self._set_str_prop('action', action, req=True)

    @property
    def id(self):
        return self._get_prop('id')

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
        if self.action not in ANNOTATION_EVENT_ACTIONS.values():
            raise_with_traceback(
                ValueError('action must be in the list of Annotation event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.generated, ENTITY_TYPES['ANNOTATION'])


class AssessmentEvent(Event):
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in ASSESSMENT_EVENT_ACTIONS.values():
            raise_with_traceback(
                ValueError('action must be in the list of Assessment Item event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSESSMENT'])
        ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'], optional=True)


class AssessmentItemEvent(Event):
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action not in ASSESSMENT_ITEM_EVENT_ACTIONS.values():
            raise_with_traceback(
                ValueError('action must be in the list of Assessment event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSESSMENT_ITEM'])
        if self.action == ASSESSMENT_ITEM_EVENT_ACTIONS['COMPLETED']:
            ensure_type(self.generated, ENTITY_TYPES['RESPONSE'], optional=True)
        else:
            ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'], optional=True)


class AssignableEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in ASSIGNABLE_EVENT_ACTIONS.values():
            raise_with_traceback(
                ValueError('action must be in the list of Assignable event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['ASSIGNABLE_DIGITAL_RESOURCE'])
        ensure_type(self.generated, ENTITY_TYPES['ATTEMPT'], optional=True)


class ForumEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in FORUM_EVENT_ACTIONS.values():
            raise_with_traceback(ValueError('action must be in the list of Forum event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['FORUM'])


class GradeEvent(Event):
    def __init__(self, target=None, **kwargs):
        Event.__init__(self, target=None, **kwargs)
        if self.action == GRADE_EVENT_ACTIONS['GRADED']:
            ensure_type(self.object, ENTITY_TYPES['ATTEMPT'])
            ensure_type(self.generated, ENTITY_TYPES['SCORE'])
        else:
            raise_with_traceback(ValueError('action must be in the list of Outcome event actions'))


class MediaEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in MEDIA_EVENT_ACTIONS.values():
            raise_with_traceback(ValueError('action must be in the list of Media event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['MEDIA_OBJECT'])
        ensure_type(self.target, ENTITY_TYPES['MEDIA_LOCATION'], optional=True)


class MessageEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in MESSAGE_EVENT_ACTIONS.values():
            raise_with_traceback(ValueError('action must be in the list of Message event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['MESSAGE'])


class NavigationEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in NAVIGATION_EVENT_ACTIONS.values():
            raise_with_traceback(
                ValueError('action must be in the list of Navigation event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
        ensure_type(self.target, ENTITY_TYPES['DIGITAL_RESOURCE'], optional=True)


class SessionEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action == SESSION_EVENT_ACTIONS['LOGGED_IN']:
            ensure_type(self.actor, ENTITY_TYPES['PERSON'])
            ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.generated, ENTITY_TYPES['SESSION'], optional=True)
            ensure_type(self.target, ENTITY_TYPES['DIGITAL_RESOURCE'], optional=True)
        elif self.action == SESSION_EVENT_ACTIONS['LOGGED_OUT']:
            ensure_type(self.actor, ENTITY_TYPES['PERSON'])
            ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.target, ENTITY_TYPES['SESSION'], optional=True)
        elif self.action == SESSION_EVENT_ACTIONS['TIMED_OUT']:
            ensure_type(self.actor, ENTITY_TYPES['SOFTWARE_APPLICATION'])
            ensure_type(self.object, ENTITY_TYPES['SESSION'])
        else:
            raise_with_traceback(ValueError('action must be in the list of Session event actions'))


class ThreadEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in THREAD_EVENT_ACTIONS.values():
            raise_with_traceback(ValueError('action must be in the list of Thread event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['THREAD'])


class ToolUseEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in TOOL_USE_EVENT_ACTIONS.values():
            raise_with_traceback(ValueError('action must be in the list of Tool Use event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['SOFTWARE_APPLICATION'])
        ensure_type(self.target, ENTITY_TYPES['SOFTWARE_APPLICATION'], optional=True)


class ViewEvent(Event):
    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        if self.action not in VIEW_EVENT_ACTIONS.values():
            raise_with_traceback(ValueError('action must be in the list of View event actions'))
        ensure_type(self.actor, ENTITY_TYPES['PERSON'])
        ensure_type(self.object, ENTITY_TYPES['DIGITAL_RESOURCE'])
