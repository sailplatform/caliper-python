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
from .actions import Action
from .entities import (Assessment, AssessmentItem, AssignableDigitalResource,
                       Attempt, DigitalResource, LearningContext, MediaLocation,
                       MediaObject, Outcome, )

## Base profile class

class Profile(BaseProfile):

    def __init__(self,
            actions = None,
            fromResources = None,
            generateds = None,
            learningContext = None,
            targets = None,
            **kwargs):
        BaseProfile.__init__(self, **kwargs)

        if isinstance(actions, collections.MutableSequence):
            if all( isinstance(item, six.string_types) for item in actions):
                self._set_list_prop('actions', actions)
            else:
                raise TypeError('actions must be a list of action strings')
        else:
            self._set_list_prop('actions', None)

        if isinstance(fromResources, collections.MutableSequence):
            if all( isinstance(item, DigitalResource) for item in fromResources):
                self._set_list_prop('fromResources', fromResources)
            else:
                raise TypeError('fromResources must be a list of entities.DigitalResources')
        else:
            self._set_list_prop('fromResources', None)

        if isinstance(generateds, collections.MutableSequence):
            if all( isinstance(item, CaliperSerializable) for item in generateds):
                self._set_list_prop('generateds', generateds)
            else:
                raise TypeError('generateds must be a list of objects implementing CaliperSerializable')
        else:
            self._set_list_prop('generateds', None)

        if isinstance(targets, collections.MutableSequence):
            if all( isinstance(item, CaliperSerializable) for item in targets):
                self._set_list_prop('targets', targets)
            else:
                raise TypeError('targets must be a list of objects implementing CaliperSerializable')
        else:
            self._set_list_prop('targets', None)

        if learningContext and (not isinstance(learningContext, LearningContext)):
            raise TypeError('learningContext must implement entities.LearningContext')
        else:
            self._set_obj_prop('learningContext', learningContext)

    @property
    def actions(self):
        return self._get_prop('actions')

    def add_action(self, new_action=None):
        if not isinstance(new_action, six.string_types):
            raise TypeError('new action must be an action string')
        else:
            self._append_list_prop('actions', new_action)

    @property
    def fromResources(self):
        return self._get_prop('fromResources')

    def add_fromResource(self, new_from_resource=None):
        if not isinstance(new_from_resource, CaliperSerializable):
            raise TypeError('new from resource must be an object implementing CaliperSerializable')
        else:
            self._append_list_prop('fromResources', new_from_resource)

    @property
    def generateds(self):
        return self._get_prop('generateds')

    def add_generated(self, new_generated=None):
        if not isinstance(new_generated, CaliperSerializable):
            raise TypeError('new generated must be an object implementing CaliperSerializable')
        else:
            self._append_list_prop('generateds', new_generated)

    @property
    def learningContext(self):
        return self._get_prop('learningContext')

    @property
    def targets(self):
        return self._get_prop('targets')

    def add_target(self, new_target=None):
        if not isinstance(new_target, CaliperSerializable):
            raise TypeError('new target must be an object impelementing CaliperSerializable')
        else:
            self._append_list_prop('targets', new_target)

            
## Derived profiles ##

class AnnotationProfile(Profile):

    def __init__(self,
            annotations = None,
            **kwargs):
        Profile.__init__(self, **kwargs)

        if isinstance( annotations, collections.MutableSequence):
            if all( isinstance(item, Annotation) for item in annotations):
                self._set_list_prop('annotations', annotations)
            else:
                raise TypeError('annotations must be a list of entities.Annotation')
        else:
            self._set_list_prop('annotations', None)

    @property
    def annotations(self):
        return self._get_prop('annotations')
        
class AssessmentProfile(Profile):

    def __init__(self,
            assessment = None,
            itemsAttempted = None,
            **kwargs):
        Profile.__init__(self, **kwargs)

        if assessment and (not isinstance(assessment, Assessment)):
            raise TypeError('assessment must implement entities.Assessment')
        else:
            self._set_obj_prop('assessment', assessment)

        if isinstance( itemsAttempted, collections.MutableSequence):
            if all( isinstance(item, AssessmentItem) for item in itemsAttempted):
                self._set_list_prop('itemsAttempted', itemsAttempted)
            else:
                raise TypeError('itemsAttempted must be a list of entities.AssessmentItem')
        else:
            self._set_list_prop('itemsAttempted', None)

    @property
    def assessment(self):
        return self._get_prop('assessment')
            
    @property
    def itemsAttempted(self):
        return self._get_prop('itemsAttempted')

    def add_item_attempted(self, new_attempt=None):
        if not isinstance(new_attempt, AssessmentItem):
            raise TypeError('new attempt must be an object implementing AssessmentItem')
        else:
            self._append_list_prop('itemsAttempted', new_attempt)

class AssignableProfile(Profile):

    def __init__(self,
            assignable = None,
            attempts = None,
            **kwargs):
        Profile.__init__(self, **kwargs)

        if assignable and (not isinstance(assignable, AssignableDigitalResource)):
            raise TypeError('assignable must implement entities.AssignableDigitalResource')
        else:
            self._set_obj_prop('assignable', assignable)

        if isinstance( attempts, collections.MutableSequence):
            if all( isinstance(item, Attempt) for item in attempts):
                self._set_list_prop('attempts', attempts)
            else:
                raise TypeError('attempts must be a list of entities.Attempt')
        else:
            self._set_list_prop('attempts', None)

    @property
    def assignable(self):
        return self._get_prop('assignable')

    @property
    def attempts(self):
        return self._get_prop('attempts')

    def add_attempt(self, new_attempt=None):
        if not isinstance(new_attempt, Attempt):
            raise TypeError('new attmept must be an object implementing Attempt')
        else:
            self._append_list_prop('attempts', new_attempt)
        
class MediaProfile(Profile):

    def __init__(self,
            mediaObject = None,
            mediaLocations = None,
            **kwargs):
        Profile.__init__(self, **kwargs)

        if mediaObject and (not isinstance(mediaObject, MediaObject)):
            raise TypeError('mediaObject must implement entities.MediaObject')
        else:
            self._set_obj_prop('mediaObject', mediaObject)

        if isinstance( mediaLocations, collections.MutableSequence):
            if all( isinstance(item, MediaLocation) for item in mediaLocations):
                self._set_list_prop('mediaLocations', mediaLocations)
            else:
                raise TypeError('mediaLocations must be a list of entities.MediaLocation')
        else:
            self._set_list_prop('mediaLocations', None)

    @property
    def mediaObject(self):
        return self._get_prop('mediaObject')

    @property
    def mediaLocations(self):
        return self._get_prop('mediaLocations')

    def add_mediaLocation(self, new_location=None):
        if not isinstance(new_location, MediaLocation):
            raise TypeError('new media location must be an object implementing MediaLocation')
        else:
            self._append_list_prop('mediaLocations', new_location)
        
class OutcomeProfile(Profile):

    def __init__(self,
            assignable = None,
            outcomes = None,
            **kwargs):
        Profile.__init__(self, **kwargs)

        if assignable and (not isinstance(assignable, AssignableDigitalResource)):
            raise TypeError('assignable must implement entities.AssignableDigitalResource')
        else:
            self._set_obj_prop('assignable', assignable)

        if isinstance( outcomes, collections.MutableSequence):
            if all( isinstance(item, Outcome) for item in outcomes):
                self._set_list_prop('outcomes', outcomes)
            else:
                raise TypeError('outcomes must be a list of entities.Outcome')
        else:
            self._set_list_prop('outcomes', None)

    @property
    def assignable(self):
        return self._get_prop('assignable')

    @property
    def outcomes(self):
        return self._get_prop('outcomes')

class ReadingProfile(Profile):

    def __init__(self,
            reading = None,
            views = None,
            **kwargs):
        Profile.__init__(self, **kwargs)

        if reading and (not isinstance(reading, DigitalResource)):
            raise TypeError('reading must implement entities.DigitalResource')
        else:
            self._set_obj_prop('reading', reading)

        if isinstance( views, collections.MutableSequence):
            if all( isinstance(item, View) for item in views):
                self._set_list_prop('views', views)
            else:
                raise TypeError('views must be a list of entities.View')
        else:
            self._set_list_prop('views', None)

    @property
    def reading(self):
        return self._get_prop('reading')

    @property
    def views(self):
        return self._get_prop('views')
