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
CALIPER_VERSION = 'v1p1'
CALIPER_CORE_CONTEXT = 'http://purl.imsglobal.org/ctx/caliper/{}'.format(CALIPER_VERSION)
_CALIPER_PROFILE_CTXTS = 'http://purl.imsglobal.org/caliper/' + CALIPER_VERSION + '/{}'
_CALIPER_PROFILE_EXT_CTXTS = _CALIPER_PROFILE_CTXTS + '-extension'


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
    'COURSE_OFFERING': 'CourseOffering',
    'COURSE_SECTION': 'CourseSection',
    'DIGITAL_RESOURCE': 'DigitalResource',
    'DIGITAL_RESOURCE_COLLECTION': 'DigitalResourceCollection',
    'DOCUMENT': 'Document',
    'ENTITY': 'Entity',
    'EPUB_CHAPTER': 'EpubChapter',
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
    'SCORE': 'Score',
    'SELECTTEXT': 'SelectTextResponse',
    'SESSION': 'Session',
    'SHARED_ANNOTATION': 'SharedAnnotation',
    'SOFTWARE_APPLICATION': 'SoftwareApplication',
    'TAG_ANNOTATION': 'TagAnnotation',
    'TEXT_POSITION_SELECTOR': 'TextPositionSelector',
    'THREAD': 'Thread',
    'TRUEFALSE': 'TrueFalseResponse',
    'VIDEO_OBJECT': 'VideoObject',
    'WEB_PAGE': 'WebPage'
}

## map implementing Python classes onto entity types
ENTITY_CLASSES = { ENTITY_TYPES[key]:'caliper.entities.{}'.format(ENTITY_TYPES[key])
                   for key in ENTITY_TYPES.keys() }


EVENT_TYPES = {
    'ANNOTATION_EVENT': 'AnnotationEvent',
    'ASSESSMENT_EVENT': 'AssessmentEvent',
    'ASSESSMENT_ITEM_EVENT': 'AssessmentItemEvent',
    'ASSIGNABLE_EVENT': 'AssignableEvent',
    'EVENT': 'Event',
    'FORUM_EVENT': 'ForumEvent',
    'MEDIA_EVENT': 'MediaEvent',
    'MESSAGE_EVENT': 'MessageEvent',
    'NAVIGATION_EVENT': 'NavigationEvent',
    'GRADE_EVENT': 'GradeEvent',
    'SESSION_EVENT': 'SessionEvent',
    'THREAD_EVENT': 'ThreadEvent',
    'TOOL_LAUNCH_EVENT': 'ToolLaunchEvent',
    'TOOL_USE_EVENT': 'ToolUseEvent',
    'VIEW_EVENT': 'ViewEvent',
}

## map implementing Python classes onto entity types
EVENT_CLASSES = { EVENT_TYPES[key]:'caliper.events.{}'.format(EVENT_TYPES[key])
                  for key in EVENT_TYPES.keys() }


MARKER_TYPES = {
    'ASSIGNABLE': 'Assignable',
    'GENERATABLE': 'Generatable',
    'REFERRABLE': 'Referrable',
    'TARGETABLE': 'Targetable',
}

## map implementing Python classes onto event types
MARKER_CLASSES = { MARKER_TYPES[key]:'caliper.entities.{}'.format(MARKER_TYPES[key])
                   for key in MARKER_TYPES.keys() }


CALIPER_TYPES = {}
CALIPER_TYPES.update(ENTITY_TYPES)
CALIPER_TYPES.update(EVENT_TYPES)
CALIPER_TYPES.update(MARKER_TYPES)

## maps types to Python classnames
CALIPER_CLASSES = {}
CALIPER_CLASSES.update(ENTITY_CLASSES)
CALIPER_CLASSES.update(EVENT_CLASSES)
CALIPER_CLASSES.update(MARKER_CLASSES)

## maps Python classnames back to types
CALIPER_TYPES_FOR_CLASSES = { CALIPER_CLASSES[key]:key for key in CALIPER_CLASSES.keys() }

## Caliper Roles and Status vocabulary
CALIPER_ROLES = {
    'LEARNER': 'Learner',
    'EXTERNAL_LEARNER': 'Learner#ExternalLearner',
    'GUEST_LEARNER': 'Learner#GuestLearner',
    'LEARNER_INSTRUCTOR': 'Learner#Instructor',
    'LEARNER_LEARNER': 'Learner#Learner',
    'NONCREDIT_LEARNER': 'Learner#NonCreditLearner',
    'INSTRUCTOR': 'Instructor',
    'EXTERNAL_INSTRUCTOR': 'Instructor#ExternalInstructor',
    'GUEST_INSTRUCTOR': 'Instructor#GuestInstructor',
    'LECTURER': 'Instructor#Lecturer',
    'PRIMARY_INSTRUCTOR': 'Instructor#PrimaryInstructor',
    'ADMINISTRATOR': 'Administrator',
    'ADMINISTRATOR_ADMINISTRATOR': 'Administrator#Administrator',
    'ADMINISTRATOR_DEVELOPER': 'Administrator#Developer',
    'ADMINISTRATOR_SUPPORT': 'Administrator#Support',
    'ADMINISTRATOR_SYSTEM_ADMINISTRATOR': 'Administrator#SystemAdministrator',
    'ADMINISTRATOR_EXTERNAL_DEVELOPER': 'Administrator#ExternalSupport',
    'ADMINISTRATOR_EXTERNAL_SUPPORT': 'Administrator#ExternalDeveloper',
    'ADMINISTRATOR_EXTERNAL_SYSTEM_ADMINISTRATOR': 'Administrator#ExternalSystemAdministrator',
    'CONTENT_DEVELOPER': 'ContentDeveloper',
    'CONTENT_DEVELOPER_CONTENT_DEVELOPER': 'ContentDeveloper#ContentDeveloper',
    'CONTENT_DEVELOPER_LIBRARIAN': 'ContentDeveloper#Librarian',
    'CONTENT_DEVELOPER_CONTENT_EXPERT': 'ContentDeveloper#ContentExpert',
    'CONTENT_DEVELOPER_EXTERNAL_CONTENT_EXPERT': 'ContentDeveloper#ExternalContentExpert',
    'MANAGER': 'Manager',
    'MANAGER_AREA_MANAGER': 'Manager#AreaManager',
    'MANAGER_COURSE_COORDINATOR': 'Manager#CourseCoordinator',
    'MANAGER_OBSERVER': 'Manager#Observer',
    'MANAGER_EXTERNAL_OBSERVER': 'Manager#ExternalObserver',
    'MEMBER': 'Member',
    'MEMBER_MEMBER': 'Member#Member',
    'MENTOR': 'Mentor',
    'MENTOR_MENTOR': 'Mentor#Mentor',
    'MENTOR_ADVISOR': 'Mentor#Advisor',
    'MENTOR_AUDITOR': 'Mentor#Auditor',
    'MENTOR_REVIEWER': 'Mentor#Reviewer',
    'MENTOR_TUTOR': 'Mentor#Tutor',
    'MENTOR_LEARNING_FACILITATOR': 'Mentor#LearningFacilitator',
    'MENTOR_EXTERNAL_MENTOR': 'Mentor#ExternalMentor',
    'MENTOR_EXTERNAL_ADVISOR': 'Mentor#ExternalAdvisor',
    'MENTOR_EXTERNAL_AUDITOR': 'Mentor#ExternalAuditor',
    'MENTOR_EXTERNAL_REVIEWER': 'Mentor#ExternalReviewer',
    'MENTOR_EXTERNAL_TUTOR': 'Mentor#ExternalTutor',
    'MENTOR_EXTERNAL_LEARNING_FACILITATOR': 'Mentor/ExternalLearningFacilitator',
    'TEACHING_ASSISTANT': 'TeachingAssistant',
    'TEACHING_ASSISTANT_TEACHING_ASSISTANT': 'TeachingAssistant#TeachingAssistant',
    'TEACHING_ASSISTANT_GRADER': 'TeachingAssistant#Grader',
    'TEACHING_ASSISTANT_TEACHING_ASSISTANT_SECTION': 'TeachingAssistant#TeachingAssistantSection',
    'TEACHING_ASSISTANT_TEACHING_ASSISTANT_SECTION_ASSOCIATION': 'TeachingAssistant#TeachingAssistantSectionAssociation',
    'TEACHING_ASSISTANT_TEACHING_ASSISTANT_OFFERING': 'TeachingAssistant#TeachingAssistantOffering',
    'TEACHING_ASSISTANT_TEACHING_ASSISTANT_TEMPLATE': 'TeachingAssistant#TeachingAssistantTemplate',
    'TEACHING_ASSISTANT_TEACHING_ASSISTANT_GROUP': 'TeachingAssistant#TeachingAssistantGroup',
}

CALIPER_STATUS = {
    'ACTIVE': 'Active',
    'DELETED': 'Deleted',
    'INACTIVE': 'Inactive',
}

## Caliper Profiles and their associated properties
CALIPER_PROFILES = {
    'BASIC_PROFILE': 'BasicProfile',
    'ANNOTATION_PROFILE': 'AnnotationProfile',
    'ASSESSMENT_PROFILE': 'AssessmentProfile',
    'ASSIGNABLE_PROFILE': 'AssignableProfile',
    'FORUM_PROFILE': 'ForumProfile',
    'GRADING_PROFILE': 'GradingProfile',
    'MEDIA_PROFILE': 'MediaProfile',
    'READING_PROFILE': 'ReadingProfile',
    'SESSION_PROFILE': 'SessionProfile',
    'TOOL_USE_PROFILE': 'ToolUseProfile',
    }

PROFILE_CONTEXTS = { CALIPER_PROFILES[key]:CALIPER_CORE_CONTEXT for key in CALIPER_PROFILES.keys() }
# We don't yet support specific profile contexts for core profiles
# PROFILE_CONTEXTS = { CALIPER_PROFILES[key]:_CALIPER_PROFILE_CTXTS.format(CALIPER_PROFILES[key])
#                      for key in CALIPER_PROFILES.keys() }
#
## profile context exceptions
# PROFILE_CONTEXTS[CALIPER_PROFILES['BASIC_PROFILE']] = CALIPER_CORE_CONTEXT

CALIPER_CONTEXTS = {}
CALIPER_CONTEXTS.update(PROFILE_CONTEXTS)

CALIPER_PROFILES_FOR_CONTEXTS = {}
CALIPER_PROFILES_FOR_CONTEXTS.update(
    {CALIPER_CORE_CONTEXT : CALIPER_PROFILES['BASIC_PROFILE']}
)

CALIPER_PROFILES_FOR_EVENT_TYPES = {
    EVENT_TYPES['EVENT'] : CALIPER_PROFILES['BASIC_PROFILE'],
    EVENT_TYPES['ANNOTATION_EVENT'] : CALIPER_PROFILES['ANNOTATION_PROFILE'],
    EVENT_TYPES['ASSESSMENT_EVENT'] : CALIPER_PROFILES['ASSESSMENT_PROFILE'],
    EVENT_TYPES['ASSESSMENT_ITEM_EVENT'] : CALIPER_PROFILES['ASSESSMENT_PROFILE'],
    EVENT_TYPES['ASSIGNABLE_EVENT'] : CALIPER_PROFILES['ASSIGNABLE_PROFILE'],
    EVENT_TYPES['FORUM_EVENT'] : CALIPER_PROFILES['FORUM_PROFILE'],
    EVENT_TYPES['GRADE_EVENT'] : CALIPER_PROFILES['GRADING_PROFILE'],
    EVENT_TYPES['MEDIA_EVENT'] : CALIPER_PROFILES['MEDIA_PROFILE'],
    EVENT_TYPES['MESSAGE_EVENT'] : CALIPER_PROFILES['FORUM_PROFILE'],
    EVENT_TYPES['NAVIGATION_EVENT'] : CALIPER_PROFILES['BASIC_PROFILE'],
    EVENT_TYPES['SESSION_EVENT'] : CALIPER_PROFILES['SESSION_PROFILE'],
    EVENT_TYPES['THREAD_EVENT'] : CALIPER_PROFILES['FORUM_PROFILE'],
    EVENT_TYPES['TOOL_USE_EVENT'] : CALIPER_PROFILES['TOOL_USE_PROFILE'],
    EVENT_TYPES['VIEW_EVENT'] : CALIPER_PROFILES['BASIC_PROFILE']
}

CALIPER_ACTIONS = {
    'ABANDONED': 'Abandoned',
    'ACTIVATED': 'Activated',
    'ADDED': 'Added',
    'ATTACHED': 'Attached',
    'BOOKMARKED': 'Bookmarked',
    'CHANGED_RESOLUTION': 'ChangedResolution',
    'CHANGED_SIZE': 'ChangedSize',
    'CHANGED_SPEED': 'ChangedSpeed',
    'CHANGED_VOLUME': 'ChangedVolume',
    'CLASSIFIED': 'Classified',
    'CLOSED_POPOUT': 'ClosedPopout',
    'COMMENTED': 'Commented',
    'COMPLETED': 'Completed',
    'CREATED': 'Created',
    'DEACTIVATED': 'Deactivated',
    'DELETED': 'Deleted',
    'DESCRIBED': 'Described',
    'DISABLED_CLOSED_CAPTIONING': 'DisabledClosedCaptioning',
    'DISLIKED': 'Disliked',
    'EARNED': 'Earned',
    'ENABLED_CLOSED_CAPTIONING': 'EnabledClosedCaptioning',
    'ENDED': 'Ended',
    'ENTERED_FULLSCREEN': 'EnteredFullScreen',
    'EXITED_FULLSCREEN': 'ExitedFullScreen',
    'FORWARDED_TO': 'ForwardedTo',
    'GRADED': 'Graded',
    'HID': 'Hid',
    'HIGHLIGHTED': 'Highlighted',
    'IDENTIFIED': 'Identified',
    'JUMPED_TO': 'JumpedTo',
    'LIKED': 'Liked',
    'LINKED': 'Linked',
    'LOGGED_IN': 'LoggedIn',
    'LOGGED_OUT': 'LoggedOut',
    'MARKED_AS_READ': 'MarkedAsRead',
    'MARKED_AS_UNREAD': 'MarkedAsUnread',
    'MODIFIED': 'Modified',
    'MUTED': 'Muted',
    'NAVIGATED_TO': 'NavigatedTo',
    'OPENED_POPOUT': 'OpenedPopout',
    'PAUSED': 'Paused',
    'POSTED': 'Posted',
    'QUESTIONED': 'Questioned',
    'RANKED': 'Ranked',
    'RECOMMENDED': 'Recommended',
    'REMOVED': 'Removed',
    'REPLIED': 'Replied',
    'RESET': 'Reset',
    'RESTARTED': 'Restarted',
    'RESUMED': 'Resumed',
    'RETRIEVED': 'Retrieved',
    'REVIEWED': 'Reviewed',
    'REWOUND': 'Rewound',
    'SEARCHED': 'Searched',
    'SHARED': 'Shared',
    'SHOWED': 'Showed',
    'SKIPPED': 'Skipped',
    'STARTED': 'Started',
    'SUBMITTED': 'Submitted',
    'SUBSCRIBED': 'Subscribed',
    'TAGGED': 'Tagged',
    'TIMED_OUT': 'TimedOut',
    'UNMUTED': 'Unmuted',
    'UNSUBSCRIBED': 'Unsubscribed',
    'USED': 'Used',
    'VIEWED': 'Viewed'
}

BASIC_EVENT_ACTIONS = list(CALIPER_ACTIONS.values())
ANNOTATION_EVENT_ACTIONS = [
    CALIPER_ACTIONS['BOOKMARKED'],
    CALIPER_ACTIONS['HIGHLIGHTED'],
    CALIPER_ACTIONS['SHARED'],
    CALIPER_ACTIONS['TAGGED'],
]
ASSESSMENT_EVENT_ACTIONS = [
    CALIPER_ACTIONS['PAUSED'],
    CALIPER_ACTIONS['RESTARTED'],
    CALIPER_ACTIONS['RESUMED'],
    CALIPER_ACTIONS['STARTED'],
    CALIPER_ACTIONS['SUBMITTED']
]
ASSESSMENT_ITEM_EVENT_ACTIONS = [
    CALIPER_ACTIONS['COMPLETED'],
    CALIPER_ACTIONS['SKIPPED'],
    CALIPER_ACTIONS['STARTED']
]
ASSIGNABLE_EVENT_ACTIONS = [
    CALIPER_ACTIONS['ACTIVATED'],
    CALIPER_ACTIONS['COMPLETED'],
    CALIPER_ACTIONS['DEACTIVATED'],
    CALIPER_ACTIONS['STARTED'],
    CALIPER_ACTIONS['SUBMITTED']
]
FORUM_EVENT_ACTIONS = [
    CALIPER_ACTIONS['SUBSCRIBED'],
    CALIPER_ACTIONS['UNSUBSCRIBED']
]
GRADE_EVENT_ACTIONS = [ CALIPER_ACTIONS['GRADED'] ]
MEDIA_EVENT_ACTIONS = [
    CALIPER_ACTIONS['CHANGED_RESOLUTION'],
    CALIPER_ACTIONS['CHANGED_SIZE'],
    CALIPER_ACTIONS['CHANGED_SPEED'],
    CALIPER_ACTIONS['CHANGED_VOLUME'],
    CALIPER_ACTIONS['CLOSED_POPOUT'],
    CALIPER_ACTIONS['DISABLED_CLOSED_CAPTIONING'],
    CALIPER_ACTIONS['ENABLED_CLOSED_CAPTIONING'],
    CALIPER_ACTIONS['ENDED'],
    CALIPER_ACTIONS['ENTERED_FULLSCREEN'],
    CALIPER_ACTIONS['EXITED_FULLSCREEN'],
    CALIPER_ACTIONS['FORWARDED_TO'],
    CALIPER_ACTIONS['JUMPED_TO'],
    CALIPER_ACTIONS['MUTED'],
    CALIPER_ACTIONS['OPENED_POPOUT'],
    CALIPER_ACTIONS['PAUSED'],
    CALIPER_ACTIONS['RESUMED'],
    CALIPER_ACTIONS['RESTARTED'],
    CALIPER_ACTIONS['STARTED'],
    CALIPER_ACTIONS['UNMUTED']
]
MESSAGE_EVENT_ACTIONS = [
    CALIPER_ACTIONS['MARKED_AS_READ'],
    CALIPER_ACTIONS['MARKED_AS_UNREAD'],
    CALIPER_ACTIONS['POSTED']
]
NAVIGATION_EVENT_ACTIONS = [ CALIPER_ACTIONS['NAVIGATED_TO'] ]
SESSION_EVENT_ACTIONS = [
    CALIPER_ACTIONS['LOGGED_IN'],
    CALIPER_ACTIONS['LOGGED_OUT'],
    CALIPER_ACTIONS['TIMED_OUT']
]
THREAD_EVENT_ACTIONS = [
    CALIPER_ACTIONS['MARKED_AS_READ'],
    CALIPER_ACTIONS['MARKED_AS_UNREAD']
]
TOOL_USE_EVENT_ACTIONS = [ CALIPER_ACTIONS['USED'] ]
VIEW_EVENT_ACTIONS = [ CALIPER_ACTIONS['VIEWED'] ]


CALIPER_PROFILE_ACTIONS = {}
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['BASIC_PROFILE']: {
        EVENT_TYPES['EVENT'] : BASIC_EVENT_ACTIONS,
        EVENT_TYPES['ANNOTATION_EVENT'] : ANNOTATION_EVENT_ACTIONS,
        EVENT_TYPES['ASSESSMENT_EVENT'] : ASSESSMENT_EVENT_ACTIONS,
        EVENT_TYPES['ASSESSMENT_ITEM_EVENT'] : ASSESSMENT_ITEM_EVENT_ACTIONS,
        EVENT_TYPES['ASSIGNABLE_EVENT'] : ASSIGNABLE_EVENT_ACTIONS,
        EVENT_TYPES['FORUM_EVENT'] : FORUM_EVENT_ACTIONS,
        EVENT_TYPES['GRADE_EVENT'] : GRADE_EVENT_ACTIONS,
        EVENT_TYPES['MEDIA_EVENT'] : MEDIA_EVENT_ACTIONS,
        EVENT_TYPES['MESSAGE_EVENT'] : MESSAGE_EVENT_ACTIONS,
        EVENT_TYPES['NAVIGATION_EVENT'] : NAVIGATION_EVENT_ACTIONS,
        EVENT_TYPES['SESSION_EVENT'] : SESSION_EVENT_ACTIONS,
        EVENT_TYPES['THREAD_EVENT'] : THREAD_EVENT_ACTIONS,
        EVENT_TYPES['TOOL_USE_EVENT'] : TOOL_USE_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT'] : VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['ANNOTATION_PROFILE']: {
        EVENT_TYPES['ANNOTATION_EVENT']: ANNOTATION_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT']: VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['ASSESSMENT_PROFILE']: {
        EVENT_TYPES['ASSESSMENT_EVENT'] : ASSESSMENT_EVENT_ACTIONS,
        EVENT_TYPES['ASSESSMENT_ITEM_EVENT'] : ASSESSMENT_ITEM_EVENT_ACTIONS,
        EVENT_TYPES['NAVIGATION_EVENT'] : NAVIGATION_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT']: VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['ASSIGNABLE_PROFILE']: {
        EVENT_TYPES['ASSIGNABLE_EVENT'] : ASSIGNABLE_EVENT_ACTIONS,
        EVENT_TYPES['NAVIGATION_EVENT'] : NAVIGATION_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT']: VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['FORUM_PROFILE']: {
        EVENT_TYPES['FORUM_EVENT'] : FORUM_EVENT_ACTIONS,
        EVENT_TYPES['MESSAGE_EVENT'] : MESSAGE_EVENT_ACTIONS,
        EVENT_TYPES['NAVIGATION_EVENT'] : NAVIGATION_EVENT_ACTIONS,
        EVENT_TYPES['THREAD_EVENT'] : THREAD_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT'] : VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['GRADING_PROFILE']: {
        EVENT_TYPES['GRADE_EVENT'] : GRADE_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT'] : VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['MEDIA_PROFILE']: {
        EVENT_TYPES['MEDIA_EVENT'] : MEDIA_EVENT_ACTIONS,
        EVENT_TYPES['NAVIGATION_EVENT'] : NAVIGATION_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT'] : VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['READING_PROFILE']: {
        EVENT_TYPES['NAVIGATION_EVENT'] : NAVIGATION_EVENT_ACTIONS,
        EVENT_TYPES['VIEW_EVENT']: VIEW_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['SESSION_PROFILE']: {
        EVENT_TYPES['SESSION_EVENT'] : SESSION_EVENT_ACTIONS,
    }}
)
CALIPER_PROFILE_ACTIONS.update(
    { CALIPER_PROFILES['TOOL_USE_PROFILE']: {
        EVENT_TYPES['TOOL_USE_EVENT'] : TOOL_USE_EVENT_ACTIONS,
    }}
)
