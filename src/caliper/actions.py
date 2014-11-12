# -*- coding: utf-8 -*-
# Caliper-python package, actions module
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

from .base import BaseAction

class Action(BaseAction):

    _annotation_actions = {
        'ATTACHED': 'annotation.attached',
        'BOOKMARKED': 'annotation.bookmarked',
        'CLASSIFIED': 'annotation.classified',
        'COMMENTED': 'annotation.commented',
        'DESCRIBED': 'annotation.described',
        'HIGHLIGHTED': 'annotation.highlighted',
        'IDENTIFIED': 'annotation.identified',
        'LIKED': 'annotation.liked',
        'RANKED': 'annotation.ranked',
        'QUESTIONED': 'annotation.questioned',
        'RECOMMENDED': 'annotation.recommended',
        'REPLIED': 'annotation.replied',
        'SHARED': 'annotation.shared',
        'SUBSCRIBED': 'annotation.subscribed',
        'TAGGED': 'annotation.tagged',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }
        
    _assessment_actions = {
        'STARTED': 'assessment.started',
        'PAUSED': 'assessment.paused',
        'RESTARTED': 'assessment.restarted',
        'SUBMITTED': 'assessment.submitted',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

    _assessment_item_actions = {
        'STARTED': 'assessment.item.started',
        'COMPLETED': 'assessment.item.completed',
        'SKIPPED': 'assessment.item.skipped',
        'REVIEWED': 'assessment.item.reviewed',
        'VIEWED': 'assessment.item.viewed',
        
        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

    _assignable_actions = {
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

    _media_actions = {
        'ENABLEDCLOSECAPTIONING': 'media.accessibility.enabledCloseCaptioning',
        'DISABLEDCLOSEDCAPTIONING': 'media.accessibility.disabledCloseCaptioning',

        'CHANGEDVOLUME': 'media.audio.changedVolume',
        'MUTED': 'media.audio.muted',
        'UNMUTED': 'media.audio.unmuted',

        'CHANGEDSPEED': 'media.playback.changedSpeed',
        'ENDED': 'media.playback.ended',
        'JUMPEDTO': 'media.playback.jumpedTo',
        'FORWARDEDTO': 'media.playback.forwardedTo',
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

    _outcome_actions = {
        'GRADED': 'outcome.graded',

        'NAVIGATED_TO': 'navigation.navigatedTo'
        }

    _reading_actions = {
        'SEARCHED': 'reading.searched',
        'VIEWED': 'reading.viewed',

        'NAVIGATED_TO': 'navigation.navigatedTo'
        }
