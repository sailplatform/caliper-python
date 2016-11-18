# -*- coding: utf-8 -*-
# Caliper-python package, entities module
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

import collections

from caliper.constants import ENTITY_TYPES, ENTITY_CONTEXTS, CALIPER_ROLES, CALIPER_STATUS
from caliper.base import CaliperSerializable, BaseEntity
from caliper.base import is_valid_date, is_valid_duration, is_valid_URI
from caliper.base import ensure_type, ensure_list_type


### Fundamental entities ###
## Base entity class
class Entity(BaseEntity):

    ## Use the base context value here, but preserve the context labels
    ## in case, in the future, indivdual contexts start getting split out

    def __init__(self,
                 id=None,
                 dateCreated=None,
                 dateModified=None,
                 description=None,
                 name=None,
                 version=None,
                 extensions=None):
        BaseEntity.__init__(self)
        self._set_id_prop('id', id, str, req=True)
        self._set_base_context(ENTITY_CONTEXTS['ENTITY'])
        self._set_str_prop('type', ENTITY_TYPES['ENTITY'])
        self._set_date_prop('dateCreated', dateCreated)
        self._set_date_prop('dateModified', dateModified)
        self._set_str_prop('description', description)
        self._set_str_prop('name', name)
        self._set_dict_prop('extensions', extensions)

    @property
    def context(self):
        return self._unpack_context()

    @property
    def id(self):
        return self._get_prop('id')

    @property
    def type(self):
        return self._get_prop('type')

    @property
    def dateCreated(self):
        return self._get_prop('dateCreated')

    @property
    def dateModified(self):
        return self._get_prop('dateModified')

    @property
    def description(self):
        return self._get_prop('description')

    @property
    def name(self):
        return self._get_prop('name')

    @property
    def extensions(self):
        return self._get_prop('extensions')


## Base collection class
class Collection(Entity):
    def __init__(self, isPartOf=None, items=None, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['COLLECTION'])
        self._set_str_prop('type', ENTITY_TYPES['COLLECTION'])

        self._set_obj_prop('isPartOf', isPartOf, t=ENTITY_TYPES['ENTITY'])
        self._set_list_prop('items', items, t=ENTITY_TYPES['ENTITY'])

    @property
    def isPartOf(self):
        return self._get_prop('isPartOf')

    @property
    def items(self):
        return self._get_prop('items')


## Behavioural interfaces for entities ##
class Assignable(BaseEntity):
    @property
    def datePublished(self):
        return self._get_prop('datePublished')

    @property
    def dateToActivate(self):
        return self._get_prop('dateToActivate')

    @property
    def dateToShow(self):
        return self._get_prop('dateToShow')

    @property
    def dateToStartOn(self):
        return self._get_prop('dateToStartOn')

    @property
    def dateToSubmit(self):
        return self._get_prop('dateToSubmit')

    @property
    def maxAttempts(self):
        return self._get_prop('maxAttempts')

    @property
    def maxSubmits(self):
        return self._get_prop('maxSubmits')


class Generatable(BaseEntity):
    pass


class Referrable(BaseEntity):
    pass


class Targetable(BaseEntity):
    pass


### Derived entities ###
## Membership entities


class Membership(Entity):
    def __init__(self, member=None, organization=None, roles=None, status=None, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MEMBERSHIP'])
        self._set_str_prop('type', ENTITY_TYPES['MEMBERSHIP'])

        self._set_obj_prop('member', member, t=ENTITY_TYPES['PERSON'], req=True)
        self._set_obj_prop('organization', organization, t=ENTITY_TYPES['ORGANIZATION'], req=True)

        if roles and isinstance(roles, collections.MutableSequence):
            if set(roles).issubset(set(CALIPER_ROLES.values())):
                self._set_list_prop('roles', roles)
            else:
                raise_with_traceback(ValueError('roles must be in the list of valid Role values'))
        elif roles:
            raise_with_traceback(ValueError('roles must be a list of valid Roles values'))
        else:
            self._set_list_prop('roles', None)

        if status not in CALIPER_STATUS.values():
            raise_with_traceback(ValueError('status must be in the list of valid Status values'))
        else:
            self._set_str_prop('status', status, req=True)

    @property
    def member(self):
        return self._get_prop('member')

    @property
    def organization(self):
        return self._get_prop('organization')

    @property
    def roles(self):
        return self._get_prop('roles')

    @property
    def status(self):
        return self._get_prop('status')


## Agent entities
class Agent(Entity, Referrable):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)


class SoftwareApplication(Agent):
    def __init__(self, version=None, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SOFTWARE_APPLICATION'])
        self._set_str_prop('type', ENTITY_TYPES['SOFTWARE_APPLICATION'])
        self._set_str_prop('version', version)

    @property
    def version(self):
        return self._get_prop('version')


class Person(Agent):
    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['PERSON'])
        self._set_str_prop('type', ENTITY_TYPES['PERSON'])


## Organization entities
class Organization(Agent):
    _types = {}

    def __init__(self, subOrganizationOf=None, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ORGANIZATION'])
        self._set_str_prop('type', ENTITY_TYPES['ORGANIZATION'])
        self._set_obj_prop('subOrganizationOf', subOrganizationOf, t=ENTITY_TYPES['ORGANIZATION'])

    @property
    def subOrganizationOf(self):
        return self._get_prop('subOrganizationOf')


class CourseOffering(Organization):
    def __init__(self, academicSession=None, courseNumber=None, **kwargs):
        Organization.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['COURSE_OFFERING'])
        self._set_str_prop('type', ENTITY_TYPES['COURSE_OFFERING'])
        self._set_str_prop('academicSession', academicSession)
        self._set_str_prop('courseNumber', courseNumber)

    @property
    def academicSession(self):
        return self._get_prop('academicSession')

    @property
    def courseNumber(self):
        return self._get_prop('courseNumber')

    @property
    def label(self):
        return self._get_prop('label')

    @property
    def semester(self):
        return self._get_prop('semester')


class CourseSection(CourseOffering):
    def __init__(self, category=None, **kwargs):
        CourseOffering.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['COURSE_SECTION'])
        self._set_str_prop('type', ENTITY_TYPES['COURSE_SECTION'])
        self._set_str_prop('category', category)

    @property
    def category(self):
        return self._get_prop('category')


class Group(Organization):
    def __init__(self, **kwargs):
        Organization.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['GROUP'])
        self._set_str_prop('type', ENTITY_TYPES['GROUP'])


## Learning Context
class LearningContext(CaliperSerializable):
    def __init__(self, edApp=None, group=None, membership=None, session=None):
        CaliperSerializable.__init__(self)
        self._set_obj_prop('edApp', edApp, t=ENTITY_TYPES['SOFTWARE_APPLICATION'])
        self._set_obj_prop('group', group, t=ENTITY_TYPES['ORGANIZATION'])
        self._set_obj_prop('membership', membership, t=ENTITY_TYPES['MEMBERSHIP'])
        self._set_obj_prop('session', session, t=ENTITY_TYPES['SESSION'])

    @property
    def edApp(self):
        return self._get_prop('edApp')

    @property
    def group(self):
        return self._get_prop('group')

    @property
    def membership(self):
        return self._get_prop('membership')

    @property
    def session(self):
        return self._get_prop('session')


## Learning objective
class LearningObjective(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['LEARNING_OBJECTIVE'])
        self._set_str_prop('type', ENTITY_TYPES['LEARNING_OBJECTIVE'])


## Creative works
class DigitalResource(Entity, Referrable, Targetable):
    def __init__(self,
                 learningObjectives=None,
                 creators=None,
                 datePublished=None,
                 isPartOf=None,
                 keywords=None,
                 mediaType=None,
                 version=None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['DIGITAL_RESOURCE'])
        self._set_str_prop('type', ENTITY_TYPES['DIGITAL_RESOURCE'])
        self._set_list_prop(
            'learningObjectives', learningObjectives, t=ENTITY_TYPES['LEARNING_OBJECTIVE'])
        self._set_list_prop('creators', creators, t=ENTITY_TYPES['AGENT'])
        self._set_date_prop('datePublished', datePublished)
        self._set_obj_prop('isPartOf', isPartOf, t=ENTITY_TYPES['ENTITY'])
        self._set_list_prop('keywords', keywords, t=str)
        self._set_str_prop('mediaType', mediaType)
        self._set_str_prop('version', version)

    @property
    def learningObjectives(self):
        return self._get_prop('learningObjectives')

    @property
    def creators(self):
        return self._get_prop('creators')

    @property
    def datePublished(self):
        return self._get_prop('datePublished')

    @property
    def isPartOf(self):
        return self._get_prop('isPartOf')

    @isPartOf.setter
    def isPartOf(self, new_object):
        self._set_obj_prop('isPartOf', isPartOf, t=ENTITY_TYPES['ENTITY'])

    @property
    def keywords(self):
        return self._get_prop('keywords')

    @property
    def mediaType(self):
        return self._get_prop('mediaType')

    @property
    def version(self):
        return self._get_prop('version')


class DigitalResourceCollection(DigitalResource, Collection):
    def __init__(self, items=None, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['DIGITAL_RESOURCE_COLLECTION'])
        self._set_str_prop('type', ENTITY_TYPES['DIGITAL_RESOURCE_COLLECTION'])
        self._set_list_prop('items', items, t=ENTITY_TYPES['DIGITAL_RESOURCE'])


class Frame(DigitalResource, Targetable):
    def __init__(self, index=None, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['FRAME'])
        self._set_str_prop('type', ENTITY_TYPES['FRAME'])
        self._set_int_prop('index', index, req=True)

    @property
    def index(self):
        return self._get_prop('index')


class Reading(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['READING'])
        self._set_str_prop('type', ENTITY_TYPES['READING'])


class WebPage(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['WEB_PAGE'])
        self._set_str_prop('type', ENTITY_TYPES['WEB_PAGE'])


class Document(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['DOCUMENT'])
        self._set_str_prop('type', ENTITY_TYPES['DOCUMENT'])


class Chapter(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['CHAPTER'])
        self._set_str_prop('type', ENTITY_TYPES['CHAPTER'])


class Page(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['PAGE'])
        self._set_str_prop('type', ENTITY_TYPES['PAGE'])


class EpubChapter(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_CHAPTER'])
        self._set_str_prop('type', ENTITY_TYPES['EPUB_CHAPTER'])


class EpubPart(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_PART'])
        self._set_str_prop('type', ENTITY_TYPES['EPUB_PART'])


class EpubSubChapter(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_SUB_CHAPTER'])
        self._set_str_prop('type', ENTITY_TYPES['EPUB_SUB_CHAPTER'])


class EpubVolume(DigitalResource):
    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_VOLUME'])
        self._set_str_prop('type', ENTITY_TYPES['EPUB_VOLUME'])


## Annotation entities
class Annotation(Entity, Generatable):
    def __init__(self, actor=None, annotated=None, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ANNOTATION'])
        self._set_str_prop('type', ENTITY_TYPES['ANNOTATION'])
        self._set_obj_prop('actor', actor, t=ENTITY_TYPES['AGENT'], req=True)
        self._set_obj_prop('annotated', annotated, t=ENTITY_TYPES['DIGITAL_RESOURCE'], req=True)

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def annotated(self):
        return self._get_prop('annotated')

    @property
    def annotated_id(self):
        return self._get_prop('annotated')


class BookmarkAnnotation(Annotation):
    def __init__(self, bookmarkNotes=None, **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['BOOKMARK_ANNOTATION'])
        self._set_str_prop('type', ENTITY_TYPES['BOOKMARK_ANNOTATION'])
        self._set_str_prop('bookmarkNotes', bookmarkNotes)

    @property
    def bookmarkNotes(self):
        return self._get_prop('bookmarkNotes')


class HighlightAnnotation(Annotation):
    def __init__(self, selection=None, selectionText=None, **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['HIGHLIGHT_ANNOTATION'])
        self._set_str_prop('type', ENTITY_TYPES['HIGHLIGHT_ANNOTATION'])
        self._set_obj_prop('selection', selection, t=TextPositionSelector)
        self._set_str_prop('selectionText', selectionText)

    @property
    def selection(self):
        return self._get_prop('selection')

    @property
    def selectionText(self):
        return self._get_prop('selectionText')


class SharedAnnotation(Annotation):
    def __init__(self, withAgents=None, **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SHARED_ANNOTATION'])
        self._set_str_prop('type', ENTITY_TYPES['SHARED_ANNOTATION'])
        self._set_list_prop('withAgents', withAgents, t=ENTITY_TYPES['AGENT'])

    @property
    def withAgents(self):
        return self._get_prop('withAgents')


class TagAnnotation(Annotation):
    def __init__(self, tags=None, **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['TAG_ANNOTATION'])
        self._set_str_prop('type', ENTITY_TYPES['TAG_ANNOTATION'])
        self._set_list_prop('tags', tags, t=str)


class TextPositionSelector(Entity):
    def __init__(self, start=None, end=None, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['TEXT_POSITION_SELECTOR'])
        self._set_str_prop('type', ENTITY_TYPES['TEXT_POSITION_SELECTOR'])
        self._set_int_prop('end', end, req=True)
        self._set_int_prop('start', start, req=True)

    @property
    def end(self):
        return self._get_prop('end')

    @end.setter
    def end(self, new_end):
        self._set_int_prop('end', new_end, req=True)

    @property
    def start(self):
        return self._get_prop('start')

    @start.setter
    def start(self, new_start):
        self._set_int_prop('start', new_start, req=True)


## Assessment entities
class AssignableDigitalResource(DigitalResource, Assignable):
    def __init__(self,
                 dateToActivate=None,
                 dateToShow=None,
                 dateToStartOn=None,
                 dateToSubmit=None,
                 maxAttempts=None,
                 maxSubmits=None,
                 maxScore=None,
                 **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ASSIGNABLE_DIGITAL_RESOURCE'])
        self._set_str_prop('type', ENTITY_TYPES['ASSIGNABLE_DIGITAL_RESOURCE'])
        self._set_date_prop('dateToActivate', dateToActivate)
        self._set_date_prop('dateToShow', dateToShow)
        self._set_date_prop('dateToStartOn', dateToStartOn)
        self._set_date_prop('dateToSubmit', dateToSubmit)
        self._set_int_prop('maxAttempts', maxAttempts)
        self._set_int_prop('maxSubmits', maxSubmits)
        self._set_float_prop('maxScore', maxScore)

    @property
    def maxScore(self):
        return self._get_prop('maxScore')


class Assessment(AssignableDigitalResource):
    def __init__(self, items=None, **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ASSESSMENT'])
        self._set_str_prop('type', ENTITY_TYPES['ASSESSMENT'])
        self._set_list_prop('items', items, t=ENTITY_TYPES['ASSESSMENT_ITEM'])


class AssessmentItem(AssignableDigitalResource):
    def __init__(self, isTimeDependent=None, **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ASSESSMENT_ITEM'])
        self._set_str_prop('type', ENTITY_TYPES['ASSESSMENT_ITEM'])
        self._set_bool_prop('isTimeDependent', isTimeDependent)

    @property
    def isTimeDependent(self):
        return self._get_prop('isTimeDependent')


## Attempt and Response entities
class Attempt(Entity, Generatable):
    def __init__(self,
                 actor=None,
                 assignable=None,
                 count=None,
                 duration=None,
                 endedAtTime=None,
                 isPartOf=None,
                 startedAtTime=None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ATTEMPT'])
        self._set_str_prop('type', ENTITY_TYPES['ATTEMPT'])
        self._set_obj_prop('actor', actor, t=ENTITY_TYPES['AGENT'])
        self._set_obj_prop('assignable', assignable, t=Assignable)
        self._set_int_prop('count', count)
        self._set_duration_prop('duration', duration)
        self._set_date_prop('endedAtTime', endedAtTime)
        self._set_obj_prop('isPartOf', isPartOf, t=ENTITY_TYPES['ATTEMPT'])
        self._set_date_prop('startedAtTime', startedAtTime)

    @property
    def assignable(self):
        return self._get_prop('assignable')

    @property
    def assignable_id(self):
        return self._get_prop('assignable')

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def actor_id(self):
        return self._get_prop('actor')

    @property
    def count(self):
        return self._get_prop('count')

    @property
    def duration(self):
        return self._get_prop('duration')

    @duration.setter
    def duration(self, new_duration):
        self._set_duration_prop('duration', new_duration)

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')

    @endedAtTime.setter
    def endedAtTime(self, new_time):
        self._set_date_prop('endedAtTime', new_time)

    @property
    def isPartOf(self):
        return self._get_prop('isPartOf')

    @isPartOf.setter
    def isPartOf(self, new_object):
        self._set_obj_prop('isPartOf', isPartOf, t=ENTITY_TYPES['Attempt'])

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')


class Response(Entity, Generatable):
    def __init__(self, attempt=None, duration=None, endedAtTime=None, startedAtTime=None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['RESPONSE'])
        self._set_str_prop('type', ENTITY_TYPES['RESPONSE'])
        self._set_obj_prop('attempt', attempt, t=ENTITY_TYPES['ATTEMPT'], req=True)
        self._set_duration_prop('duration', duration)
        self._set_date_prop('endedAtTime', endedAtTime)
        self._set_date_prop('startedAtTime', startedAtTime)

    @property
    def attempt(self):
        return self._get_prop('attempt')

    @property
    def duration(self):
        return self._get_prop('duration')

    @duration.setter
    def duration(self, new_duration):
        self._set_duration_prop('duration', new_duration)

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')

    @endedAtTime.setter
    def endedAtTime(self, new_time):
        self._set_date_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')


class FillinBlankResponse(Response):
    def __init__(self, values=None, **kwargs):
        Response.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['FILLINBLANK'])
        self._set_str_prop('type', ENTITY_TYPES['FILLINBLANK'])
        self._set_list_prop('values', values, t=str)

    @property
    def values(self):
        return self._get_prop('values')


class MultipleChoiceResponse(Response):
    def __init__(self, value=None, **kwargs):
        Response.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MULTIPLECHOICE'])
        self._set_str_prop('type', ENTITY_TYPES['MULTIPLECHOICE'])
        self._set_str_prop('value', value)

    @property
    def value(self):
        return self._get_prop('value')


class MultipleResponseResponse(Response):
    def __init__(self, values=None, **kwargs):
        Response.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MULTIPLERESPONSE'])
        self._set_str_prop('type', ENTITY_TYPES['MULTIPLERESPONSE'])
        self._set_list_prop('values', values, t=str)

    @property
    def values(self):
        return self._get_prop('values')


class SelectTextResponse(Response):
    def __init__(self, values=None, **kwargs):
        Response.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SELECTTEXT'])
        self._set_str_prop('type', ENTITY_TYPES['SELECTTEXT'])
        self._set_list_prop('values', values, t=str)

    @property
    def values(self):
        return self._get_prop('values')


class TrueFalseResponse(Response):
    def __init__(self, value=None, **kwargs):
        Response.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['TRUEFALSE'])
        self._set_str_prop('type', ENTITY_TYPES['TRUEFALSE'])
        self._set_str_prop('value', value)

    @property
    def value(self):
        return self._get_prop('value')


## Discussion forum entities
class Forum(DigitalResourceCollection):
    def __init__(self, items=None, **kwargs):
        DigitalResourceCollection.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['FORUM'])
        self._set_str_prop('type', ENTITY_TYPES['FORUM'])
        self._set_list_prop('items', items, t=ENTITY_TYPES['THREAD'])


class Thread(DigitalResourceCollection):
    def __init__(self, items=None, **kwargs):
        DigitalResourceCollection.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['THREAD'])
        self._set_str_prop('type', ENTITY_TYPES['THREAD'])
        self._set_list_prop('items', items, t=ENTITY_TYPES['MESSAGE'])


class Message(DigitalResource):
    def __init__(self, body=None, replyTo=None, attachments=None, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MESSAGE'])
        self._set_str_prop('type', ENTITY_TYPES['MESSAGE'])
        self._set_str_prop('body', body)
        self._set_obj_prop('replyTo', replyTo, t=ENTITY_TYPES['MESSAGE'])
        self._set_list_prop('attachments', attachments, t=ENTITY_TYPES['DIGITAL_RESOURCE'])


## Media entities
class MediaObject(DigitalResource):
    def __init__(self, duration=None, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MEDIA_OBJECT'])
        self._set_str_prop('type', ENTITY_TYPES['MEDIA_OBJECT'])
        self._set_duration_prop('duration', duration)

    @property
    def duration(self):
        return self._get_prop('duration')


class MediaLocation(DigitalResource, Targetable):
    def __init__(self, currentTime=None, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MEDIA_LOCATION'])
        self._set_str_prop('type', ENTITY_TYPES['MEDIA_LOCATION'])
        self._set_duration_prop('currentTime', currentTime)

    @property
    def currentTime(self):
        return self._get_prop('currentTime')


class AudioObject(MediaObject):
    def __init__(self, muted=None, volumeLevel=None, volumeMax=None, volumeMin=None, **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['AUDIO_OBJECT'])
        self._set_str_prop('type', ENTITY_TYPES['AUDIO_OBJECT'])
        self._set_bool_prop('muted', muted)
        self._set_str_prop('volumeLevel', volumeLevel)
        self._set_str_prop('volumeMax', volumeMax)
        self._set_str_prop('volumeMin', volumeMin)

    @property
    def muted(self):
        return self._get_prop('muted')

    @property
    def volumeLevel(self):
        return self._get_prop('volumeLevel')

    @property
    def volumeMax(self):
        return self._get_prop('volumeMax')

    @property
    def volumeMin(self):
        return self._get_prop('volumeMin')


class ImageObject(MediaObject):
    def __init__(self, **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['IMAGE_OBJECT'])
        self._set_str_prop('type', ENTITY_TYPES['IMAGE_OBJECT'])


class VideoObject(MediaObject):
    def __init__(self, **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['VIDEO_OBJECT'])
        self._set_str_prop('type', ENTITY_TYPES['VIDEO_OBJECT'])


## Outcome entities
class Result(Entity, Generatable):
    def __init__(self,
                 attempt=None,
                 comment=None,
                 curvedTotalScore=None,
                 curveFactor=None,
                 extraCreditScore=None,
                 normalScore=None,
                 penaltyScore=None,
                 scoredBy=None,
                 totalScore=None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['RESULT'])
        self._set_str_prop('type', ENTITY_TYPES['RESULT'])
        self._set_obj_prop('attempt', attempt, t=ENTITY_TYPES['ATTEMPT'], req=True)
        self._set_str_prop('comment', comment)
        self._set_float_prop('curvedTotalScore', curvedTotalScore)
        self._set_float_prop('curveFactor', curveFactor)
        self._set_float_prop('extraCreditScore', extraCreditScore)
        self._set_float_prop('normalScore', normalScore)
        self._set_float_prop('penaltyScore', penaltyScore)
        self._set_obj_prop('scoredBy', scoredBy, t=ENTITY_TYPES['AGENT'])
        self._set_float_prop('totalScore', totalScore)

    @property
    def attempt(self):
        return self._get_prop('attempt')

    @property
    def comment(self):
        return self._get_prop('comment')

    @property
    def curvedTotalScore(self):
        return self._get_prop('curvedTotalScore')

    @property
    def curveFactor(self):
        return self._get_prop('curveFactor')

    @property
    def extraCreditScore(self):
        return self._get_prop('extraCreditScore')

    @property
    def normalScore(self):
        return self._get_prop('normalScore')

    @property
    def penaltyScore(self):
        return self._get_prop('penaltyScore')

    @property
    def scoredBy(self):
        return self._get_prop('scoredBy')


## Session entities
class Session(Entity, Generatable, Targetable):
    def __init__(self, actor=None, duration=None, endedAtTime=None, startedAtTime=None, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SESSION'])
        self._set_str_prop('type', ENTITY_TYPES['SESSION'])
        self._set_obj_prop('actor', actor, t=ENTITY_TYPES['AGENT'])
        self._set_duration_prop('duration', duration)
        self._set_date_prop('endedAtTime', endedAtTime)
        self._set_date_prop('startedAtTime', startedAtTime)

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def duration(self):
        return self._get_prop('duration')

    @duration.setter
    def duration(self, new_duration):
        self._set_duration_prop('duration', new_duration)

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')

    @endedAtTime.setter
    def endedAtTime(self, new_time):
        self._set_date_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')


class LtiSession(Session):
    def __init__(self, launchParameters=None, **kwargs):
        Session.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['LTI_SESSION'])
        self._set_str_prop('type', ENTITY_TYPES['LTI_SESSION'])
        self._set_dict_prop('launchParameters', launchParameters)

    @property
    def launchParameters(self):
        return self._get_prop('launchParameters')
