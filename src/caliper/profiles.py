# -*- coding: utf-8 -*-
# Caliper-python package, profiles module
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
import six

from .base import BaseProfile, CaliperSerializable
from .entities import Assignable, Generatable, Targetable
from .entities import (Assessment, AssessmentItem, AssignableDigitalResource,
                       Attempt, DigitalResource, LearningContext, MediaLocation,
                       MediaObject, Outcome, )

## Base profile class

class Profile(BaseProfile):
    _actions = {
        'DOWNLOADED': 'item.downloaded',
        'UPLOADED': 'item.uploaded',
        
        'LOGGED_IN': 'session.loggedIn',
        'LOGGED_OUT': 'session.loggedOut',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

## Derived profiles ##

class AnnotationProfile(Profile):
    _actions = {
        'ATTACHED': 'annotation.attached',
        'BOOKMARKED': 'annotation.bookmarked',
        'CLASSIFIED': 'annotation.classified',
        'COMMENTED': 'annotation.commented',
        'DESCRIBED': 'annotation.described',
        'HIGHLIGHTED': 'annotation.highlighted',
        'IDENTIFIED': 'annotation.identified',
        'LIKED': 'annotation.liked',
        'LINKED': 'annotation.linked',
        'QUESTIONED': 'annotation.questioned',
        'RANKED': 'annotation.ranked',
        'RECOMMENDED': 'annotation.recommended',
        'REPLIED': 'annotation.replied',
        'SHARED': 'annotation.shared',
        'SUBSCRIBED': 'annotation.subscribed',
        'TAGGED': 'annotation.tagged',
        }
        
class AssessmentProfile(Profile):
    _actions = {
        'PAUSED': 'assessment.paused',
        'RESTARTED': 'assessment.restarted',
        'STARTED': 'assessment.started',
        'SUBMITTED': 'assessment.submitted',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

class AssessmentItemProfile(Profile):
    _actions = {
        'COMPLETED': 'assessment.item.completed',
        'SKIPPED': 'assessment.item.skipped',
        'STARTED': 'assessment.item.started',
        'REVIEWED': 'assessment.item.reviewed',
        'VIEWED': 'assessment.item.viewed',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

class AssignableProfile(Profile):
    _actions = {
        'ABANDONED': 'assignable.abandoned',
        'ACTIVATED': 'assignable.activated',
        'COMPLETED': 'assignable.completed',
        'DEACTIVATED': 'assignable.deactivated',
        'HID': 'assignable.hid',
        'REVIEWED': 'assignable.reviewed',
        'SHOWED': 'assignable.showed',
        'STARTED': 'assignable.started',
        'SUBMITTED': 'assignable.submitted',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

class MediaProfile(Profile):
    _actions = {
        'DISABLEDCLOSEDCAPTIONING': 'media.accessibility.disabledClosedCaptioning',
        'ENABLEDCLOSECAPTIONING': 'media.accessibility.enabledClosedCaptioning',

        'CHANGEDVOLUME': 'media.audio.changedVolume',
        'MUTED': 'media.audio.muted',
        'UNMUTED': 'media.audio.unmuted',

        'CHANGEDSPEED': 'media.playback.changedSpeed',
        'ENDED': 'media.playback.ended',
        'FORWARDEDTO': 'media.playback.forwardedTo',
        'JUMPEDTO': 'media.playback.jumpedTo',
        'PAUSED': 'media.playback.paused',
        'RESUMED': 'media.playback.resumed',
        'REWINDED': 'media.playback.rewindedTo',
        'STARTED': 'media.playback.started',

        'CHANGEDRESOLUTION': 'media.viewer.changedResolution',
        'CHANGEDVIEWERSIZE': 'media.viewer.changedViewerSize',
        'CLOSEDPOPOUT': 'media.viewer.closedPopout',
        'ENTEREDFULLSCREEN': 'media.viewer.enteredFullScreen',
        'EXITEDFULLSCREEN': 'media.viewer.exitedFullScreen',
        'OPENEDPOPOUT': 'media.viewer.openedPopout',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }
        
class OutcomeProfile(Profile):
    _actions = {
        'GRADED': 'outcome.graded',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

class ReadingProfile(Profile):
    _actions = {
        'SEARCHED': 'reading.searched',
        'VIEWED': 'reading.viewed',
        }
