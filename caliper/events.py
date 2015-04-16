# -*- coding: utf-8 -*-
# Caliper-python package, events module
#
# Copyright (c) 2015 IMS Global Learning Consortium, Inc. All Rights Reserved.
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

from __future__ import absolute_import



from caliper.base import BaseEvent, CaliperSerializable
from caliper import entities, profiles
from caliper.extern import foaf, schemadotorg

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
        'READING': 'http://purl.imsglobal.org/ctx/caliper/v1/ReadingEvent',
        'SESSION': 'http://purl.imsglobal.org/ctx/caliper/v1/SessionEvent',
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
        'READING': 'http://purl.imsglobal.org/caliper/v1/ReadingEvent',
        'SESSION': 'http://purl.imsglobal.org/caliper/v1/SessionEvent',
        'VIEW': 'http://purl.imsglobal.org/caliper/v1/ViewEvent',
        }

    def __init__(self,
            action = None,
            actor = None,
            duration = None,
            edApp = None,
            endedAtTime = None,
            event_object = None,
            generated = None,
            group = None,
            startedAtTime = None,
            target = None,
            **kwargs):
        BaseEvent.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['EVENT'])
        self._set_str_prop('@type', Event.Types['EVENT'])

        if action and (action not in profiles.CaliperProfile.Actions.values()):
            raise ValueError('action must be in the list of CaliperProfile actions')
        else:
            self._set_str_prop('action', action)

        if actor and (not isinstance(actor, foaf.Agent)):
            raise TypeError('actor must implement foaf.Agent')
        else:
            self._set_obj_prop('actor', actor)

        self._set_str_prop('duration', duration)
                    
        if edApp and (not isinstance(edApp, entities.SoftwareApplication)):
            raise TypeError('edApp must implement entities.SoftwareApplication')
        else:
            self._set_obj_prop('edApp', edApp)

        self._set_str_prop('endedAtTime', endedAtTime)

        if event_object and (not isinstance(event_object, CaliperSerializable)):
            raise TypeError('event_object must implement CaliperSerializable')
        else:
            self._set_obj_prop('object', event_object)

        if generated and (not isinstance(generated, entities.Generatable)):
            raise TypeError('generated must implement entities.Generatable')
        else:
            self._set_obj_prop('generated', generated)

        if group and (not isinstance(group, entities.Organization)):
            raise TypeError('group must implement entities.Organization')
        else:
            self._set_obj_prop('group', group)

        if not startedAtTime:
            raise ValueError('startedAtTime must have a time value')
        else:
            self._set_str_prop('startedAtTime', startedAtTime)
            
        if target and (not isinstance(target, entities.Targetable)):
            raise TypeError('target must implement entities.Targetable')
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
    def object(self):
        return self._get_prop('object')

    @property
    def startedAtTime(self):
        return self._get_prop('startedAtTime')

    @property
    def target(self):
        return self._get_prop('target')


## Derived Events
class AnnotationEvent(Event):

    def __init__(self,
            action = None,
            actor = None,
            event_object = None,
            generated = None,
            **kwargs):
        Event.__init__(self,
                       **kwargs)
        self._set_str_prop('@context', Event.Contexts['ANNOTATION'])
        self._set_str_prop('@type', Event.Types['ANNOTATION'])

        if action not in profiles.AnnotationProfile.Actions.values():
            raise ValueError('action must be in the list of AnnotationProfile actions')
        else:
            self._set_str_prop('action', action)

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.DigitalResource):
            raise TypeError('event_object must implement entities.DigitalResource')
        else:
            self._set_obj_prop('object', event_object)

        if not isinstance(generated, entities.Annotation):
            raise TypeError('generated must implement entities.Annotation')
        else:
            self._set_obj_prop('generated', generated)


class AssessmentEvent(Event):
    
    def __init__(self,
            action = None,
            actor = None,
            event_object = None,
            generated = None,
            **kwargs):
        Event.__init__(self,
                       target = None,
                       **kwargs)
        self._set_str_prop('@context', Event.Contexts['ASSESSMENT'])
        self._set_str_prop('@type', Event.Types['ASSESSMENT'])

        if action not in profiles.AssessmentProfile.Actions.values():
            raise ValueError('action must be in the list of AssessmentProfile actions')
        else:
            self._set_str_prop('action', action)

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.Assessment):
            raise TypeError('event_object must implement entities.Assessment')
        else:
            self._set_obj_prop('object', event_object)

        if generated and (not isinstance(generated, entities.Attempt)):
            raise TypeError('generated must implement entities.Attempt')
        else:
            self._set_obj_prop('generated', generated)


class AssessmentItemEvent(Event):
    
    def __init__(self,
            action = None,
            actor = None,
            event_object = None,
            generated = None,
            **kwargs):
        Event.__init__(self,
                       target = None,
                       **kwargs)
        self._set_str_prop('@context', Event.Contexts['ASSESSMENT_ITEM'])
        self._set_str_prop('@type', Event.Types['ASSESSMENT_ITEM'])

        if action not in profiles.AssessmentItemProfile.Actions.values():
            raise ValueError('action must be in the list of AssessmentItemProfile actions')
        else:
            self._set_str_prop('action', action)

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.AssessmentItem):
            raise TypeError('event_object must implement entities.AssessmentItem')
        else:
            self._set_obj_prop('object', event_object)

        if not isinstance(generated, entities.Generatable):
            raise TypeError('generated must implement entities.Generatable')
        else:
            self._set_obj_prop('generated', generated)


class AssignableEvent(Event):
    
    def __init__(self,
            action = None,
            event_object = None,
            generated = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['ASSIGNABLE'])
        self._set_str_prop('@type', Event.Types['ASSIGNABLE'])

        if action not in profiles.AssignableProfile.Actions.values():
            raise TypeError('action must be in the list of AssignableProfile actions')
        else:
            self._set_str_prop('action', action)

        if  not isinstance(event_object, entities.AssignableDigitalResource):
            raise TypeError('event_object must implement AssignableDigitalResource')
        else:
            self._set_obj_prop('object', event_object)

        if not isinstance(generated, entities.Attempt):
            raise TypeError('generated must implement entities.Attempt')
        else:
            self._set_obj_prop('generated', generated)


class MediaEvent(Event):

    def __init__(self,
            action = None,
            actor = None,
            event_object = None,
            target = None,
            **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['MEDIA'])
        self._set_str_prop('@type', Event.Types['MEDIA'])

        if action not in profiles.MediaProfile.Actions.values():
            raise TypeError('action must be in the list of MediaProfile actions')
        else:
            self._set_str_prop('action', action)

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.MediaObject):
            raise TypeError('event_object must implement entities.MediaObject')
        else:
            self._set_obj_prop('object', event_object)

        if target and not( isinstance(target, entities.MediaLocation)):
            raise TypeError('target must implement entities.MediaLocation')
        else:
            self._set_obj_prop('target', target)


class NavigationEvent(Event):

    def __init__(self,
                 actor = None,
                 event_object = None,
                 navigatedFrom = None,
                 target = None,
                 **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['NAVIGATION'])
        self._set_str_prop('@type', Event.Types['NAVIGATION'])
        self._set_str_prop('action', profiles.CaliperProfile.Actions['NAVIGATED_TO'])

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.DigitalResource):
            raise TypeError('event_object must implement entities.DigitalResource')
        else:
            self._set_obj_prop('object', event_object)

        if navigatedFrom and not( isinstance(navigatedFrom, entities.DigitalResource)):
            raise TypeError('navigatedFrom must implement entities.DigitalResource')
        else:
            self._set_obj_prop('navigatedFrom', navigatedFrom)

        if not isinstance(target, entities.DigitalResource):
            raise TypeError('target must implement entities.DigitalResource')
        else:
            self._set_obj_prop('target', target)

    @property
    def navigatedFrom(self):
        return self._get_prop('navigatedFrom')


class OutcomeEvent(Event):

    def __init__(self,
                 action = None,
                 event_object = None,
                 generated = None,
                 **kwargs):
        Event.__init__(self,
                       target = None,
                       **kwargs)
        self._set_str_prop('@context', Event.Contexts['OUTCOME'])
        self._set_str_prop('@type', Event.Types['OUTCOME'])

        if  action not in profiles.OutcomeProfile.Actions.values():
            raise TypeError('action must be in the list of OutcomeProfile actions')
        else:
            self._set_str_prop('action', action)
                
        if not isinstance(event_object, entities.Attempt):
            raise TypeError('event_object must implement entities.Attempt')
        else:
            self._set_obj_prop('object', event_object)

        if not isinstance(generated, entities.Result):
            raise TypeError('generated must implement entities.Result')
        else:
            self._set_obj_prop('generated', generated)


class ReadingEvent(Event):

    def __init__(self,
                 action = None,
                 actor = None,
                 event_object = None,
                 target = None,
                 **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['READING'])
        self._set_str_prop('@type', Event.Types['READING'])

        if action not in profiles.ReadingProfile.Actions.values():
            raise TypeError('action must be in the list of ReadingProfile actions')
        else:
            self._set_str_prop('action', action)

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.DigitalResource):
            raise TypeError('event_object must implement entities.DigitalResource')
        else:
            self._set_obj_prop('object', event_object)

        if target and not( isinstance(target, entities.Frame)):
            raise TypeError('target must implement entities.Frame')
        else:
            self._set_obj_prop('target', target)


class SessionEvent(Event):

    def __init__(self,
                 action = None,
                 actor = None,
                 endedAtTime = None,
                 event_object = None,
                 generated = None,
                 target = None,
                 **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['SESSION'])
        self._set_str_prop('@type', Event.Types['SESSION'])

        if action not in profiles.SessionProfile.Actions.values():
            raise TypeError('action must be in the list of SessionProfile actions')
        else:
            self._set_str_prop('action', action)

        if action == profiles.SessionProfile.Actions['TIMED_OUT']:
            if not isinstance(actor, entities.SoftwareApplication):
                raise TypeError('for TIMED_OUT action, actor must implement entities.SoftwareApplication')
        else:
            if not isinstance(actor, entities.Person):
                raise TypeError('for actions other than TIMED_OUT, actor must implement entities.Person')
        self._set_obj_prop('actor', actor)
            
        if not isinstance(event_object, entities.SoftwareApplication):
            raise TypeError('event_object must implement entities.SoftwareApplication')
        else:
            self._set_obj_prop('object', event_object)

        if action == profiles.SessionProfile.Actions['LOGGED_IN']:
            if not isinstance(generated, entities.Session):
                raise TypeError('for LOGGED_IN action, generated must implement entities.Session')
            else:
                self._set_obj_prop('generated', generated)
            if not isinstance(target, entities.DigitalResource):
                raise TypeError('for LOGGED_IN, target must impelement entities.DigitalResource')
        else:
            if not isinstance(target, entities.Session):
                raise TypeError('for actions other than LOGGED_IN, target must impelement entities.Session')
            if not endedAtTime:
                raise ValueError('for actions other than LOGGED_IN, endedAtTime must have a time value')
            else:
                self._set_str_prop('endedAtTime', endedAtTime)
        self._set_obj_prop('target', target)


class ViewEvent(Event):

    def __init__(self,
                 action = None,
                 actor = None,
                 event_object = None,
                 **kwargs):
        Event.__init__(self, **kwargs)
        self._set_str_prop('@context', Event.Contexts['VIEW'])
        self._set_str_prop('@type', Event.Types['VIEW'])

        if action not in profiles.ReadingProfile.Actions.values():
            raise TypeError('action must be in the list of ReadingProfile actions')
        else:
            self._set_str_prop('action', action)

        if not isinstance(actor, entities.Person):
            raise TypeError('actor must implement entities.Person')
        else:
            self._set_obj_prop('actor', actor)

        if not isinstance(event_object, entities.DigitalResource):
            raise TypeError('event_object must implement entities.DigitalResource')
        else:
            self._set_obj_prop('object', event_object)
            
