# -*- coding: utf-8 -*-
# Caliper-python package, constants module
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

# The line lengths in this file are long, but it's more legible as is
# yapf: disable

## Caliper constants
ENTITY_CONTEXTS = {
    'AGENT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ASSESSMENT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ASSIGNABLE_DIGITAL_RESOURCE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ATTEMPT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'AUDIO_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'BOOKMARK_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'CHAPTER': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'COLLECTION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'COURSE_OFFERING': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'COURSE_SECTION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'DIGITAL_RESOURCE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'DIGITAL_RESOURCE_COLLECTION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'DOCUMENT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ENTITY': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'EPUB_CHAPTER': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'EPUB_PART': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'EPUB_SUB_CHAPTER': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'EPUB_VOLUME': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'FILLINBLANK': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'FORUM': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'FRAME': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'GROUP': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'HIGHLIGHT_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'IMAGE_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'LEARNING_OBJECTIVE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'LTI_SESSION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MEDIA_LOCATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MEDIA_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MEMBERSHIP': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MESSAGE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MULTIPLECHOICE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MULTIPLERESPONSE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ORGANIZATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'PAGE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'PERSON': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'READING': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'RESPONSE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'RESULT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'SELECTTEXT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'SESSION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'SHARED_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'SOFTWARE_APPLICATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'TAG_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'TEXT_POSITION_SELECTOR': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'THREAD': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'TRUEFALSE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'VIDEO_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'VIEW': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'WEB_PAGE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context'
}

ENTITY_TYPES = {
    'AGENT': 'Agent',
    'ANNOTATION': 'Annotation',
    'ASSESSMENT': 'Assessment',
    'ASSESSMENT_ITEM': 'AssessmentItem',
    'ASSIGNABLE_DIGITAL_RESOURCE': 'AssignableDigitalResource',
    'ATTEMPT': 'Attempt',
    'AUDIO_OBJECT': 'AudioObject',
    'BOOKMARK_ANNOTATION': 'BookmarkAnnotation',
    'CHAPTER': 'Chapter',
    'COLLECTION': 'Collection',
    'COURSE_OFFERING': 'CourseOffering',
    'COURSE_SECTION': 'CourseSection',
    'DIGITAL_RESOURCE': 'DigitalResource',
    'DIGITAL_RESOURCE_COLLECTION': 'DigitalResourceCollection',
    'DOCUMENT': 'Document',
    'ENTITY': 'Entity',
    'EPUB_CHAPTER': 'http://purl.imsglobal/org/caliper/v1/EpubChapter',
    'EPUB_PART': 'EpubPart',
    'EPUB_SUB_CHAPTER': 'EpubSubChapter',
    'EPUB_VOLUME': 'EpubVolume',
    'FILLINBLANK': 'FillinBlankResponse',
    'FORUM': 'Forum',
    'FRAME': 'Frame',
    'GROUP': 'Group',
    'HIGHLIGHT_ANNOTATION': 'HighlightAnnotation',
    'IMAGE_OBJECT': 'ImageObject',
    'LEARNING_OBJECTIVE': 'LearningObjective',
    'LTI_SESSION': 'LtiSession',
    'MEDIA_LOCATION': 'MediaLocation',
    'MEDIA_OBJECT': 'MediaObject',
    'MEMBERSHIP': 'Membership',
    'MESSAGE': 'Message',
    'MULTIPLECHOICE': 'MultipleChoiceResponse',
    'MULTIPLERESPONSE': 'MultipleResponseResponse',
    'ORGANIZATION': 'Organization',
    'PAGE': 'Page',
    'PERSON': 'Person',
    'READING': 'Reading',
    'RESPONSE': 'Response',
    'RESULT': 'Result',
    'SELECTTEXT': 'SelectTextResponse',
    'SESSION': 'Session',
    'SHARED_ANNOTATION': 'SharedAnnotation',
    'SOFTWARE_APPLICATION': 'SoftwareApplication',
    'TAG_ANNOTATION': 'TagAnnotation',
    'TEXT_POSITION_SELECTOR': 'TextPositionSelector',
    'THREAD': 'Thread',
    'TRUEFALSE': 'TrueFalseResponse',
    'VIDEO_OBJECT': 'VideoObject',
    'VIEW': 'View',
    'WEB_PAGE': 'WebPage'
}

ENTITY_CLASSES = {
    ENTITY_TYPES['AGENT']: 'caliper.entities.Agent',
    ENTITY_TYPES['ANNOTATION']: 'caliper.entities.Annotation',
    ENTITY_TYPES['ASSESSMENT']: 'caliper.entities.Assessment',
    ENTITY_TYPES['ASSESSMENT_ITEM']: 'caliper.entities.AssessmentItem',
    ENTITY_TYPES['ASSIGNABLE_DIGITAL_RESOURCE']: 'caliper.entities.AssignableDigitalResource',
    ENTITY_TYPES['ATTEMPT']: 'caliper.entities.Attempt',
    ENTITY_TYPES['AUDIO_OBJECT']: 'caliper.entities.AudioObject',
    ENTITY_TYPES['BOOKMARK_ANNOTATION']: 'caliper.entities.BookmarkAnnotation',
    ENTITY_TYPES['CHAPTER']: 'caliper.entities.Chapter',
    ENTITY_TYPES['COLLECTION']: 'caliper.entities.Collection',
    ENTITY_TYPES['COURSE_OFFERING']: 'caliper.entities.CourseOffering',
    ENTITY_TYPES['COURSE_SECTION']: 'caliper.entities.CourseSection',
    ENTITY_TYPES['DIGITAL_RESOURCE']: 'caliper.entities.DigitalResource',
    ENTITY_TYPES['DIGITAL_RESOURCE_COLLECTION']: 'caliper.entities.DigitalResourceCollection',
    ENTITY_TYPES['DOCUMENT']: 'caliper.entities.Document',
    ENTITY_TYPES['ENTITY']: 'caliper.entities.Entity',
    ENTITY_TYPES['EPUB_CHAPTER']: 'caliper.entities.EpubChapter',
    ENTITY_TYPES['EPUB_PART']: 'caliper.entities.EpubPart',
    ENTITY_TYPES['EPUB_SUB_CHAPTER']: 'caliper.entities.EpubSubChapter',
    ENTITY_TYPES['EPUB_VOLUME']: 'caliper.entities.EpubVolume',
    ENTITY_TYPES['FILLINBLANK']: 'caliper.entities.FillinBlankResponse',
    ENTITY_TYPES['FORUM']: 'caliper.entities.Forum',
    ENTITY_TYPES['FRAME']: 'caliper.entities.Frame',
    ENTITY_TYPES['GROUP']: 'caliper.entities.Group',
    ENTITY_TYPES['HIGHLIGHT_ANNOTATION']: 'caliper.entities.HighlightAnnotation',
    ENTITY_TYPES['IMAGE_OBJECT']: 'caliper.entities.ImageObject',
    ENTITY_TYPES['LEARNING_OBJECTIVE']: 'caliper.entities.LearningObjective',
    ENTITY_TYPES['LTI_SESSION']: 'caliper.entities.LtiSession',
    ENTITY_TYPES['MEDIA_LOCATION']: 'caliper.entities.MediaLocation',
    ENTITY_TYPES['MEDIA_OBJECT']: 'caliper.entities.MediaObject',
    ENTITY_TYPES['MEMBERSHIP']: 'caliper.entities.Membership',
    ENTITY_TYPES['MESSAGE']: 'caliper.entities.Message',
    ENTITY_TYPES['MULTIPLECHOICE']: 'caliper.entities.MultipleChoiceResponse',
    ENTITY_TYPES['MULTIPLERESPONSE']: 'caliper.entities.MultipleResponseResponse',
    ENTITY_TYPES['ORGANIZATION']: 'caliper.entities.Organization',
    ENTITY_TYPES['PAGE']: 'caliper.entities.Page',
    ENTITY_TYPES['PERSON']: 'caliper.entities.Person',
    ENTITY_TYPES['READING']: 'caliper.entities.Reading',
    ENTITY_TYPES['RESPONSE']: 'caliper.entities.Response',
    ENTITY_TYPES['RESULT']: 'caliper.entities.Result',
    ENTITY_TYPES['SELECTTEXT']: 'caliper.entities.SelectTextResponse',
    ENTITY_TYPES['SESSION']: 'caliper.entities.Session',
    ENTITY_TYPES['SHARED_ANNOTATION']: 'caliper.entities.SharedAnnotation',
    ENTITY_TYPES['SOFTWARE_APPLICATION']: 'caliper.entities.SoftwareApplication',
    ENTITY_TYPES['TAG_ANNOTATION']: 'caliper.entities.TagAnnotation',
    ENTITY_TYPES['TEXT_POSITION_SELECTOR']: 'caliper.entities.TextPositionSelector',
    ENTITY_TYPES['THREAD']: 'caliper.entities.Thread',
    ENTITY_TYPES['TRUEFALSE']: 'caliper.entities.TrueFalseResponse',
    ENTITY_TYPES['VIDEO_OBJECT']: 'caliper.entities.VideoObject',
    ENTITY_TYPES['WEB_PAGE']: 'caliper.entities.WebPage'
}


EVENT_CONTEXTS = {
    'ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ASSESSMENT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'ASSIGNABLE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'EVENT': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'FORUM': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MEDIA': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'MESSAGE': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'NAVIGATION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'OUTCOME': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'SESSION': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'THREAD': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
    'VIEW': 'http://purl.imsglobal.org/ctx/caliper/v1p1/Context',
}

EVENT_TYPES = {
    'ANNOTATION': 'AnnotationEvent',
    'ASSESSMENT': 'AssessmentEvent',
    'ASSESSMENT_ITEM': 'AssessmentItemEvent',
    'ASSIGNABLE': 'AssignableEvent',
    'EVENT': 'Event',
    'FORUM': 'ForumEvent',
    'MEDIA': 'MediaEvent',
    'MESSAGE': 'MessageEvent',
    'NAVIGATION': 'NavigationEvent',
    'OUTCOME': 'OutcomeEvent',
    'SESSION': 'SessionEvent',
    'THREAD': 'ThreadEvent',
    'VIEW': 'ViewEvent',
}

EVENT_CLASSES = {
    EVENT_TYPES['ANNOTATION']: 'caliper.events.AnnotationEvent',
    EVENT_TYPES['ASSESSMENT']: 'caliper.events.AssessmentEvent',
    EVENT_TYPES['ASSESSMENT_ITEM']: 'caliper.events.AssessmentItemEvent',
    EVENT_TYPES['ASSIGNABLE']: 'caliper.events.AssignableEvent',
    EVENT_TYPES['EVENT']: 'caliper.events.Event',
    EVENT_TYPES['FORUM']: 'caliper.events.ForumEvent',
    EVENT_TYPES['MEDIA']: 'caliper.events.MediaEvent',
    EVENT_TYPES['MESSAGE']: 'caliper.events.MessageEvent',
    EVENT_TYPES['NAVIGATION']: 'caliper.events.NavigationEvent',
    EVENT_TYPES['OUTCOME']: 'caliper.events.OutcomeEvent',
    EVENT_TYPES['SESSION']: 'caliper.events.SessionEvent',
    EVENT_TYPES['THREAD']: 'caliper.events.ThreadEvent',
    EVENT_TYPES['VIEW']: 'caliper.events.ViewEvent',
}

CALIPER_CLASSES = {}
CALIPER_CLASSES.update(ENTITY_CLASSES)
CALIPER_CLASSES.update(EVENT_CLASSES)

CALIPER_CONTEXTS = {}
CALIPER_CONTEXTS.update(ENTITY_CONTEXTS)
CALIPER_CONTEXTS.update(EVENT_CONTEXTS)

CALIPER_TYPES = {}
CALIPER_TYPES.update(ENTITY_TYPES)
CALIPER_TYPES.update(EVENT_TYPES)

CALIPER_ROLES = {
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

CALIPER_STATUS = {
    'ACTIVE': 'http://purl.imsglobal.org/vocab/lis/v2/status#Active',
    'DELETED': 'http://purl.imsglobal.org/vocab/lis/v2/status#Deleted',
    'INACTIVE': 'http://purl.imsglobal.org/vocab/lis/v2/status#Inactive',
}


## Profiles
BASE_PROFILE_ACTIONS = {
    'ATTACHED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Attached',
    'CLASSIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Classified',
    'COMMENTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Commented',
    'DESCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Described',
    'DISLIKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Disliked',
    'IDENTIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Identified',
    'LIKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Liked',
    'LINKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Linked',
    'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
    'QUESTIONED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Questioned',
    'RANKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Ranked',
    'RECOMMENDED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Recommended',
    'REPLIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Replied',
    'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
}

CRUD_ACTIONS = {
    'CHANGED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Changed',
    'CREATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Created',
    'DELETED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Deleted',
    'MODIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Modified',
    'REMOVED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Removed',
    'RESET': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Reset',
    'RETRIEVED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Retrieved',
    'UPDATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Updated',
}

ANNOTATION_PROFILE_ACTIONS = {
    'BOOKMARKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Bookmarked',
    'HIGHLIGHTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Highlighted',
    'SHARED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Shared',
    'TAGGED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Tagged',
}

ASSESSMENT_PROFILE_ACTIONS = {
    'COMPLETED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Completed',
    'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
    'PAUSED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Paused',
    'RESTARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Restarted',
    'SKIPPED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Skipped',
    'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
    'SUBMITTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Submitted',
    'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
}

ASSIGNABLE_PROFILE_ACTIONS = {
    'ABANDONED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Abandoned',
    'ACTIVATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Activated',
    'COMPLETED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Completed',
    'DEACTIVATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Deactivated',
    'HID': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Hid',
    'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
    'REVIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Reviewed',
    'SHOWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Showed',
    'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
    'SUBMITTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Submitted',
    'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
}

FORUM_PROFILE_ACTIONS = {
    'MARKED_AS_READ': 'http://purl.imsglobal.org/vocab/caliper/v1/action#MarkedAsRead',
    'MARKED_AS_UNREAD': 'http://purl.imsglobal.org/vocab/caliper/v1/action#MarkedAsUnread',
    'POSTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Posted',
    'SUBSCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Subscribed',
    'UNSUBSCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Unsubscribed',
}

MEDIA_PROFILE_ACTIONS = {
    'CHANGED_RESOLUTION': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedResolution',
    'CHANGED_SIZE': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedSize',
    'CHANGED_SPEED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedSpeed',
    'CHANGED_VOLUME': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedVolume',
    'CLOSED_POPOUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ClosedPopout',
    'DISABLED_CLOSED_CAPTIONING': 'http://purl.imsglobal.org/vocab/caliper/v1/action#DisabledClosedCaptioning',
    'ENABLED_CLOSED_CAPTIONING': 'http://purl.imsglobal.org/vocab/caliper/v1/action#EnabledClosedCaptioning',
    'ENDED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Ended',
    'ENTERED_FULLSCREEN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#EnteredFullscreen',
    'EXITED_FULLSCREEN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ExitedFullscreen',
    'FORWARDED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ForwardedTo',
    'JUMPED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#JumpedTo',
    'MUTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Muted',
    'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
    'OPENED_POPOUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#OpenedPopout',
    'PAUSED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Paused',
    'RESUMED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Resumed',
    'REWOUND': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Rewound',
    'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
    'UNMUTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Unmuted',
    'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
}

NAVIGATION_ACTIONS = {
    'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
}

OUTCOME_PROFILE_ACTIONS = {
    'GRADED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Graded',
    'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
}

# Formalism only: navigation and view events verify their action against the base profile
READING_PROFILE_ACTIONS = {
    'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
    'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
}

SESSION_PROFILE_ACTIONS = {
    'LOGGED_IN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#LoggedIn',
    'LOGGED_OUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#LoggedOut',
    'TIMED_OUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#TimedOut',
}


CALIPER_ACTIONS = { }
CALIPER_ACTIONS.update(BASE_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(CRUD_ACTIONS)
CALIPER_ACTIONS.update(ANNOTATION_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(ASSESSMENT_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(ASSIGNABLE_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(FORUM_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(MEDIA_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(OUTCOME_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(READING_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(NAVIGATION_ACTIONS)
CALIPER_ACTIONS.update(SESSION_PROFILE_ACTIONS)
