# -*- coding: utf-8 -*-
# Caliper-python package, entities module
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

import collections
from rfc3987 import parse as rfc3987_parse
import six
import uuid

from .base import BaseEntity, CaliperSerializable
from .extern import foaf, qti, schemadotorg

### Fundamental entities ###
## Base entity class
class Entity(BaseEntity):

    _types = {
        'ACTIVITY_CONTEXT': 'http://purl.imsglobal.org/caliper/v1/ActivityContext',
        'AGENT': 'http://purl.imsglobal.org/caliper/v1/Agent',
        'ATTEMPT': 'http://purl.imsglobal.org/caliper/v1/Attempt',
        'DIGITAL_RESOURCE': 'http://purl.imsglobal.org/caliper/v1/DigitalResource',
        'ENTITY': 'http://purl.imsglobal.org/caliper/v1/Entity',
        'LEARNING_OBJECTIVE': 'http://purl.imsglobal.org/caliper/v1/LearningObjective',
        'MEDIA_LOCATION': 'http://purl.imsglobal.org/caliper/v1/MediaLocation',
        'RESULT': 'http://purl.imsglobal.org/caliper/v1/Result',
        'VIEW': 'http://purl.imsglobal.org/caliper/v1/View',
        }

    def __init__(self,
            entity_id = None,
            name = None,
            lastModifiedTime = 0,
            properties = {},
            **kwargs):
        BaseEntity.__init__(self, **kwargs)
        self._set_str_prop('@id', entity_id)
        self._set_str_prop('@type', Entity.Types['ENTITY'])
        self._set_int_prop('lastModifiedTime', lastModifiedTime)
        self._set_str_prop('name', name)

        if properties and (not isinstance(properties, collections.MutableMapping)):
            raise TypeError('properties must be a dictionary or mapping of key-value pairs')
        else:
            self._set_obj_prop('properties', properties)

    @property
    def id(self):
        return self._get_prop('@id')

    @property
    def type(self):
        return self._get_prop('@type')

    @property
    def lastModifiedTime(self):
        return self._get_prop('lastModifiedTime')

    @property
    def name(self):
        return self._get_prop('name')

    @property
    def properties(self):
        return self._get_obj_prop('properties')


### Derived entities ###

## Activity context entities
class ActivityContext(Entity):

    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['ACTIVITY_CONTEXT'])

## Agent entities
class Agent(Entity, foaf.Agent):
    _types = {
        'LIS_PERSON': 'http://purl.imsglobal.org/caliper/v1/lis/Person',
        'LIS_ORGANIZATION': 'http://purl.imsglobal.org/caliper/v1/lis/Organization',
        'SOFTWARE_APPLICATION': 'http://purl.imsglobal.org/caliper/v1/SoftwareApplication',
        }

    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['AGENT'])

class SoftwareApplication(Agent):

    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_str_prop('@type', Agent.Types['SOFTWARE_APPLICATION'])

class Person(Agent):

    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_str_prop('@type', Agent.Types['LIS_PERSON'])

class Organization(Agent):
    _types = {
        'LIS_COURSE_SECTION': 'http://purl.imsglobal.org/caliper/v1/lis/CourseSection',
        }

    def __init__(self,
            parentOrg=None,
            **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_str_prop('@type', Agent.Types['LIS_ORGANIZATION'])

        if parentOrg and (not isinstance(parentOrg, Organization)):
            raise TypeError('parentOrg must implement Organization')
        else:
            self._set_obj_prop('parentOrg', parentOrg)

    @property
    def parentOrg(self):
        return self._get_prop('parentOrg')

class CourseSection(Organization):

    def __init__(self,
                 courseNumber = None,
                 label = None,
                 semester = None,
                 **kwargs):
        Organization.__init__(self, **kwargs)
        self._set_str_prop('@type', Organization.Types['LIS_COURSE_SECTION'])
        self._set_str_prop('courseNumber', courseNumber)
        self._set_str_prop('label', label)
        self._set_str_prop('semester', semester)

    @property
    def courseNumber(self):
        return self._get_prop('courseNumber')

    @property
    def label(self):
        return self._get_prop('label')

    @property
    def semester(self):
        return self._get_prop('semester')


## Learning Context
class LearningContext(CaliperSerializable):
    def __init__(self,
                 agent = None,
                 edApp = None,
                 lisOrganization = None):

        CaliperSerializable.__init__(self)

        if agent and (not isinstance(agent, Agent)):
            raise TypeError('agent must implement Agent')
        else:
            self._set_obj_prop('agent', agent)

        if edApp and (not isinstance(edApp, SoftwareApplication)):
            raise TypeError('edApp must implement SoftwareApplication')
        else:
            self._set_obj_prop('edApp', edApp)

        if lisOrganization and (not isinstance(lisOrganization, Organization)):
            raise TypeError('lisOrganization must implement Organization')
        else:
            self._set_obj_prop('lisOrganization', lisOrganization)
            
    @property
    def agent(self):
        return self._get_prop('agent')

    @property
    def edApp(self):
        return self._get_prop('edApp')

    @property
    def lisOrganization(self):
        return self._get_prop('lisOrganization')


## Learning objective
class LearningObjective(Entity):

    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['LEARNING_OBJECTIVE'])

    
## Creative works
class DigitalResource(Entity, schemadotorg.CreativeWork):

    _types = {
        'ASSIGNABLE_DIGITAL_RESOURCE': 'http://purl.imsglobal.org/caliper/v1/AssignableDigitalResource',
        'EPUB_CHAPTER': 'http://www.idpf.org/epub/vocab/structure/#chapter',
        'EPUB_PART': 'http://www.idpf.org/epub/vocab/structure/#part',
        'EPUB_SUB_CHAPTER': 'http://www.idpf.org/epub/vocab/structure/#subchapter',
        'EPUB_VOLUME': 'http://www.idpf.org/epub/vocab/structure/#volume',
        'FRAME': 'http://purl.imsglobal.org/caliper/v1/Frame',
        'MEDIA_OBJECT': 'http://purl.imsglobal.org/caliper/v1/MediaObject',
        'READING': 'http://www.idpf.org/epub/vocab/structure',
        'WEB_PAGE': 'http://purl.imsglobal.org/caliper/v1/WebPage',
        }
        
    def __init__(self,
            alignedLearningObjective = None,
            keyword = None,
            objectType = None,
            partOf = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['DIGITAL_RESOURCE'])
        
        if isinstance(alignedLearningObjective, collections.MutableSequence):
            if all( isinstance(item, LearningObjective) for item in alignedLearningObjective ):
                self._set_list_prop('alignedLearningObjective', alignedLearningObjective)
            else:
                raise TypeError('alignedLearningObjective must be a list of LearningObjectives')
        else:
            self._set_list_prop('alignedLearningObjective', None)

        if isinstance(keyword, collections.MutableSequence):
            if all( isinstance(item, six.string_types) for item in keyword):
                self._set_list_prop('keyword', keyword)
            else:
                raise TypeError('keyword must be a list of keyword strings')
        else:
            self._set_list_prop('keyword', None)

        if isinstance(objectType, collections.MutableSequence):
            if all( isinstance(item, six.string_types) for item in objectType ):
                self._set_list_prop('objectType', objectType)
            else:
                raise TypeError('keyword must be a list of keyword strings')
        else:
            self._set_list_prop('objectType', None)

        if partOf:
            if (isinstance(partOf, six.string_types)) and (rfc3987_parse(partOf, rule='URI')):
                self._set_str_prop('partOf', partOf)
            elif isinstance(partOf, CaliperSerializable):
                self._set_obj_prop('partOf', partOf)
            else:
                raise TypeError('partOf must implement CaliperSerializable or be an URL for a caliper entity')
        else:
            self._set_obj_prop('partOf', partOf)
            
    @property
    def alignedLearningObjective(self):
        return self._get_prop('alignedLearningObjective')

    @property
    def keyword(self):
        return self._get_prop('keyword')

    @property
    def objectType(self):
        return self._get_prop('objecType')

    @property
    def partOf(self):
        return self._get_prop('partOf')

class View(Entity):

    def __init__(self,
            actor = None,
            duration = None,
            endedAtTime = 0,
            frame = None,
            startedAtTime = 0,
            **kwargs):
        Entity.__init__(self,**kwargs)
        self._set_str_prop('@type', Entity.Types['VIEW'])

        if actor and (not isinstance(actor, Agent)):
            raise TypeError('actor must implement Agent')
        else:
            self._set_obj_prop('actor', actor)

        self._set_str_prop('duration', duration)
        self._set_int_prop('endedAtTime', endedAtTime)

        if frame and (not isinstance(frame, Frame)):
            raise TypeError('frame must implement Frame')
        else:
            self._set_obj_prop('frame', frame)

        self._set_int_prop('startedAtTime', startedAtTime)

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
    def endedAtTime(self, new_endedAtTime):
        self._set_int_prop('endedAtTime', new_endedAtTime)

    @property
    def frame(self):
        return self._get_prop('frame')

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')
        
class Frame(DigitalResource):

    def __init__(self,
            index = 0,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['FRAME'])
        self._set_int_prop('index', index)

    @property
    def index(self):
        return self._get_prop('index')
    

class MediaObject(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['MEDIA_OBJECT'])

class Reading(DigitalResource):

    def __init__(self,
            educationalUse = None,
            learningResourceType = None,
            timeRequired = None,
            version = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['READING'])
        self._set_str_prop('educationalUse', educationalUse)
        self._set_str_prop('learningResourceType', learningResourceType)
        self._set_str_prop('timeRequired', timeRequired)
        self._set_str_prop('version', version)

    @property
    def educationalUse(self):
        return self._get_prop('educationalUse')

    @property
    def learningResourceType(self):
        return self._get_prop('learningResourceType')

    @property
    def timeRequired(self):
        return self._get_prop('timeRequired')

    @property
    def version(self):
        return self._get_prop('version')
                     
class WebPage(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['WEB_PAGE'])

class EpubChapter(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['EPUB_CHAPTER'])
    
class EpubPart(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['EPUB_PART'])

class EpubSubChapter(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['EPUB_SUB_CHAPTER'])

class EpubVolume(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['EPUB_VOLUME'])


## Annotation entities
class Annotation(Entity, schemadotorg.Thing):
    _types = {
        'ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/Annotation',
        'BOOKMARK_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/BookmarkAnnotation',
        'HIGHLIGHT_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/HighlightAnnotation',
        'SHARED_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/SharedAnnotation',
        'TAG_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/TagAnnotation',
        }

    def __init__(self,
            target = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._target = None
        self._set_str_prop('@type', Annotation.Types['ANNOTATION'])

        if target and (not isinstance(target, CaliperSerializable)):
            raise TypeError('target must implement CaliperSerializable')
        else:
            self._target = target

    @property
    def target(self):
        return self._target

            
class BookmarkAnnotation(Annotation):

    def __init__(self,
            bookmarkNotes = None,
            **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_str_prop('@type', Annotation.Types['BOOKMARK_ANNOTATION'])
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
        self._set_str_prop('@type', Annotation.Types['BOOKMARK_ANNOTATION'])

        if selection and (not isinstance(selection, TextPositionSelector)):
            raise TypeError ('selection must implement TextPositionSelector')
        else:
            self._set_obj_prop('selection', TextPositionSelector)
        
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
        self._set_str_prop('@type', Annotation.Types['SHARED_ANNOTATION'])

        if isinstance(withAgents, collections.MutableSequence):
            if all( isinstance(item, Agent) for item in withAgents):
                self._set_list_prop('withAgents', withAgents)
            else:
                raise TypeError('withAgents must be a list of objects that implement Agent')
        else:
            self._set_list_prop('withAgents', None)

    @property
    def withAgents(self):
        return self._get_prop('withAgents')

class TagAnnotation(Annotation):

    def __init__(self,
            tags = None,
            **kwargs):
        Annotation.__init__(self, **kwargs)
        self._set_str_prop('@type', Annotation.Types['TAG_ANNOTATION'])

        if isinstance(tags, collections.MutableSequence):
            if all( isinstance(item, six.string_types) for item in tags):
                self._set_list_prop('tags', tags)
            else:
                raise TypeError('tags must be a list of strings')
        else:
            self._set_list_prop('tags', None)
        
class TextPositionSelector(CaliperSerializable):

    def __init__(self,
            start = None,
            end = None):
        CaliperSerializable.__init__(self)

        self._set_str_prop('end', end)
        self._set_str_prop('start', start)

    @property
    def end(self):
        return self._get_prop('end')
    @end.setter
    def end(self, new_end):
        self._set_str_prop('end', new_end)

    @property
    def start(self):
        return self._get_prop('start')
    @start.setter
    def start(self, new_start):
        self._set_str_prop('start', new_start)

## Assignable entities
class Assignable(CaliperSerializable):

    @property
    def dateCreated(self):
        return self._get_prop('dateCreated')

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
                 
class Attempt(Entity):

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
            assignable = None,
            actor = None,
            count = None,
            duration = None,
            endedAtTime = 0,
            startedAtTime = 0,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['ATTEMPT'])
        self._assignable = self._actor = None

        if assignable and (not isinstance(assignable, Assignable)):
            raise TypeError('assignable must implement Assignable')
        else:
            self._assignable = None

        if actor and (not isinstance(actor, Agent)):
            raise TypeError('agent must implement Agent')
        else:
            self._actor = None

        self._set_int_prop('count', count)
        self._set_str_prop('duration', duration) ## should we armour this with a regex?
        self._set_int_prop('endedAtTime', endedAtTime)
        self._set_int_prop('startedAtTime', startedAtTime)
            
    @property
    def assignable(self):
        return self._assignable

    @property
    def actor(self):
        return self._actor

    @property
    def count(self):
        return self._get_prop('count')

    @property
    def duration(self):
        return self._get_prop('duration')
    @duration.setter
    def duration(self, new_duration):
        self._set_str_prop('duration', duration) ## should we armour this with a regex?

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')
    @endedAtTime.setter
    def endedAtTime(self,new_time):
        self._set_int_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')

## Assessment entities
class AssignableDigitalResource(DigitalResource, Assignable):
    _types = {
        'ASSESSMENT': 'http://purl.imsglobal.org/caliper/v1/Assessment',
        'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/caliper/v1/AssessmentItem',
        }

    def __init__(self,
            dateCreated = 0,
            datePublished = 0,
            dateToActivate = 0,
            dateToShow = 0,
            dateToStartOn = 0,
            dateToSubmit = 0,
            maxAttempts = None,
            maxSubmits = None,
            maxScore = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['ASSIGNABLE_DIGITAL_RESOURCE'])

        self._set_int_prop('dateCreated', dateCreated)
        self._set_int_prop('datePublished', datePublished)
        self._set_int_prop('dateToActivate', dateToActivate)
        self._set_int_prop('dateToShow', dateToShow)
        self._set_int_prop('dateToStartOn', dateToStartOn)
        self._set_int_prop('dateToSubmit', dateToSubmit)
        self._set_int_prop('maxAttempts', maxAttempts)
        self._set_int_prop('maxSubmits', maxSubmits)
        self._set_float_prop('maxScore', maxScore)

    @property
    def maxScore(self):
        return self._get_prop('maxScore')
    
class Assessment(AssignableDigitalResource, qti.Assessment):

    def __init__(self,
            assessmentItems = None,
            **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', AssignableDigitalResource.Types['ASSESSMENT'])

        if isinstance(assessmentItems, collections.MutableSequence):
            if all( isinstance(item, AssessmentItem) for item in assessmentItems):
                self._set_list_prop('assessmentItems', assessmentItems)
            else:
                raise TypeError('assessmentItems must be a list of AssessmentItems')
        else:
            self._set_list_prop('assessmentItems', None)

    @property
    def assessmentItems(self):
        return self._get_prop('assessmentItems')

class AssessmentItem(AssignableDigitalResource, qti.AssessmentItem):

    def __init__(self, **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', AssignableDigitalResource.Types['ASSESSMENT_ITEM'])

## Media entities
class MediaLocation(Entity):

    def __init__(self,
            currentTime = None,
            entity_id = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['MEDIA_LOCATION'])
        ## Is it sufficient just to generate a random UUID here? Or does there
        ## need to be some specific value (as there seems to be in the Java client)??
        self._uuid = uuid.uuid4()
        if not entity_id:
            self._set_str_prop('@id', '{0}/{1}'.format(
                self._get_prop('@type'),
                self._uuid
                ))
        else:
            self._set_str_prop('@id', entity_id)
        self._set_int_prop('currentTime', currentTime)

    @property
    def currentTime(self):
        return self._get_prop('currentTime')


        
class MediaObject(DigitalResource, schemadotorg.MediaObject):
    _types = {
        'AUDIO_OBJECT': 'http://purl.imsglobal.org/caliper/v1/AudioObject',
        'IMAGE_OBJECT': 'http://purl.imsglobal.org/caliper/v1/ImageObject',
        'VIDEO_OBJECT': 'http://purl.imsglobal.org/caliper/v1/VideoObject',
        }

    def __init__(self,
            duration = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['MEDIA_OBJECT'])
        self._set_int_prop('duration', duration) ## Is this the same as an Attempt duration?

    @property
    def duration(self):
        return self._get_prop('duration')

class AudioObject(MediaObject, schemadotorg.AudioObject):

    def __init__(self,
            muted = None,
            volumeLevel = None,
            volumeMax = None,
            volumeMin = None,
            **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_str_prop('@type', MediaObject.Types['AUDIO_OBJECT'])
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
        self._set_str_prop('@type', MediaObject.Types['IMAGE_OBJECT'])

class VideoObject(MediaObject, schemadotorg.VideoObject):

    def __init__(self, **kwargs):
        MediaObject.__init__(self, **kwargs)
        self._set_str_prop('@type', MediaObject.Types['VIDEO_OBJECT'])

## Outcome entities
class Outcome(CaliperSerializable):

    def __init__(self,
            attempt = None,
            result = None):
        CaliperSerializable.__init__(self)

        if attempt and (not isinstance(attempt, Attempt)):
            raise TypeError('attempt must implement Attempt')
        else:
            self._set_obj_prop('attmept', attempt)

        if result and (not isinstance(result, Result)):
            raise TypeError('result must implement Result')
        else:
            self._set_obj_prop('result', result)

    @property
    def attempt(self):
        return self._get_prop('attempt')
    @attempt.setter
    def attempt(self, new_attempt):
        if new_attempt and (not isinstance(new_attempt, Attempt)):
            raise TypeError('new_attempt must implement Attempt')
        else:
            self._set_obj_prop('attmept', new_attempt)
        
    @property
    def result(self):
        return self._get_prop('result')
    @result.setter
    def result(self, new_result):
        if new_result and (not isinstance(new_result, Result)):
            raise TypeError('new_result must implement Result')
        else:
            self._set_obj_prop('result', new_result)


class Result(Entity):

    def __init__(self,
            comment = None,
            curvedTotalScore = None,
            curveFactor = None,
            extraCreditScore = None,
            normalScore = None,
            penaltyScore = None,
            scoredBy = None,
            totalScore = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['RESULT'])

        self._set_str_prop('comment', comment)
        self._set_float_prop('curvedTotalScore', curvedTotalScore)
        self._set_float_prop('curveFactor', curveFactor)
        self._set_float_prop('extraCreditScore', extraCreditScore)
        self._set_float_prop('normalScore', normalScore)
        self._set_float_prop('penaltyScore', penaltyScore)

        if scoredBy and (not isinstance(scoredBy, Agent)):
            raise TypeError('scoredBy must implement Agent')
        else:
            self._set_obj_prop('scoredBy', scoredBy)
        
        self._set_float_prop('totalScore', totalScore)

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


