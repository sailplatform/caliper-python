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
                       MediaObject, )

## Base profile class

class Profile(BaseProfile):
    _actions = {
        'DOWNLOADED': 'downloaded', # item.downloaded
        'UPLOADED': 'uploaded', # item.uploaded
        
        'LOGGED_IN': 'logged in', # session.loggedIn
        'LOGGED_OUT': 'logged out', # session.loggedOut

        'VIEWED': 'viewed', # reading.viewed
        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }

## Derived profiles ##

class AnnotationProfile(Profile):
    _actions = {
        'ATTACHED': 'attached', # annotation.attached
        'BOOKMARKED': 'bookmarked', # annotation.bookmarked
        'CLASSIFIED': 'classified', # annotation.classified
        'COMMENTED': 'commented', # annotation.commented
        'DESCRIBED': 'described', # annotation.described
        'HIGHLIGHTED': 'highlighted', # annotation.highlighted
        'IDENTIFIED': 'identified', # annotation.identified
        'LIKED': 'liked', # annotation.liked
        'LINKED': 'linked', # annotation.linked
        'QUESTIONED': 'questioned', # annotation.questioned
        'RANKED': 'ranked', # annotation.ranked
        'RECOMMENDED': 'recommended', # annotation.recommended
        'REPLIED': 'replied', # annotation.replied
        'SHARED': 'shared', # annotation.shared
        'SUBSCRIBED': 'subscribed', # annotation.subscribed
        'TAGGED': 'tagged', # annotation.tagged
        }
        
class AssessmentProfile(Profile):
    _actions = {
        'PAUSED': 'paused', # assessment.paused
        'RESTARTED': 'restarted', # assessment.restarted
        'STARTED': 'started', # assessment.started
        'SUBMITTED': 'submitted', # assessment.submitted
        
        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }

class AssessmentItemProfile(Profile):
    _actions = {
        'COMPLETED': 'completed', # assessment.item.completed
        'SKIPPED': 'skipped', # assessment.item.skipped
        'STARTED': 'started', # assessment.item.started
        'REVIEWED': 'reviewed', # assessment.item.reviewed
        'VIEWED': 'viewed', # assessment.item.viewed
        
        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }

class AssignableProfile(Profile):
    _actions = {
        'ABANDONED': 'abandoned', # assignable.abandoned
        'ACTIVATED': 'activated', # assignable.activated
        'COMPLETED': 'completed', # assignable.completed
        'DEACTIVATED': 'deactivated', # assignable.deactivated
        'HID': 'hid', # assignable.hid
        'REVIEWED': 'reviewed', # assignable.reviewed
        'SHOWED': 'showed', # assignable.showed
        'STARTED': 'started', # assignable.started
        'SUBMITTED': 'submitted', # assignable.submitted
        
        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }

class MediaProfile(Profile):
    _actions = {
        'DISABLEDCLOSEDCAPTIONING': 'disabled closed captioning', # media.accessibility.disabledClosedCaptioning
        'ENABLEDCLOSECAPTIONING': 'enabled closed captioning', # media.accessibility.enabledClosedCaptioning

        'CHANGEDVOLUME': 'changed volume', # media.audio.changedVolume
        'MUTED': 'muted', # media.audio.muted
        'UNMUTED': 'unmuted', # media.audio.unmuted

        'CHANGEDSPEED': 'changed speed', # media.playback.changedSpeed
        'ENDED': 'ended', # media.playback.ended
        'FORWARDEDTO': 'forwarded to', # media.playback.forwardedTo
        'JUMPEDTO': 'jumped to', # media.playback.jumpedTo
        'PAUSED': 'paused', # media.playback.paused
        'RESUMED': 'resumed', # media.playback.resumed
        'REWINDED': 'rewinded to', # media.playback.rewindedTo
        'STARTED': 'started', # media.playback.started

        'CHANGEDRESOLUTION': 'changed resolution', # media.viewer.changedResolution
        'CHANGEDSIZE': 'changed viewer size', # media.viewer.changedSize
        'CLOSEDPOPOUT': 'closed popout', # media.viewer.closedPopout
        'ENTEREDFULLSCREEN': 'entered full screen', # media.viewer.enteredFullScreen
        'EXITEDFULLSCREEN': 'exited full screen', # media.viewer.exitedFullScreen
        'OPENEDPOPOUT': 'opened popout', # media.viewer.openedPopout
        
        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }
        
class OutcomeProfile(Profile):
    _actions = {
        'GRADED': 'graded', # outcome.graded
        
        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }

class ReadingProfile(Profile):
    _actions = {
        'SEARCHED': 'searched', # reading.searched
        'VIEWED': 'viewed', # reading.viewed

        'NAVIGATED_TO': 'navigated to', # navigation.navigatedTo
        }

class SessionProfile(Profile):
    _actions = {
        'LOGGEDIN': 'logged in', # session.loggedIn
        'LOGGEDOUT': 'logged out', # session.loggedOut
        'TIMEDOUT': 'timed out', # session.timedOut
        }
