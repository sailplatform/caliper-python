# -*- coding: utf-8 -*-
# Caliper-python package, events module
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

from .base import BaseEvent, CaliperSerializable
from .actions import Action
from . import entities

## Base event class
class Event(BaseEvent):

    _contexts = {
        'ANNOTATION': 'http://purl.imsglobal.org/ctx/caliper/v1/AnnotationEvent',
        'ASSESSMENT': 'http://purl.imsglobal.org/ctx/caliper/v1/AssessmentEvent',
        'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/ctx/caliper/v1/AssessmentItemEvent',
        'ASSIGNABLE': 'http://purl.imsglobal.org/ctx/caliper/v1/AssignableEvent',
        'EVENT': 'http://purl.imsglobal.org/ctx/caliper/v1/Event',
        'MEDIA': 'http://purl.imsglobal.org/ctx/caliper/v1/MediaEvent',
        'NAVIGATION': 'http://purl.imsglobal.org/ctx/caliper/v1/NavigationEvent',
        'OUTCOME': 'http://purl.imsglobal.org/ctx/caliper/v1/OutcomeEvent',
        'VIEW': 'http://purl.imsglobal.org/ctx/caliper/v1/ViewEvent',
        }    
    _types = {
        'ANNOTATION': 'http://purl.imsglobal.org/caliper/v1/AnnotationEvent',
        'ASSESSMENT': 'http://purl.imsglobal.org/caliper/v1/AssessmentEvent',
        'ASSESSMENT_ITEM': 'http://purl.imsglobal.org/caliper/v1/AssessmentItemEvent',
        'ASSIGNABLE': 'http://purl.imsglobal.org/caliper/v1/AssignableEvent',
        'EVENT': 'http://purl.imsglobal.org/caliper/v1/Event',
        'MEDIA': 'http://purl.imsglobal.org/caliper/v1/MediaEvent',
        'NAVIGATION': 'http://purl.imsglobal.org/caliper/v1/NavigationEvent',
        'OUTCOME': 'http://purl.imsglobal.org/caliper/v1/OutcomeEvent',
        'VIEW': 'http://purl.imsglobal.org/caliper/v1/ViewEvent',
        }

    def __init__(self,
            action = None,
            actor = None,
            context = None,
            duration = None,
            edApp = None,
            endedAtTime = 0,
            event_object = None,
            generated = None,
            group = None,
            startedAtTime = None,
            target = None,
            **kwargs):
        BaseEvent.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['EVENT'])
        self._set_str_prop('@type', Event.Types['EVENT'])

        self._set_str_prop('action', action)

        if actor and (not isinstance(actor, entities.Agent)):
            raise TypeError('actor must implement entities.Agent')
        else:
            self._set_obj_prop('actor', actor)

        self._set_str_prop('duration', duration)
                    
        if edApp and (not isinstance(edApp, entities.SoftwareApplication)):
            raise TypeError('edApp must implement entities.SoftwareApplication')
        else:
            self._set_obj_prop('edApp', edApp)

        self._set_int_prop('endedAtTime', endedAtTime)

        if event_object and (not isinstance(event_object, CaliperSerializable)):
            raise TypeError('event_object must implement CaliperSerializable')
        else:
            self._set_obj_prop('object', event_object)

        if generated and (not isinstance(generated, CaliperSerializable)):
            raise TypeError('generated must implement CaliperSerializable')
        else:
            self._set_obj_prop('generated', generated)

        if group and (not isinstance(group, entities.Organization)):
            raise TypeError('group must implement entities.Organization')
        else:
            self._set_obj_prop('group', group)

        self._set_int_prop('startedAtTime', startedAtTime)
            
        if target and (not isinstance(target, CaliperSerializable)):
            raise TypeError('target must implement CaliperSerializable')
        else:
            self._set_obj_prop('target', target)


    @property
    def context(self):
        return self._get_prop('@context')

    @property
    def type(self):
        return self._get_prop('@type')

    @property
    def action(self):
        return self._get_prop('action')

    @property
    def actor(self):
        return self._get_prop('actor')

    @property
    def duration(self):
        return self._get_prop('duration')

    @property
    def edApp(self):
        return self._get_prop('edApp')

    @property
    def endedAtTime(self):
        return self._get_prop('endedAtTime')

    @property
    def generated(self):
        return self._get_prop('generated')

    @property
    def group(self):
        return self._get_prop('group')

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')
    
    @property
    def object(self):
        return self._get_prop('object')

## Derived Events
class AnnotationEvent(Event):

    def __init__(self,
            action = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['ANNOTATION'])
        self._set_str_prop('@type', Event.Types['ANNOTATION'])

        if action not in Action.AnnotationActions:
            raise TypeError('action must be in Action.AnnotationActions')
        else:
            self._set_str_prop('action', Action.AnnotationActions[action])

class AssessmentEvent(Event):
    
    def __init__(self,
            action = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['ASSESSMENT'])
        self._set_str_prop('@type', Event.Types['ASSESSMENT'])

        if action not in Action.AssessmentActions:
            raise TypeError('action must be in Action.AssessmentActions')
        else:
            self._set_str_prop('action', Action.AssessmentActions[action])

class AssessmentItemEvent(Event):
    
    def __init__(self,
            action = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['ASSESSMENT_ITEM'])
        self._set_str_prop('@type', Event.Types['ASSESSMENT_ITEM'])

        if action not in Action.AssessmentItemActions:
            raise TypeError('action must be in Actions.AssessmentItemActions')
        else:
            self._set_str_prop('action', Action.AssessmentItemActions[action])

class AssignableEvent(Event):
    
    def __init__(self,
            action = None,
            event_object = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['ASSIGNABLE'])
        self._set_str_prop('@type', Event.Types['ASSIGNABLE'])

        if action not in Action.AssignableActions:
            raise TypeError('action must be in Action.AssignableActions')
        else:
            self._set_str_prop('action', Action.AssignableActions[action])

        if event_object and not( isinstance(event_object, entities.AssignableDigitalResource)):
            raise TypeError('event_object must implement AssignableDigitalResource')
        else:
            self._set_obj_prop('object', event_object)

class MediaEvent(Event):

    def __init__(self,
            action = None,
            event_object = None,
            mediaLocation = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['MEDIA'])
        self._set_str_prop('@type', Event.Types['MEDIA'])

        if action not in Action.MediaActions:
            raise TypeError('action must be in Action.MediaActions')
        else:
            self._set_str_prop('action', Action.MediaActions[action])

        if event_object and not( isinstance(event_object, entities.MediaObject)):
            raise TypeError('event_object must implement entities.MediaObject')
        else:
            self._set_obj_prop('object', event_object)

        if mediaLocation and not( isinstance(mediaLocation, entities.MediaLocation)):
            raise TypeError('mediaLocation must implement entities.MediaLocation')
        else:
            self._set_obj_prop('mediaLocation', mediaLocation)

    @property
    def mediaLocation(self):
        return self._get_prop('mediaLocation')

class NavigationEvent(Event):

    def __init__(self,
            navigatedFrom = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['NAVIGATION'])
        self._set_str_prop('@type', Event.Types['NAVIGATION'])
        self._set_str_prop('action', Action.ReadingActions['NAVIGATED_TO'])

        if navigatedFrom and not( isinstance(navigatedFrom, entities.DigitalResource)):
            raise TypeError('navigatedFrom must implement entities.DigitalResource')
        else:
            self._set_obj_prop('navigatedFrom', navigatedFrom)

    @property
    def navigatedFrom(self):
        return self._get_prop('navigatedFrom')

class OutcomeEvent(Event):

    def __init__(self,
                 action = None,
                 event_object = None,
                 generated = None,
                 **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['OUTCOME'])
        self._set_str_prop('@type', Event.Types['OUTCOME'])
                
        if action not in Action.OutcomeActions:
            raise TypeError('action must be in Action.OutcomeActions')
        else:
            self._set_str_prop('action', Action.OutcomeActions[action])

        if event_object and not( isinstance(event_object, entities.Attempt)):
            raise TypeError('event_object must implement entities.Attempt')
        else:
            self._set_obj_prop('object', event_object)

        if generated and not( isinstance(generated, entities.Result)):
            raise TypeError('generated must implement entities.Result')
        else:
            self._set_obj_prop('generated', generated)

class ViewEvent(Event):

    def __init__(self, **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['VIEW'])
        self._set_str_prop('@type', Event.Types['VIEW'])
        self._set_str_prop('action', Action.ReadingActions['VIEWED'])

