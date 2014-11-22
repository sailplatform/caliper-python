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
        'ATTACHED': 'attached',
        'BOOKMARKED': 'bookmarked',
        'CLASSIFIED': 'classified',
        'COMMENTED': 'commented',
        'DESCRIBED': 'described',
        'HIGHLIGHTED': 'highlighted',
        'IDENTIFIED': 'identified',
        'LIKED': 'liked',
        'LINKED': 'linked',
        'QUESTIONED': 'questioned',
        'RANKED': 'ranked',
        'RECOMMENDED': 'recommended',
        'REPLIED': 'replied',
        'SHARED': 'shared',
        'SUBSCRIBED': 'subscribed',
        'TAGGED': 'tagged',
        
        'NAVIGATED_TO': 'navigated to'
        }
        
    _assessment_actions = {
        'PAUSED': 'paused',
        'RESTARTED': 'restarted',
        'STARTED': 'started',
        'SUBMITTED': 'submitted',
        
        'NAVIGATED_TO': 'navigated to'
        }

    _assessment_item_actions = {
        'COMPLETED': 'completed',
        'SKIPPED': 'skipped',
        'STARTED': 'started',
        'REVIEWED': 'reviewed',
        'VIEWED': 'viewed',
        
        'NAVIGATED_TO': 'navigated to'
        }

    _assignable_actions = {
        'ABANDONED': 'abandoned',
        'ACTIVATED': 'activated',
        'COMPLETED': 'completed',
        'DEACTIVATED': 'deactivated',
        'HID': 'hid',
        'REVIEWED': 'reviewed',
        'SHOWED': 'showed',
        'STARTED': 'started',
        'SUBMITTED': 'submitted',
        
        'NAVIGATED_TO': 'navigated to'
        }

    _media_actions = {
        'DISABLEDCLOSEDCAPTIONING': 'disabled closed captioning',
        'ENABLEDCLOSECAPTIONING': 'enabled closed captioning',

        'CHANGEDVOLUME': 'changed volume',
        'MUTED': 'muted',
        'UNMUTED': 'unmuted',

        'CHANGEDSPEED': 'changed speed',
        'ENDED': 'ended',
        'FORWARDEDTO': 'forwarded to',
        'JUMPEDTO': 'jumpted to',
        'PAUSED': 'paused',
        'RESUMED': 'resumed',
        'REWINDED': 'rewinded to',
        'STARTED': 'started',

        'CHANGEDRESOLUTION': 'changed resolution',
        'CHANGEDVIEWERSIZE': 'changed viewer size',
        'CLOSEDPOPOUT': 'closed popout',
        'ENTEREDFULLSCREEN': 'entered full screen',
        'EXITEDFULLSCREEN': 'exited full screen',
        'OPENEDPOPOUT': 'opened popout',

        'NAVIGATED_TO': 'navigated to'
        }

    _outcome_actions = {
        'GRADED': 'graded',

        'NAVIGATED_TO': 'navigated to'
        }

    _reading_actions = {
        'SEARCHED': 'searched',
        'VIEWED': 'viewed',

        'NAVIGATED_TO': 'navigated to'
        }
