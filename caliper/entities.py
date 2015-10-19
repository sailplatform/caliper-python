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
from builtins import *

import collections

from caliper.constants import ENTITY_TYPES, ENTITY_CONTEXTS, CALIPER_ROLES, CALIPER_STATUS
from caliper.base import CaliperSerializable, BaseEntity
from caliper.base import is_valid_URI, ensure_type, ensure_list_type
from caliper.extern import foaf, schemadotorg, w3c

### Fundamental entities ###
## Base entity class
class Entity(BaseEntity, schemadotorg.Thing):

    ## Use the base context value here, but preserve the context labels
    ## in case, in the future, indivdual contexts start getting split out


    def __init__(self,
            entity_id = None,
            dateCreated = None,
            dateModified = None,
            description = None,
            name = None,
            extensions = {}):
        BaseEntity.__init__(self)
        self._set_id_prop('@id', entity_id, str, req=True)
        self._set_base_context(ENTITY_CONTEXTS['ENTITY'])
        self._set_str_prop('@type', ENTITY_TYPES['ENTITY'])
        self._set_str_prop('dateCreated', dateCreated)
        self._set_str_prop('dateModified', dateModified)
        self._set_str_prop('description', description)
        self._set_str_prop('name', name)
        self._set_obj_prop('extensions', extensions, t=collections.MutableMapping)

    @property
    def context(self):
        return self._unpack_context()

    @property
    def id(self):
        return self._get_prop('@id')

    @property
    def type(self):
        return self._get_prop('@type')

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

class Targetable(BaseEntity):
    pass

    
### Derived entities ###

## Membership entities

class Membership(Entity, w3c.Membership):

    def __init__(self,
                 member = None,
                 organization = None,
                 roles = None,
                 status = None,
                 **kwargs):
        Entity.__init__(self,**kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MEMBERSHIP'])
        self._set_str_prop('@type', ENTITY_TYPES['MEMBERSHIP'])

        self._set_id_prop('member', member, t=ENTITY_TYPES['PERSON'], req=True)
        self._set_id_prop('organization', organization, t=ENTITY_TYPES['ORGANIZATION'], req=True)

        if roles and isinstance(roles, collections.MutableSequence):
            if set(roles).issubset(set(CALIPER_ROLES.values())):
                self._set_list_prop('roles', roles)
            else:
                raise ValueError('roles must be in the list of valid Role values')
        elif roles:
            raise ValueError('roles must be a list of valid Roles values')
        else:
            self._set_list_prop('roles', None)

        if status not in CALIPER_STATUS.values():
            raise ValueError('status must be in the list of valid Status values')
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
class Agent(Entity, foaf.Agent):

    def __init__(self, **kwargs):
        Entity.__init__(self,**kwargs)

class SoftwareApplication(Agent, schemadotorg.SoftwareApplication):

    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SOFTWARE_APPLICATION'])
        self._set_str_prop('@type', ENTITY_TYPES['SOFTWARE_APPLICATION'])

class Person(Agent):

    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['PERSON'])
        self._set_str_prop('@type', ENTITY_TYPES['PERSON'])


## Organization entities
class Organization(Entity, w3c.Organization):
    _types = {
        }

    def __init__(self,
                 subOrganizationOf = None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ORGANIZATION'])
        self._set_str_prop('@type', ENTITY_TYPES['ORGANIZATION'])
        self._set_obj_prop('subOrganizationOf', subOrganizationOf, t=ENTITY_TYPES['ORGANIZATION'])

    @property
    def subOrganizationOf(self):
        return self._get_prop('subOrganizationOf')

class Course(Organization):

    def __init__(self,**kwargs):
        Organization.__init__(self,**kwargs)

class CourseOffering(Course):

    def __init__(self,
                 academicSession = None,
                 courseNumber = None,
                 **kwargs):
        Organization.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['COURSE_OFFERING'])
        self._set_str_prop('@type', ENTITY_TYPES['COURSE_OFFERING'])
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

    def __init__(self,
                 category = None,
                 **kwargs):
        CourseOffering.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['COURSE_SECTION'])        
        self._set_str_prop('@type', ENTITY_TYPES['COURSE_SECTION'])
        self._set_str_prop('category', category)

    @property
    def category(self):
        return self._get_prop('category')

class Group(Organization):

    def __init__(self, **kwargs):
        Organization.__init__(self,**kwargs)
        ensure_type(self.subOrganizationOf, Course)
        self._set_base_context(ENTITY_CONTEXTS['GROUP'])
        self._set_str_prop('@type', ENTITY_TYPES['GROUP'])

## Learning Context
class LearningContext(CaliperSerializable):

    def __init__(self,
                 edApp = None,
                 group = None,
                 membership = None,
                 session = None):
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
        self._set_str_prop('@type', ENTITY_TYPES['LEARNING_OBJECTIVE'])

    
## Creative works
class DigitalResource(Entity, schemadotorg.CreativeWork, Targetable):

    def __init__(self,
            alignedLearningObjective = None,
            datePublished = None,
            isPartOf = None,
            keywords = None,
            objectType = None,
            version = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['DIGITAL_RESOURCE'])
        self._set_str_prop('@type', ENTITY_TYPES['DIGITAL_RESOURCE'])
        self._set_list_prop('alignedLearningObjective', alignedLearningObjective,
                            t=ENTITY_TYPES['LEARNING_OBJECTIVE'])
        self._set_str_prop('datePublished', datePublished)
        self._set_obj_prop('isPartOf', isPartOf, t=schemadotorg.CreativeWork)
        self._set_list_prop('keywords', keywords, t=str)
        self._set_list_prop('objectType', objectType, t=str)
        self._set_str_prop('version', version)

            
    @property
    def alignedLearningObjective(self):
        return self._get_prop('alignedLearningObjective')

    @property
    def datePublished(self):
        return self._get_prop('datePublished')

    @property
    def isPartOf(self):
        return self._get_prop('isPartOf')
    @isPartOf.setter
    def isPartOf(self, new_object):
        self._set_obj_prop('isPartOf', isPartOf, t=schemadotorg.CreativeWork)

    @property
    def keywords(self):
        return self._get_prop('keywords')

    @property
    def objectType(self):
        return self._get_prop('objectType')

    @property
    def version(self):
        return self._get_prop('version')

class Frame(DigitalResource, Targetable):

    def __init__(self,
            index = 0,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['FRAME'])
        self._set_str_prop('@type', ENTITY_TYPES['FRAME'])
        self._set_int_prop('index', index, req=True)

    @property
    def index(self):
        return self._get_prop('index')
    
class Reading(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['READING'])
        self._set_str_prop('@type', ENTITY_TYPES['READING'])
                     
class WebPage(DigitalResource, schemadotorg.WebPage):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['WEB_PAGE'])
        self._set_str_prop('@type', ENTITY_TYPES['WEB_PAGE'])

class EpubChapter(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_CHAPTER'])
        self._set_str_prop('@type', ENTITY_TYPES['EPUB_CHAPTER'])
    
class EpubPart(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_PART'])
        self._set_str_prop('@type', ENTITY_TYPES['EPUB_PART'])

class EpubSubChapter(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_SUB_CHAPTER'])
        self._set_str_prop('@type', ENTITY_TYPES['EPUB_SUB_CHAPTER'])

class EpubVolume(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['EPUB_VOLUME'])
        self._set_str_prop('@type', ENTITY_TYPES['EPUB_VOLUME'])


## Annotation entities
class Annotation(Entity, Generatable):

    def __init__(self,
            annotated = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ANNOTATION'])
        self._set_str_prop('@type', ENTITY_TYPES['ANNOTATION'])
        self._set_id_prop('annotated', annotated, t=ENTITY_TYPES['DIGITAL_RESOURCE'], req=True)

    @property
    def annotated(self):
        return self._get_prop('annotated')

    @property
    def annotated_id(self):
        return self._get_prop('annotated')
    
            
class BookmarkAnnotation(Annotation):

    def __init__(self,
            bookmarkNotes = None,
            **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['BOOKMARK_ANNOTATION'])
        self._set_str_prop('@type', ENTITY_TYPES['BOOKMARK_ANNOTATION'])
        self._set_str_prop('bookmarkNotes', bookmarkNotes)
                 
    @property
    def bookmarkNotes(self):
        return self._get_prop('bookmarkNotes')

class HighlightAnnotation(Annotation):

    def __init__(self,
            selection = None,
            selectionText = None,
            **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['HIGHLIGHT_ANNOTATION'])
        self._set_str_prop('@type', ENTITY_TYPES['HIGHLIGHT_ANNOTATION'])
        self._set_obj_prop('selection', selection, t=TextPositionSelector)
        self._set_str_prop('selectionText', selectionText)
                 
    @property
    def selection(self):
        return self._get_prop('selection')

    @property
    def selectionText(self):
        return self.get_prop('selectionText')
    
class SharedAnnotation(Annotation):

    def __init__(self,
            withAgents = None,
            **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SHARED_ANNOTATION'])
        self._set_str_prop('@type', ENTITY_TYPES['SHARED_ANNOTATION'])
        self._set_list_prop('withAgents', withAgents, t=Agent)

    @property
    def withAgents(self):
        return self._get_prop('withAgents')

class TagAnnotation(Annotation):

    def __init__(self,
            tags = None,
            **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['TAG_ANNOTATION'])
        self._set_str_prop('@type', ENTITY_TYPES['TAG_ANNOTATION'])
        self._set_list_prop('tags', tags, t=str)
        
class TextPositionSelector(CaliperSerializable):

    def __init__(self,
            start = None,
            end = None):
        CaliperSerializable.__init__(self)

        self._set_str_prop('end', end, req=True)
        self._set_str_prop('start', start, req=True)

    @property
    def end(self):
        return self._get_prop('end')
    @end.setter
    def end(self, new_end):
        self._set_str_prop('end', new_end, req=True)

    @property
    def start(self):
        return self._get_prop('start')
    @start.setter
    def start(self, new_start):
        self._set_str_prop('start', new_start, req=True)


## Assessment entities
class AssignableDigitalResource(DigitalResource, Assignable):

    def __init__(self,
            dateToActivate = None,
            dateToShow = None,
            dateToStartOn = None,
            dateToSubmit = None,
            maxAttempts = None,
            maxSubmits = None,
            maxScore = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ASSIGNABLE_DIGITAL_RESOURCE'])        
        self._set_str_prop('@type', ENTITY_TYPES['ASSIGNABLE_DIGITAL_RESOURCE'])
        self._set_str_prop('dateToActivate', dateToActivate)
        self._set_str_prop('dateToShow', dateToShow)
        self._set_str_prop('dateToStartOn', dateToStartOn)
        self._set_str_prop('dateToSubmit', dateToSubmit)
        self._set_int_prop('maxAttempts', maxAttempts)
        self._set_int_prop('maxSubmits', maxSubmits)
        self._set_float_prop('maxScore', maxScore)

    @property
    def maxScore(self):
        return self._get_prop('maxScore')
    
class Assessment(AssignableDigitalResource):

    def __init__(self, **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ASSESSMENT'])
        self._set_str_prop('@type', ENTITY_TYPES['ASSESSMENT'])

class AssessmentItem(AssignableDigitalResource):

    def __init__(self,
                 isTimeDependent = False,
                 **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ASSESSMENT_ITEM'])        
        self._set_str_prop('@type', ENTITY_TYPES['ASSESSMENT_ITEM'])
        self._set_bool_prop('isTimeDependent', isTimeDependent, req=True)

    @property
    def isTimeDependent(self):
        return self._get_prop('isTimeDependent')


## Attempt and Response entities
class Attempt(Entity, Generatable):

    '''
    Keyword arguments:
    duration -- An xsd:duration (http://books.xmlschemata.org/relaxng/ch19-77073.html)

                The format is expected to be PnYnMnDTnHnMnS
                
                Valid values include PT1004199059S, PT130S, PT2M10S,
                P1DT2S, -P1Y, or P1Y2M3DT5H20M30.123S.
                
                The following values are invalid: 1Y (leading P is
                missing), P1S (T separator is missing), P-1Y (all parts
                must be positive), P1M2Y (parts order is significant and
                Y must precede M), or P1Y-1M (all parts must be
                positive).
    '''
    def __init__(self,
            actor = None,
assignable = None,
            count = None,
            duration = None,
            endedAtTime =None,
            startedAtTime = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['ATTEMPT'])
        self._set_str_prop('@type', ENTITY_TYPES['ATTEMPT'])
        self._set_id_prop('actor', actor, Agent, req=True)
        self._set_id_prop('assignable', assignable, t=ENTITY_TYPES['DIGITAL_RESOURCE'], req=True)
        self._set_int_prop('count', count, req=True)
        self._set_str_prop('duration', duration)
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_str_prop('startedAtTime', startedAtTime, req=True)
            
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
        self._set_str_prop('duration', new_duration)

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')
    @endedAtTime.setter
    def endedAtTime(self,new_time):
        self._set_str_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')

class Response(Entity, Generatable):

    def __init__(self,
            assignable = None,
            actor = None,
            attempt = None,
            duration = None,
            endedAtTime =None,
            startedAtTime = None,
            values = None,
            **kwargs):
        Entity.__init__(self,**kwargs)
        self._set_base_context(ENTITY_CONTEXTS['RESPONSE'])
        self._set_str_prop('@type', ENTITY_TYPES['RESPONSE'])
        self._set_id_prop('actor', actor, t=Agent, req=True)
        self._set_id_prop('assignable', assignable, t=ENTITY_TYPES['DIGITAL_RESOURCE'], req=True)
        self._set_obj_prop('attempt', attempt, t=ENTITY_TYPES['ATTEMPT'], req=True)
        self._set_str_prop('duration', duration)
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_str_prop('startedAtTime', startedAtTime)
        self._set_list_prop('values', values)

    @property
    def assignable(self):
        return self._get_prop('assignable')

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def duration(self):
        return self._get_prop('duration')
    @duration.setter
    def duration(self, new_duration):
        self._set_str_prop('duration', new_duration)

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')
    @endedAtTime.setter
    def endedAtTime(self,new_time):
        self._set_str_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')

    @property
    def values(self):
        return self._get_prop('values')

class FillinBlankResponse(Response):

    def __init__(self, **kwargs):
        Response.__init__(self,**kwargs)
        ensure_list_type(self.values,str)
        self._set_base_context(ENTITY_CONTEXTS['FILLINBLANK'])
        self._set_str_prop('@type', ENTITY_TYPES['FILLINBLANK'])

class MultipleChoiceResponse(Response):

    def __init__(self, **kwargs):
        Response.__init__(self,**kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MULTIPLECHOICE'])
        self._set_str_prop('@type', ENTITY_TYPES['MULTIPLECHOICE'])

class MultipleResponseResponse(Response):

    def __init__(self, **kwargs):
        Response.__init__(self,**kwargs)
        ensure_list_type(self.values,str)
        self._set_base_context(ENTITY_CONTEXTS['MULTIPLERESPONSE'])
        self._set_str_prop('@type', ENTITY_TYPES['MULTIPLERESPONSE'])
        
class SelectTextResponse(Response):

    def __init__(self, **kwargs):
        Response.__init__(self,**kwargs)
        ensure_list_type(self.values,str)
        self._set_base_context(ENTITY_CONTEXTS['SELECTTEXT'])
        self._set_str_prop('@type', ENTITY_TYPES['SELECTTEXT'])


class TrueFalseResponse(Response):

    def __init__(self, **kwargs):
        Response.__init__(self,**kwargs)
        self._set_base_context(ENTITY_CONTEXTS['TRUEFALSE'])
        self._set_str_prop('@type', ENTITY_TYPES['TRUEFALSE'])


## Media entities
class MediaObject(DigitalResource, schemadotorg.MediaObject):

    def __init__(self,
            duration = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MEDIA_OBJECT'])
        self._set_str_prop('@type', ENTITY_TYPES['MEDIA_OBJECT'])
        self._set_int_prop('duration', duration)

    @property
    def duration(self):
        return self._get_prop('duration')

class MediaLocation(DigitalResource, Targetable):

    def __init__(self,
            currentTime = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['MEDIA_LOCATION'])
        self._set_str_prop('@type', ENTITY_TYPES['MEDIA_LOCATION'])
        self._set_int_prop('currentTime', currentTime)

    @property
    def currentTime(self):
        return self._get_prop('currentTime')
    
class AudioObject(MediaObject, schemadotorg.AudioObject):

    def __init__(self,
            muted = None,
            volumeLevel = None,
            volumeMax = None,
            volumeMin = None,
            **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['AUDIO_OBJECT'])
        self._set_str_prop('@type', ENTITY_TYPES['AUDIO_OBJECT'])
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


class ImageObject(MediaObject, schemadotorg.ImageObject):

    def __init__(self, **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['IMAGE_OBJECT'])
        self._set_str_prop('@type', ENTITY_TYPES['IMAGE_OBJECT'])

class VideoObject(MediaObject, schemadotorg.VideoObject):

    def __init__(self, **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['VIDEO_OBJECT'])
        self._set_str_prop('@type', ENTITY_TYPES['VIDEO_OBJECT'])


## Outcome entities
class Result(Entity, Generatable):

    def __init__(self,
            actor = None,
            assignable = None,
            comment = None,
            curvedTotalScore = 0.0,
            curveFactor = 0.0,
            extraCreditScore = 0.0,
            normalScore = 0.0,
            penaltyScore = 0.0,
            scoredBy = None,
            totalScore = 0.0,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['RESULT'])
        self._set_str_prop('@type', ENTITY_TYPES['RESULT'])
        self._set_id_prop('actor', actor, t=Agent, req=True)
        self._set_id_prop('assignable', assignable, t=Assignable, req=True)
        self._set_str_prop('comment', comment)
        self._set_float_prop('curvedTotalScore', curvedTotalScore)
        self._set_float_prop('curveFactor', curveFactor)
        self._set_float_prop('extraCreditScore', extraCreditScore)
        self._set_float_prop('normalScore', normalScore)
        self._set_float_prop('penaltyScore', penaltyScore)
        self._set_obj_prop('scoredBy', scoredBy, Agent)
        self._set_float_prop('totalScore', totalScore)

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def assignable(self):
        return self._get_prop('assignable')

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

    def __init__(self,
                 actor = None,
                 duration = None,
                 endedAtTime = None,
                 startedAtTime = None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_base_context(ENTITY_CONTEXTS['SESSION'])
        self._set_str_prop('@type', ENTITY_TYPES['SESSION'])
        self._set_obj_prop('actor', actor, t=Agent, req=True)
        self._set_str_prop('duration', duration)
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_str_prop('startedAtTime', startedAtTime)

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def duration(self):
        return self._get_prop('duration')
    @duration.setter
    def duration(self, new_duration):
        self._set_str_prop('duration', new_duration)

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')
    @endedAtTime.setter
    def endedAtTime(self,new_time):
        self._set_str_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')
