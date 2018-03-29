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

CALIPER_PROFILES = {
    'BASIC_PROFILE': 'BasicProfile',
    'ANNOTATION_PROFILE': 'AnnotationProfile',
    'ASSESSMENT_PROFILE': 'AssessmentProfile',
    'FORUM_PROFILE': 'ForumProfile',
    'GRADING_PROFILE': 'GradingProfile',
    'MEDIA_PROFILE': 'MediaProfile',
    'READING_PROFILE': 'ReadingProfile',
    'SESSION_PROFILE': 'SessionProfile',
    'TOOL_USE_PROFILE': 'ToolUseProfile',
    }

PROFILE_CONTEXTS = { CALIPER_PROFILES[key]:_CALIPER_PROFILE_CTXTS.format(CALIPER_PROFILES[key])
                     for key in CALIPER_PROFILES.keys() }

## profile context exceptions
PROFILE_CONTEXTS[CALIPER_PROFILES['BASIC_PROFILE']] = CALIPER_CORE_CONTEXT

CALIPER_CONTEXTS = {'Caliper': CALIPER_CORE_CONTEXT}
CALIPER_CONTEXTS.update(PROFILE_CONTEXTS)
CALIPER_PROFILES_FOR_CONTEXTS = { CALIPER_CONTEXTS[key]:key for key in PROFILE_CONTEXTS.keys() }

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


## Event Actions
BASIC_EVENT_ACTIONS = {
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

ANNOTATION_EVENT_ACTIONS = {
    'BOOKMARKED': 'Bookmarked',
    'HIGHLIGHTED': 'Highlighted',
    'SHARED': 'Shared',
    'TAGGED': 'Tagged',
}

ASSESSMENT_EVENT_ACTIONS = {
    'PAUSED': 'Paused',
    'RESTARTED': 'Restarted',
    'RESUMED': 'Resumed',
    'STARTED': 'Started',
    'SUBMITTED': 'Submitted',
}

ASSESSMENT_ITEM_EVENT_ACTIONS = {
    'COMPLETED': 'Completed',
    'SKIPPED': 'Skipped',
    'STARTED': 'Started',
}

ASSIGNABLE_EVENT_ACTIONS = {
    'ACTIVATED': 'Activated',
    'COMPLETED': 'Completed',
    'DEACTIVATED': 'Deactivated',
    'STARTED': 'Started',
    'SUBMITTED': 'Submitted',
}

FORUM_EVENT_ACTIONS = {
    'SUBSCRIBED': 'Subscribed',
    'UNSUBSCRIBED': 'Unsubscribed',
}

GRADE_EVENT_ACTIONS = {
    'GRADED': 'Graded',
}

MEDIA_EVENT_ACTIONS = {
    'CHANGED_RESOLUTION': 'ChangedResolution',
    'CHANGED_SIZE': 'ChangedSize',
    'CHANGED_SPEED': 'ChangedSpeed',
    'CHANGED_VOLUME': 'ChangedVolume',
    'CLOSED_POPOUT': 'ClosedPopout',
    'DISABLED_CLOSED_CAPTIONING': 'DisabledClosedCaptioning',
    'ENABLED_CLOSED_CAPTIONING': 'EnabledClosedCaptioning',
    'ENDED': 'Ended',
    'ENTERED_FULLSCREEN': 'EnteredFullScreen',
    'EXITED_FULLSCREEN': 'ExitedFullScreen',
    'FORWARDED_TO': 'ForwardedTo',
    'JUMPED_TO': 'JumpedTo',
    'MUTED': 'Muted',
    'OPENED_POPOUT': 'OpenedPopout',
    'PAUSED': 'Paused',
    'RESUMED': 'Resumed',
    'RESTARTED': 'Restarted',
    'REWOUND': 'Rewound',
    'STARTED': 'Started',
    'UNMUTED': 'Unmuted',
}

MESSAGE_EVENT_ACTIONS = {
    'MARKED_AS_READ': 'MarkedAsRead',
    'MARKED_AS_UNREAD': 'MarkedAsUnread',
    'POSTED': 'Posted',
}

NAVIGATION_EVENT_ACTIONS = {
    'NAVIGATED_TO': 'NavigatedTo',
}

SESSION_EVENT_ACTIONS = {
    'LOGGED_IN': 'LoggedIn',
    'LOGGED_OUT': 'LoggedOut',
    'TIMED_OUT': 'TimedOut',
}

THREAD_EVENT_ACTIONS = {
    'MARKED_AS_READ': 'MarkedAsRead',
    'MARKED_AS_UNREAD': 'MarkedAsUnread',
}

TOOL_USE_EVENT_ACTIONS = {
    'USED': 'Used',
}

VIEW_EVENT_ACTIONS = {
    'VIEWED': 'Viewed'
}


## Profiles
BASIC_PROFILE_ACTIONS = {}
BASIC_PROFILE_ACTIONS.update(BASIC_EVENT_ACTIONS)

ANNOTATION_PROFILE_ACTIONS = {}
ANNOTATION_PROFILE_ACTIONS.update(ANNOTATION_EVENT_ACTIONS)
ANNOTATION_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

ASSESSMENT_PROFILE_ACTIONS = {}
ASSESSMENT_PROFILE_ACTIONS.update(ASSESSMENT_EVENT_ACTIONS)
ASSESSMENT_PROFILE_ACTIONS.update(ASSESSMENT_ITEM_EVENT_ACTIONS)
ASSESSMENT_PROFILE_ACTIONS.update(NAVIGATION_EVENT_ACTIONS)
ASSESSMENT_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

ASSIGNABLE_PROFILE_ACTIONS = {}
ASSIGNABLE_PROFILE_ACTIONS.update(ASSIGNABLE_EVENT_ACTIONS)
ASSIGNABLE_PROFILE_ACTIONS.update(NAVIGATION_EVENT_ACTIONS)
ASSIGNABLE_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

FORUM_PROFILE_ACTIONS = {}
FORUM_PROFILE_ACTIONS.update(FORUM_EVENT_ACTIONS)
FORUM_PROFILE_ACTIONS.update(MESSAGE_EVENT_ACTIONS)
FORUM_PROFILE_ACTIONS.update(THREAD_EVENT_ACTIONS)
FORUM_PROFILE_ACTIONS.update(NAVIGATION_EVENT_ACTIONS)
FORUM_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

GRADING_PROFILE_ACTIONS = {}
GRADING_PROFILE_ACTIONS.update(GRADE_EVENT_ACTIONS)
GRADING_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

MEDIA_PROFILE_ACTIONS = {}
MEDIA_PROFILE_ACTIONS.update(MEDIA_EVENT_ACTIONS)
MEDIA_PROFILE_ACTIONS.update(NAVIGATION_EVENT_ACTIONS)
MEDIA_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

READING_PROFILE_ACTIONS = {}
READING_PROFILE_ACTIONS.update(NAVIGATION_EVENT_ACTIONS)
READING_PROFILE_ACTIONS.update(VIEW_EVENT_ACTIONS)

SESSION_PROFILE_ACTIONS = {}
SESSION_PROFILE_ACTIONS.update(SESSION_EVENT_ACTIONS)

TOOL_USE_PROFILE_ACTIONS = {}
TOOL_USE_PROFILE_ACTIONS.update(TOOL_USE_EVENT_ACTIONS)

CALIPER_ACTIONS = {}
CALIPER_ACTIONS.update(BASIC_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(ANNOTATION_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(ASSESSMENT_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(ASSIGNABLE_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(FORUM_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(MEDIA_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(GRADING_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(READING_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(SESSION_PROFILE_ACTIONS)
CALIPER_ACTIONS.update(TOOL_USE_PROFILE_ACTIONS)
