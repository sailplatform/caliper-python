# -*- coding: utf-8 -*-
# Caliper-python package, profiles module
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements.
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

from __future__ import absolute_import


from caliper.base import BaseProfile

class CaliperProfile(BaseProfile):
    _actions = {
        'ABANDONED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Abandoned',
        'ACTIVATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Activated',
        'ATTACHED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Attached',
        'BOOKMARKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Bookmarked',
        'CHANGED_RESOLUTION': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedResolution',
        'CHANGED_SIZE': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedSize',
        'CHANGED_SPEED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedSpeed',
        'CHANGED_VOLUME': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ChangedVolume',
        'CLASSIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Classified',
        'CLOSED_POPOUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ClosedPopout',
        'COMMENTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Commented',
        'COMPLETED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Completed',
        'DEACTIVATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Deactivated',
        'DESCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Described',
        'DISLIKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Disliked',
        'DISABLED_CLOSED_CAPTIONING': 'http://purl.imsglobal.org/vocab/caliper/v1/action#DisabledClosedCaptioning',
        'ENABLED_CLOSED_CAPTIONING': 'http://purl.imsglobal.org/vocab/caliper/v1/action#EnabledClosedCaptioning',
        'ENDED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Ended',
        'ENTERED_FULLSCREEN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#EnteredFullscreen',
        'EXITED_FULLSCREEN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ExitedFullscreen',
        'FORWARDED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#ForwardedTo',
        'GRADED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Graded',
        'HID': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Hid',
        'HIGHLIGHTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Highlighted',
        'JUMPED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#JumpedTo',
        'IDENTIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Identified',
        'LIKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Liked',
        'LINKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Linked',
        'LOGGED_IN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#LoggedIn',
        'LOGGED_OUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#LoggedOut',
        'MUTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Muted',
        'NAVIGATED_TO': 'http://purl.imsglobal.org/vocab/caliper/v1/action#NavigatedTo',
        'OPENED_POPOUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#OpenedPopout',
        'PAUSED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Paused',
        'RANKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Ranked',
        'QUESTIONED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Questioned',
        'RECOMMENDED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Recommended',
        'REPLIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Replied',
        'RESTARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Restarted',
        'RESUMED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Resumed',
        'REVIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Reviewed',
        'REWOUND': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Rewound',
        'SEARCHED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Searched',
        'SHARED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Shared',
        'SHOWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Showed',
        'SKIPPED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Skipped',
        'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
        'SUBMITTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Submitted',
        'SUBSCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Subscribed',
        'TAGGED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Tagged',
        'TIMED_OUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#TimedOut',
        'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
        'UNMUTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Unmuted',
        }

## Derived profiles ##

class AnnotationProfile(CaliperProfile):
    _actions = {
        'ATTACHED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Attached',
        'BOOKMARKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Bookmarked',
        'CLASSIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Classified',
        'COMMENTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Commented',
        'DESCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Described',
        'DISLIKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Disliked',
        'HIGHLIGHTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Highlighted',
        'IDENTIFIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Identified',
        'LIKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Liked',
        'LINKED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Linked',
        'QUESTIONED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Questioned',
        'RECOMMENDED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Recommended',
        'REPLIED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Replied',
        'SHARED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Shared',
        'SUBSCRIBED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Subscribed',
        'TAGGED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Tagged',
        }
        
class AssessmentProfile(CaliperProfile):
    _actions = {
        'PAUSED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Paused',
        'RESTARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Restarted',
        'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
        'SUBMITTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Submitted',
        }

class AssessmentItemProfile(CaliperProfile):
    _actions = {
        'COMPLETED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Completed',
        'REVIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Reviewed',
        'SKIPPED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Skipped',
        'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
        'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',
        }

class AssignableProfile(CaliperProfile):
    _actions = {
        'ABANDONED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Abandoned',
        'ACTIVATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Activated',
        'COMPLETED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Completed',
        'DEACTIVATED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Deactivated',
        'HID': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Hid',
        'REVIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Reviewed',
        'SHOWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Showed',
        'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
        }

class MediaProfile(CaliperProfile):
    _actions = {
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
        'UNMUTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Unmuted',
        'OPENED_POPOUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#OpenedPopout',
        'PAUSED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Paused',
        'RESUMED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Resumed',
        'REWOUND': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Rewound',
        'STARTED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Started',
        }
        
class OutcomeProfile(CaliperProfile):
    _actions = {
        'GRADED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Graded',
        }

class ReadingProfile(CaliperProfile):
    _actions = {
        'SEARCHED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Searched',
        'VIEWED': 'http://purl.imsglobal.org/vocab/caliper/v1/action#Viewed',        
        }

class SessionProfile(CaliperProfile):
    _actions = {
        'LOGGED_IN': 'http://purl.imsglobal.org/vocab/caliper/v1/action#LoggedIn',
        'LOGGED_OUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#LoggedOut',
        'TIMED_OUT': 'http://purl.imsglobal.org/vocab/caliper/v1/action#TimedOut',
        }
