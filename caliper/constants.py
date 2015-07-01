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


## Caliper constants
ENTITY_CONTEXTS = {
    'ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ASSESSMENT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ASSIGNABLE_DIGITAL_RESOURCE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ATTEMPT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'AUDIO_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'BOOKMARK_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'COURSE_OFFERING': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'COURSE_SECTION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'DIGITAL_RESOURCE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ENTITY': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'EPUB_CHAPTER': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'EPUB_PART': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'EPUB_SUB_CHAPTER': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'EPUB_VOLUME': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'FILLINBLANK': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'FRAME': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'GROUP': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'HIGHLIGHT_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'IMAGE_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'LEARNING_OBJECTIVE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'MEDIA_LOCATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'MEDIA_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'MEMBERSHIP': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'MULTIPLECHOICE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'MULTIPLERESPONSE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ORGANIZATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'PERSON': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'READING': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'RESPONSE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'RESULT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'SELECTTEXT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'SESSION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'SHARED_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'SOFTWARE_APPLICATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'TAG_ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'TRUEFALSE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'VIDEO_OBJECT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'VIEW': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'WEB_PAGE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context'}

ENTITY_TYPES = {
    'ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/Annotation',
    'ASSESSMENT': 'http://purl.imsglobal.org/caliper/v1/Assessment',
    'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/caliper/v1/AssessmentItem',
    'ASSIGNABLE_DIGITAL_RESOURCE': 'http://purl.imsglobal.org/caliper/v1/AssignableDigitalResource',
    'ATTEMPT': 'http://purl.imsglobal.org/caliper/v1/Attempt',
    'AUDIO_OBJECT': 'http://purl.imsglobal.org/caliper/v1/AudioObject',
    'BOOKMARK_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/BookmarkAnnotation',
    'COURSE_OFFERING': 'http://purl.imsglobal.org/caliper/v1/lis/CourseOffering',
    'COURSE_SECTION': 'http://purl.imsglobal.org/caliper/v1/lis/CourseSection',
    'DIGITAL_RESOURCE': 'http://purl.imsglobal.org/caliper/v1/DigitalResource',
    'ENTITY': 'http://purl.imsglobal.org/caliper/v1/Entity',
    'EPUB_CHAPTER': 'http://www.idpf.org/epub/vocab/structure/#chapter',
    'EPUB_PART': 'http://www.idpf.org/epub/vocab/structure/#part',
    'EPUB_SUB_CHAPTER': 'http://www.idpf.org/epub/vocab/structure/#subchapter',
    'EPUB_VOLUME': 'http://www.idpf.org/epub/vocab/structure/#volume',
    'FILLINBLANK': 'http://purl.imsglobal.org/caliper/v1/FillinBlankResponse',
    'FRAME': 'http://purl.imsglobal.org/caliper/v1/Frame',
    'GROUP': 'http://purl.imsglobal.org/caliper/v1/lis/Group',
    'HIGHLIGHT_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/HighlightAnnotation',
    'IMAGE_OBJECT': 'http://purl.imsglobal.org/caliper/v1/ImageObject',
    'LEARNING_OBJECTIVE': 'http://purl.imsglobal.org/caliper/v1/LearningObjective',
    'MEDIA_LOCATION': 'http://purl.imsglobal.org/caliper/v1/MediaLocation',
    'MEDIA_OBJECT': 'http://purl.imsglobal.org/caliper/v1/MediaObject',
    'MEMBERSHIP': 'http://purl.imsglobal.org/caliper/v1/lis/Membership',
    'MULTIPLECHOICE': 'http://purl.imsglobal.org/caliper/v1/MultipleChoiceResponse',
    'MULTIPLERESPONSE': 'http://purl.imsglobal.org/caliper/v1/MultipleResponseResponse',
    'ORGANIZATION': 'http://purl.imsglobal.org/caliper/v1/w3c/Organization',
    'PERSON': 'http://purl.imsglobal.org/caliper/v1/lis/Person',
    'READING': 'http://purl.imsglobal.org/caliper/v1/Reading',
    'RESPONSE': 'http://purl.imsglobal.org/caliper/v1/Response',
    'RESULT': 'http://purl.imsglobal.org/caliper/v1/Result',
    'SELECTTEXT': 'http://purl.imsglobal.org/caliper/v1/SelectTextResponse',
    'SESSION': 'http://purl.imsglobal.org/caliper/v1/Session',
    'SHARED_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/SharedAnnotation',
    'SOFTWARE_APPLICATION': 'http://purl.imsglobal.org/caliper/v1/SoftwareApplication',
    'TAG_ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/TagAnnotation',
    'TRUEFALSE': 'http://purl.imsglobal.org/caliper/v1/TrueFalseResponse',
    'VIDEO_OBJECT': 'http://purl.imsglobal.org/caliper/v1/VideoObject',
    'VIEW': 'http://purl.imsglobal.org/caliper/v1/View',
    'WEB_PAGE': 'http://purl.imsglobal.org/caliper/v1/WebPage'}

ENTITY_CLASSES = {
    ENTITY_TYPES['ANNOTATION']: 'caliper.entities.Annotation',
    ENTITY_TYPES['ASSESSMENT']: 'caliper.entities.Assessment',
    ENTITY_TYPES['ASSESSMENT_ITEM']: 'caliper.entities.AssessmentItem',
    ENTITY_TYPES['ASSIGNABLE_DIGITAL_RESOURCE']: 'caliper.entities.AssignableDigitalResource',
    ENTITY_TYPES['ATTEMPT']: 'caliper.entities.Attempt',
    ENTITY_TYPES['AUDIO_OBJECT']: 'caliper.entities.AudioObject',
    ENTITY_TYPES['BOOKMARK_ANNOTATION']: 'caliper.entities.BookmarkAnnotation',
    ENTITY_TYPES['COURSE_OFFERING']: 'caliper.entities.CourseOffering',
    ENTITY_TYPES['COURSE_SECTION']: 'caliper.entities.CourseSection',
    ENTITY_TYPES['DIGITAL_RESOURCE']: 'caliper.entities.DigitalResource',
    ENTITY_TYPES['ENTITY']: 'caliper.entities.Entity',
    ENTITY_TYPES['EPUB_CHAPTER']: 'caliper.entities.EpubChapter',
    ENTITY_TYPES['EPUB_PART']: 'caliper.entities.EpubPart',
    ENTITY_TYPES['EPUB_SUB_CHAPTER']: 'caliper.entities.EpubSubChapter',
    ENTITY_TYPES['EPUB_VOLUME']: 'caliper.entities.EpubVolume',
    ENTITY_TYPES['FILLINBLANK']: 'caliper.entities.FillinBlankResponse',
    ENTITY_TYPES['FRAME']: 'caliper.entities.Frame',
    ENTITY_TYPES['GROUP']: 'caliper.entities.Group',
    ENTITY_TYPES['HIGHLIGHT_ANNOTATION']: 'caliper.entities.HighlightAnnotation',
    ENTITY_TYPES['IMAGE_OBJECT']: 'caliper.entities.ImageObject',
    ENTITY_TYPES['LEARNING_OBJECTIVE']: 'caliper.entities.LearningObjective',
    ENTITY_TYPES['MEDIA_LOCATION']: 'caliper.entities.MediaLocation',
    ENTITY_TYPES['MEDIA_OBJECT']: 'caliper.entities.MediaObject',
    ENTITY_TYPES['MEMBERSHIP']: 'caliper.entities.Membership',
    ENTITY_TYPES['MULTIPLECHOICE']: 'caliper.entities.MultipleChoiceResponse',
    ENTITY_TYPES['MULTIPLERESPONSE']: 'caliper.entities.MultipleResponseResponse',
    ENTITY_TYPES['ORGANIZATION']: 'caliper.entities.Organization',
    ENTITY_TYPES['PERSON']: 'caliper.entities.Person',
    ENTITY_TYPES['READING']: 'caliper.entities.Reading',
    ENTITY_TYPES['RESPONSE']: 'caliper.entities.Response',
    ENTITY_TYPES['RESULT']: 'caliper.entities.Result',
    ENTITY_TYPES['SELECTTEXT']: 'caliper.entities.SelectTextResponse',
    ENTITY_TYPES['SESSION']: 'caliper.entities.Session',
    ENTITY_TYPES['SHARED_ANNOTATION']: 'caliper.entities.SharedAnnotation',
    ENTITY_TYPES['SOFTWARE_APPLICATION']: 'caliper.entities.SoftwareApplication',
    ENTITY_TYPES['TAG_ANNOTATION']: 'caliper.entities.TagAnnotation',
    ENTITY_TYPES['TRUEFALSE']: 'caliper.entities.TrueFalseResponse',
    ENTITY_TYPES['VIDEO_OBJECT']: 'caliper.entities.VideoObject',
    ENTITY_TYPES['WEB_PAGE']: 'caliper.entities.WebPage'
    }


EVENT_CONTEXTS = {
    'ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ASSESSMENT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'ASSIGNABLE': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'EVENT': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'MEDIA': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'NAVIGATION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'OUTCOME': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'READING': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'SESSION': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    'VIEW': 'http://purl.imsglobal.org/ctx/caliper/v1/Context',
    }

EVENT_TYPES = {
    'ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/AnnotationEvent',
    'ASSESSMENT': 'http://purl.imsglobal.org/caliper/v1/AssessmentEvent',
    'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/caliper/v1/AssessmentItemEvent',
    'ASSIGNABLE': 'http://purl.imsglobal.org/caliper/v1/AssignableEvent',
    'EVENT': 'http://purl.imsglobal.org/caliper/v1/Event',
    'MEDIA': 'http://purl.imsglobal.org/caliper/v1/MediaEvent',
    'NAVIGATION': 'http://purl.imsglobal.org/caliper/v1/NavigationEvent',
    'OUTCOME': 'http://purl.imsglobal.org/caliper/v1/OutcomeEvent',
    'READING': 'http://purl.imsglobal.org/caliper/v1/ReadingEvent',
    'SESSION': 'http://purl.imsglobal.org/caliper/v1/SessionEvent',
    'VIEW': 'http://purl.imsglobal.org/caliper/v1/ViewEvent',
    }

EVENT_CLASSES = {
    EVENT_TYPES['ANNOTATION']: 'caliper.events.AnnotationEvent',
    EVENT_TYPES['ASSESSMENT']: 'caliper.events.AssessmentEvent',
    EVENT_TYPES['ASSESSMENT_ITEM']: 'caliper.events.AssessmentItemEvent',
    EVENT_TYPES['ASSIGNABLE']: 'caliper.events.AssignableEvent',
    EVENT_TYPES['EVENT']: 'caliper.events.Event',
    EVENT_TYPES['MEDIA']: 'caliper.events.MediaEvent',
    EVENT_TYPES['NAVIGATION']: 'caliper.events.NavigationEvent',
    EVENT_TYPES['OUTCOME']: 'caliper.events.OutcomeEvent',
    EVENT_TYPES['READING']: 'caliper.events.ReadingEvent',
    EVENT_TYPES['SESSION']: 'caliper.events.SessionEvent',
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
