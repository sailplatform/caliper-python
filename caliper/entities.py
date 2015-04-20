# -*- coding: utf-8 -*-
# Caliper-python package, entities module
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

from __future__ import absolute_import


import collections
from rfc3987 import parse as rfc3987_parse
import six

from caliper.base import BaseEntity, CaliperSerializable, BaseRole, BaseStatus
from caliper.extern import foaf, schemadotorg, w3c

### Fundamental entities ###
## Base entity class
class Entity(BaseEntity, schemadotorg.Thing):

    _types = {
        'AGENT': 'http://purl.imsglobal.org/caliper/v1/Agent',
        'ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/Annotation',
        'ATTEMPT': 'http://purl.imsglobal.org/caliper/v1/Attempt',
        'COURSE_OFFERING': 'http://purl.imsglobal.org/caliper/v1/lis/CourseOffering',        
        'COURSE_SECTION': 'http://purl.imsglobal.org/caliper/v1/lis/CourseSection',
        'DIGITAL_RESOURCE': 'http://purl.imsglobal.org/caliper/v1/DigitalResource',
        'ENTITY': 'http://purl.imsglobal.org/caliper/v1/Entity',
        'GENERATED': 'http://purl.imsglobal.org/caliper/v1/Generated',
        'GROUP': 'http://purl.imsglobal.org/caliper/v1/lis/Group',
        'LEARNING_OBJECTIVE': 'http://purl.imsglobal.org/caliper/v1/LearningObjective',
        'MEDIA_OBJECT': 'http://purl.imsglobal.org/caliper/v1/MediaObject',
        'MEMBERSHIP': 'http://purl.imsglobal.org/caliper/v1/lis/Membership',
        'ORGANIZATION': 'http://purl.imsglobal.org/caliper/v1/w3c/Organization',
        'PERSON': 'http://purl.imsglobal.org/caliper/v1/lis/Person',
        'RESPONSE': 'http://purl.imsglobal.org/caliper/v1/Response',
        'RESULT': 'http://purl.imsglobal.org/caliper/v1/Result',
        'SESSION': 'http://purl.imsglobal.org/caliper/v1/Session',
        'SOFTWARE_APPLICATION': 'http://purl.imsglobal.org/caliper/v1/SoftwareApplication',
        'TARGET': 'http://purl.imsglobal.org/caliper/v1/Target',
        'VIEW': 'http://purl.imsglobal.org/caliper/v1/View',
        }

    def __init__(self,
            entity_id = None,
            dateCreated = None,
            dateModified = None,
            description = None,
            name = None,
            extensions = {},
            **kwargs):
        BaseEntity.__init__(self, **kwargs)

        if not entity_id:
            raise ValueError('Entity must have an ID.')
        else:
            self._set_str_prop('@id', entity_id)
            
        self._set_str_prop('@type', Entity.Types['ENTITY'])
        self._set_str_prop('dateCreated', dateCreated)
        self._set_str_prop('dateModified', dateModified)
        self._set_str_prop('description', description)
        self._set_str_prop('name', name)
        self._set_obj_prop('extensions', extensions)

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
class Assignable(CaliperSerializable):

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

class Generatable(CaliperSerializable):
    pass

class Targetable(CaliperSerializable):
    pass

    
### Derived entities ###

## Membership entities

class Role(BaseRole, w3c.Role):
    _roles = {
        'LEARNER': 'http://purl.imsglobal.org/vocab/lis/v2/membership#Learner',
        'EXTERNAL_LEARNER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Learner#ExternalLearner',
        'GUEST_LEARNER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Learner#GuestLearner',
        'LEARNER_INSTRUCTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Learner#Instructor',
        'LEARNER_LEARNER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Learner#Learner',
        'NONCREDIT_LEARNER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Learner#NonCreditLearner',
        'INSTRUCTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor',
        'EXTERNAL_INSTRUCTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Instructor#ExternalInstructor',
        'GUEST_INSTRUCTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Instructor#GuestInstructor',
        'LECTURER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Instructor#Lecturer',
        'PRIMARY_INSTRUCTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Instructor#PrimaryInstructor',
        'ADMINISTRATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator',
        'ADMINISTRATOR_ADMINISTRATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#Administrator',
        'ADMINISTRATOR_DEVELOPER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#Developer',
        'ADMINISTRATOR_SUPPORT': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#Support',
        'ADMINISTRATOR_SYSTEM_ADMINISTRATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#SystemAdministrator',
        'ADMINISTRATOR_EXTERNAL_DEVELOPER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#ExternalSupport',
        'ADMINISTRATOR_EXTERNAL_SUPPORT': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#ExternalDeveloper',
        'ADMINISTRATOR_EXTERNAL_SYSTEM_ADMINISTRATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Administrator#ExternalSystemAdministrator',
        'CONTENT_DEVELOPER': 'http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper',
        'CONTENT_DEVELOPER_CONTENT_DEVELOPER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/ContentDeveloper#ContentDeveloper',
        'CONTENT_DEVELOPER_LIBRARIAN': 'http://purl.imsglobal.org/vocab/lis/v2/membership/ContentDeveloper#Librarian',
        'CONTENT_DEVELOPER_CONTENT_EXPERT': 'http://purl.imsglobal.org/vocab/lis/v2/membership/ContentDeveloper#ContentExpert',
        'CONTENT_DEVELOPER_EXTERNAL_CONTENT_EXPERT': 'http://purl.imsglobal.org/vocab/lis/v2/membership/ContentDeveloper#ExternalContentExpert',
        'MANAGER': 'http://purl.imsglobal.org/vocab/lis/v2/membership#Manager',
        'MANAGER_AREA_MANAGER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Manager#AreaManager',
        'MANAGER_COURSE_COORDINATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Manager#CourseCoordinator',
        'MANAGER_OBSERVER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Manager#Observer',
        'MANAGER_EXTERNAL_OBSERVER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Manager#ExternalObserver',
        'MEMBER': 'http://purl.imsglobal.org/vocab/lis/v2/membership#Member',
        'MEMBER_MEMBER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Member#Member',
        'MENTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership#Mentor',
        'MENTOR_MENTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#Mentor',
        'MENTOR_ADVISOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#Advisor',
        'MENTOR_AUDITOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#Auditor',
        'MENTOR_REVIEWER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#Reviewer',
        'MENTOR_TUTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#Tutor',
        'MENTOR_LEARNING_FACILITATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#LearningFacilitator',
        'MENTOR_EXTERNAL_MENTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#ExternalMentor',
        'MENTOR_EXTERNAL_ADVISOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#ExternalAdvisor',
        'MENTOR_EXTERNAL_AUDITOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#ExternalAuditor',
        'MENTOR_EXTERNAL_REVIEWER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#ExternalReviewer',
        'MENTOR_EXTERNAL_TUTOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor#ExternalTutor',
        'MENTOR_EXTERNAL_LEARNING_FACILITATOR': 'http://purl.imsglobal.org/vocab/lis/v2/membership/Mentor/ExternalLearningFacilitator',
        'TEACHING_ASSISTANT': 'http://purl.imsglobal.org/vocab/lis/v2/membership#TeachingAssistant',
        'TEACHING_ASSISTANT_TEACHING_ASSISTANT': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#TeachingAssistant',
        'TEACHING_ASSISTANT_GRADER': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#Grader',
        'TEACHING_ASSISTANT_TEACHING_ASSISTANT_SECTION': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#TeachingAssistantSection',
        'TEACHING_ASSISTANT_TEACHING_ASSISTANT_SECTION_ASSOCIATION': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#TeachingAssistantSectionAssociation',
        'TEACHING_ASSISTANT_TEACHING_ASSISTANT_OFFERING': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#TeachingAssistantOffering',
        'TEACHING_ASSISTANT_TEACHING_ASSISTANT_TEMPLATE': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#TeachingAssistantTemplate',
        'TEACHING_ASSISTANT_TEACHING_ASSISTANT_GROUP': 'http://purl.imsglobal.org/vocab/lis/v2/membership/TeachingAssistant#TeachingAssistantGroup',
        }

class Status(BaseStatus, w3c.Status):
    _statuses = {
        'ACTIVE': 'http://purl.imsglobal.org/vocab/lis/v2/status#Active',
        'DELETED': 'http://purl.imsglobal.org/vocab/lis/v2/status#Deleted',
        'INACTIVE': 'http://purl.imsglobal.org/vocab/lis/v2/status#Inactive',
        }

class Membership(Entity, w3c.Membership):

    def __init__(self,
                 member_id = None,
                 organization_id = None,
                 roles = None,
                 status = None,
                 **kwargs):
        Entity.__init__(self,**kwargs)
        self._set_str_prop('@type', Entity.Types['MEMBERSHIP'])
        self._set_str_prop('member', member_id)
        self._set_str_prop('organization', organization_id)

        if roles and isinstance(roles, collections.MutableSequence):
            if set(roles).issubset(set(Role.Roles.values())):
                self._set_list_prop('roles', roles)
            else:
                raise TypeError('roles must be in the list of valid Role values')
        elif roles:
            raise TypeError('roles must be a list of valid Roles values')
        else:
            self._set_list_prop('roles', None)

        if status not in Status.Statuses.values():
            raise ValueError('status must be in the list of valid Status values')
        else:
            self._set_str_prop('status', status)

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

    def __init__(self,
                 membership = None,
                 **kwargs):
        Entity.__init__(self,**kwargs)
        self._set_str_prop('@type', Entity.Types['AGENT'])

        if membership and isinstance(membership, collections.MutableSequence):
            if all( isinstance(item, Membership) for item in membership ):
                self._set_list_prop('hasMembership', membership)
            else:
                raise TypeError('membership must be a list of Memberships')
        else:
            self._set_list_prop('hasMembership', membership)

    @property
    def membership(self):
        return self._get_prop('hasMembership')

class SoftwareApplication(Agent, schemadotorg.SoftwareApplication):

    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['SOFTWARE_APPLICATION'])

class Person(Agent):

    def __init__(self, **kwargs):
        Agent.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['PERSON'])

## Organization entities
class Organization(Entity, w3c.Organization):
    _types = {
        }

    def __init__(self,
                 membership = None,
                 subOrganizationOf = None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['ORGANIZATION'])

        if membership and isinstance(membership, collections.MutableSequence):
            if all( isinstance(item, Membership) for item in membership ):
                self._set_list_prop('membership', membership)
            else:
                raise TypeError('membership must be a list of Memberships')
        elif membership:
            raise TypeError('membership must be a list of Memberships')
        else:
            self._set_list_prop('membership', None)

        if subOrganizationOf and (not isinstance(subOrganizationOf, w3c.Organization)):
            raise TypeError('subOrganizationOf must implement w3c.Organization')
        else:
            self._set_obj_prop('subOrganizationOf', subOrganizationOf)

    @property
    def membership(self):
        return self._get_prop('membership')

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
        self._set_str_prop('@type', Entity.Types['COURSE_OFFERING'])
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
        self._set_str_prop('@type', Entity.Types['COURSE_SECTION'])
        self._set_str_prop('category', category)

    @property
    def category(self):
        return self._get_prop('category')

class Group(Organization):

    def __init__(self, **kwargs):
        Organization.__init__(self,**kwargs)
        self._set_str_prop('@type', Entity.Types['GROUP'])


## Learning Context
class LearningContext(CaliperSerializable):

    def __init__(self,
                 agent = None,
                 edApp = None,
                 group = None):

        CaliperSerializable.__init__(self)

        if not isinstance(agent, Agent):
            raise TypeError('agent must implement Agent')
        else:
            self._set_obj_prop('agent', agent)

        if edApp and (not isinstance(edApp, SoftwareApplication)):
            raise TypeError('edApp must implement SoftwareApplication')
        else:
            self._set_obj_prop('edApp', edApp)

        if group and (not isinstance(group, Organization)):
            raise TypeError('group must implement Organization')
        else:
            self._set_obj_prop('group', group)
            
    @property
    def agent(self):
        return self._get_prop('agent')

    @property
    def edApp(self):
        return self._get_prop('edApp')

    @property
    def group(self):
        return self._get_prop('group')


## Learning objective
class LearningObjective(Entity):

    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['LEARNING_OBJECTIVE'])

    
## Creative works
class DigitalResource(Entity, schemadotorg.CreativeWork, Targetable):

    _types = {
        'ASSIGNABLE_DIGITAL_RESOURCE': 'http://purl.imsglobal.org/caliper/v1/AssignableDigitalResource',
        'EPUB_CHAPTER': 'http://www.idpf.org/epub/vocab/structure/#chapter',
        'EPUB_PART': 'http://www.idpf.org/epub/vocab/structure/#part',
        'EPUB_SUB_CHAPTER': 'http://www.idpf.org/epub/vocab/structure/#subchapter',
        'EPUB_VOLUME': 'http://www.idpf.org/epub/vocab/structure/#volume',
        'FRAME': 'http://purl.imsglobal.org/caliper/v1/Frame',
        'READING': 'http://www.idpf.org/epub/vocab/structure',
        'WEB_PAGE': 'http://purl.imsglobal.org/caliper/v1/WebPage',
        }
        
    def __init__(self,
            alignedLearningObjective = None,
            datePublished = None,
            isPartOf = None,
            keywords = None,
            objectType = None,
            version = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['DIGITAL_RESOURCE'])
        
        if alignedLearningObjective and isinstance(alignedLearningObjective, collections.MutableSequence):
            if all( isinstance(item, LearningObjective) for item in alignedLearningObjective ):
                self._set_list_prop('alignedLearningObjective', alignedLearningObjective)
            else:
                raise TypeError('alignedLearningObjective must be a list of LearningObjectives')                
        elif alignedLearningObjective:
                raise TypeError('alignedLearningObjective must be a list of LearningObjectives')
        else:
            self._set_list_prop('alignedLearningObjective', None)

        self._set_str_prop('datePublished', datePublished)

        if isPartOf and (not isinstance(isPartOf, schemadotorg.CreativeWork)):
            raise TypeError('isPartOf must implement schemadotorg.CreativeWork')
        else:
            self._set_id_prop('isPartOf', isPartOf)

        if isinstance(keywords, collections.MutableSequence):
            if all( isinstance(item, six.string_types) for item in keywords):
                self._set_list_prop('keywords', keywords)
            else:
                raise TypeError('keywords must be a list of keyword strings')
        else:
            self._set_list_prop('keywords', None)

        if isinstance(objectType, collections.MutableSequence):
            if all( isinstance(item, six.string_types) for item in objectType ):
                self._set_list_prop('objectType', objectType)
            else:
                raise TypeError('objectType must be a list of object type strings')
        else:
            self._set_list_prop('objectType', None)

        self._set_str_prop('version', version)

            
    @property
    def alignedLearningObjective(self):
        return self._get_prop('alignedLearningObjective')

    @property
    def datePublished(self):
        return self._get_prop('datePublished')

    @property
    def isPartOf(self):
        return self._get_object('isPartOf')
    @isPartOf.setter
    def isPartOf(self, new_object):
        if new_object and (not isinstance(new_object, schemadotorg.CreativeWork)):
            raise TypeError('new object must implement schemadotorg.CreativeWork')
        else:
            self._set_id_prop('isPartOf', new_object)

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
        self._set_str_prop('@type', DigitalResource.Types['FRAME'])
        self._set_int_prop('index', index)

    @property
    def index(self):
        return self._get_prop('index')
    
class Reading(DigitalResource):

    def __init__(self, **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', DigitalResource.Types['READING'])
                     
class WebPage(DigitalResource, schemadotorg.WebPage):

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
class Annotation(Entity, Generatable):
    _types = {
        'BOOKMARK_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/BookmarkAnnotation',
        'HIGHLIGHT_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/HighlightAnnotation',
        'SHARED_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/SharedAnnotation',
        'TAG_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/TagAnnotation',
        }

    def __init__(self,
            annotated = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['ANNOTATION'])

        if annotated and (not isinstance(annotated, DigitalResource)):
            raise TypeError('annotated must implement DigitalResource')
        else:
            self._set_id_prop('annotated', annotated)

    @property
    def annotated(self):
        return self._get_object('annotated')

    @property
    def annotated_id(self):
        return self._get_prop('annotated')
    
            
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
        self._set_str_prop('@type', Annotation.Types['HIGHLIGHT_ANNOTATION'])

        if selection and (not isinstance(selection, TextPositionSelector)):
            raise TypeError ('selection must implement TextPositionSelector')
        else:
            self._set_obj_prop('selection', selection)
        
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
            if all( isinstance(item, foaf.Agent) for item in withAgents):
                self._set_list_prop('withAgents', withAgents)
            else:
                raise TypeError('withAgents must be a list of objects that implement foaf.Agent')
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

        if not isinstance(end, six.string_types):
            raise ValueError('must provide an end string value')
        else:
            self._set_str_prop('end', end)

        if not isinstance(start, six.string_types):
            raise ValueError('must provide a start string value')
        else:
            self._set_str_prop('start', start)

    @property
    def end(self):
        return self._get_prop('end')
    @end.setter
    def end(self, new_end):
        if not isinstance(new_end, six.string_types):
            raise ValueError('must provide a new end string value')
        else:
            self._set_str_prop('end', new_end)

    @property
    def start(self):
        return self._get_prop('start')
    @start.setter
    def start(self, new_start):
        if not isinstance(new_start, six.string_types):
            raise ValueError('must provide a new start string value')
        else:
            self._set_str_prop('start', new_start)


## Generatable entities
                 
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
            assignable = None,
            actor = None,
            count = None,
            duration = None,
            endedAtTime =None,
            startedAtTime = None,
            **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['ATTEMPT'])

        if actor and (not isinstance(actor, Agent)):
            raise TypeError('actor must implement Agent')
        else:
            self._set_id_prop('actor', actor)
        
        if assignable and (not isinstance(assignable, DigitalResource)):
            raise TypeError('assignable must implement DigitalResource')
        else:
            self._set_id_prop('assignable', assignable)
        
        self._set_int_prop('count', count)
        self._set_str_prop('duration', duration) ## should we armour this with a regex?
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_str_prop('startedAtTime', startedAtTime)
            
    @property
    def assignable(self):
        return self._get_object('assignable')

    @property
    def assignable_id(self):
        return self._get_prop('assignable')

    @property
    def actor(self):
        return self._get_object('actor')

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
        self._set_str_prop('duration', new_duration) ## should we armour this with a regex?

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
    _types = {
        # 'DRAGOBJECT': 'http://purl.imsglobal.org/caliper/v1/Response/DragObject',
        # 'ESSAY': 'http://purl.imsglobal.org/caliper/v1/Response/Essay',
        # 'HOTSPOT': 'http://purl.imsglobal.org/caliper/v1/Response/HotSpot',
        'FILLINBLANK': 'http://purl.imsglobal.org/caliper/v1/Response/FillinBlank',
        'MULTIPLECHOICE': 'http://purl.imsglobal.org/caliper/v1/Response/MultipleChoice',
        'MULTIPLERESPONSE': 'http://purl.imsglobal.org/caliper/v1/Response/MultipleResponse',
        'SELECTTEXT': 'http://purl.imsglobal.org/caliper/v1/Response/SelectText',
        # 'SHORTANSWER': 'http://purl.imsglobal.org/caliper/v1/Response/ShortAnswer',
        # 'SLIDER': 'http://purl.imsglobal.org/caliper/v1/Response/Slider',
        'TRUEFALSE': 'http://purl.imsglobal.org/caliper/v1/Response/TrueFalse'
        }

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
        self._set_str_prop('@type', Entity.Types['RESPONSE'])

        if actor and (not isinstance(actor, Agent)):
            raise TypeError('actor must implement Agent')
        else:
            self._set_id_prop('actor', actor)
        
        if assignable and (not isinstance(assignable, DigitalResource)):
            raise TypeError('assignable must implement DigitalResource')
        else:
            self._set_id_prop('assignable', assignable)
        
        if attempt and not( isinstance(attempt, Attempt)):
            raise TypeError('attempt must implement Attempt')
        else:
            self._set_list_prop('attempt', attempt)
        
        self._set_str_prop('duration', duration) ## should we armour this with a regex?
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_str_prop('startedAtTime', startedAtTime)
        self._set_str_prop('values', values)

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
        self._set_str_prop('duration', new_duration) ## should we armour this with a regex?

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


## Assessment entities
class AssignableDigitalResource(DigitalResource, Assignable):
    _types = {
        'ASSESSMENT': 'http://purl.imsglobal.org/caliper/v1/Assessment',
        'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/caliper/v1/AssessmentItem',
        }

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
        self._set_str_prop('@type', DigitalResource.Types['ASSIGNABLE_DIGITAL_RESOURCE'])
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
    @assessmentItems.setter
    def assessmentItems(self, new_items):
        if isinstance(new_items, collections.MutableSequence):
            if all( isinstance(item, AssessmentItem) for item in new_items):
                self._set_list_prop('assessmentItems', new_items)
            else:
                raise TypeError('new items must be a list of AssessmentItems')
        else:
            self._set_list_prop('assessmentItems', None)
        

class AssessmentItem(AssignableDigitalResource):

    def __init__(self,
                 isTimeDependent = False,
                 **kwargs):
        AssignableDigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', AssignableDigitalResource.Types['ASSESSMENT_ITEM'])
        self._set_bool_prop('isTimeDependent', isTimeDependent)

    @property
    def isTimeDependent(self):
        return self._get_prop('isTimeDependent')


## Media entities
    
class MediaObject(DigitalResource, schemadotorg.MediaObject):
    _types = {
        'AUDIO_OBJECT': 'http://purl.imsglobal.org/caliper/v1/AudioObject',
        'IMAGE_OBJECT': 'http://purl.imsglobal.org/caliper/v1/ImageObject',
        'VIDEO_OBJECT': 'http://purl.imsglobal.org/caliper/v1/VideoObject',
        'MEDIA_LOCATION': 'http://purl.imsglobal.org/caliper/v1/MediaLocation',
        }

    def __init__(self,
            duration = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['MEDIA_OBJECT'])
        self._set_int_prop('duration', duration) ## Is this the same as an Attempt duration?

    @property
    def duration(self):
        return self._get_prop('duration')

class MediaLocation(DigitalResource, Targetable):

    def __init__(self,
            currentTime = None,
            **kwargs):
        DigitalResource.__init__(self, **kwargs)
        self._set_str_prop('@type', MediaObject.Types['MEDIA_LOCATION'])
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
        self._set_str_prop('@type', Entity.Types['RESULT'])

        if actor and (not isinstance(actor, Agent)):
            raise TypeError('actor must implement Agent')
        else:
            self._set_id_prop('actor', actor)
        
        if assignable and (not isinstance(assignable, DigitalResource)):
            raise TypeError('assignable must implement DigitalResource')
        else:
            self._set_id_prop('assignable', assignable)
        
        self._set_str_prop('comment', comment)
        self._set_float_prop('curvedTotalScore', curvedTotalScore)
        self._set_float_prop('curveFactor', curveFactor)
        self._set_float_prop('extraCreditScore', extraCreditScore)
        self._set_float_prop('normalScore', normalScore)
        self._set_float_prop('penaltyScore', penaltyScore)

        if scoredBy and (not isinstance(scoredBy, foaf.Agent)):
            raise TypeError('scoredBy must implement foaf.Agent')
        else:
            self._set_obj_prop('scoredBy', scoredBy)
        
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

## Response entities
class FillinBlankResponse(Response):

    def __init__(self,
                 values = None,
                 **kwargs):
        Response.__init__(self,**kwargs)

        self._set_str_prop('@type', Response.Types['FILLINBLANK'])

        if values and isinstance(values, collections.MutableSequence):
          if all( isinstance(item, six.string_types) for item in values):
            self._set_list_prop('values', values)
          else:
            raise TypeError('values must be a list of strings')
        else:
          self._set_list_prop('values', None)

class MultipleChoiceResponse(Response):

    def __init__(self,
                 values = None,
                 **kwargs):
        Response.__init__(self,**kwargs)

        self._set_str_prop('@type', Response.Types['MULTIPLECHOICE'])

class MultipleResponseResponse(Response):

    def __init__(self,
                 values = None,
                 **kwargs):
        Response.__init__(self,**kwargs)

        self._set_str_prop('@type', Response.Types['MULTIPLERESPONSE'])

        if values and isinstance(values, collections.MutableSequence):
          if all( isinstance(item, six.string_types) for item in values):
            self._set_list_prop('values', values)
          else:
            raise TypeError('values must be alist of strings')
        else:
          self._set_list_prop('values', None)

class SelectTextResponse(Response):

    def __init__(self,
                 values = None,
                 **kwargs):
        Response.__init__(self,**kwargs)

        self._set_str_prop('@type', Response.Types['SELECTTEXT'])

        if values and isinstance(values, collections.MutableSequence):
          if all( isinstance(item, six.string_types) for item in values):
            self._set_list_prop('values', values)
          else:
            raise TypeError('values must be alist of strings')
        else:
          self._set_list_prop('values', None)

class TrueFalseResponse(Response):

    def __init__(self,
                 values = None,
                 **kwargs):
        Response.__init__(self,**kwargs)

        self._set_str_prop('@type', Response.Types['TRUEFALSE'])


## Session entities
class Session(Entity, Generatable, Targetable):

    def __init__(self,
                 actor = None,
                 duration = None,
                 endedAtTime = None,
                 startedAtTime = None,
                 **kwargs):
        Entity.__init__(self, **kwargs)
        self._set_str_prop('@type', Entity.Types['SESSION'])

        if not isinstance(actor, foaf.Agent):
            raise TypeError('actor must implement foaf.Agent')
        else:
            self._set_obj_prop('actor', actor)

        self._set_str_prop('duration', duration) ## should we armour this with a regex?
        self._set_str_prop('endedAtTime', endedAtTime)
        self._set_str_prop('startedAtTime', startedAtTime)

    @property
    def actor(self):
        return self._actor

    @property
    def duration(self):
        return self._get_prop('duration')
    @duration.setter
    def duration(self, new_duration):
        self._set_str_prop('duration', new_duration) ## should we armour this with a regex?

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')
    @endedAtTime.setter
    def endedAtTime(self,new_time):
        self._set_str_prop('endedAtTime', new_time)

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')
