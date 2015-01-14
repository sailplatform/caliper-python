# -*- coding: utf-8 -*-
# Caliper-python testing package (testing util functions)
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

import sys, os
sys.path.insert(0, os.path.abspath('..'))
import caliper, caliper_tests
import json


_LMT = 1402965614516
_SAT = 1402965614516

## general state and utility functions used by many tests
def get_testing_options():
    return caliper.base.HttpOptions(
        host='http://httpbin.org/post',
        api_key='6xp7jKrOSOWOgy3acxHFWA')

def get_fixture_str(fixture=None):
    return json.dumps(json.loads(fixture), sort_keys=True)

## build a test learning context
def build_student_554433():
    return caliper.entities.Person(
        entity_id = 'https://some-university.edu/user/554433',
        lastModifiedTime = _LMT
        )

def build_AmRev101_course_section():
    return caliper.entities.CourseSection(
        entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101',
        semester = 'Spring-2014',
        courseNumber = 'AmRev-101',
        # sectionNumber = '001',
        label = 'Am Rev 101',
        name = 'American Revolution 101',
        lastModifiedTime = _LMT
        )

def build_readium_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://github.com/readium/readium-js-viewer',
            name = 'Readium',
            lastModifiedTime = _LMT
            ),
        lisOrganization = build_AmRev101_course_section()
        )

def build_assessment_tool_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://com.sat/super-assessment-tool',
            name = 'Super Assessment Tool',
            lastModifiedTime = _LMT
            ),
        lisOrganization = build_AmRev101_course_section()
        )

### Assessment Profile ###

## build a test assessment
def build_assessment_items():
    _id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item'
    _name = 'Assessment Item'
    return [caliper.entities.AssessmentItem(
               entity_id = '{0}{1}'.format(_id,particle),
               name = '{0} {1}'.format(_name,particle),
               partOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
               maxAttempts = 2,
               maxSubmits = 2,
               maxScore = 1)
            for particle in ['1','2','3']
        ]

def build_assessment():
    return caliper.entities.Assessment(
        entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
        name = 'American Revolution - Key Figures Assessment',
        partOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101',
        dateCreated = _LMT,
        datePublished = _LMT,
        dateToActivate = _LMT,
        dateToShow = _LMT,
        dateToStartOn = _LMT,
        dateToSubmit = _LMT,
        maxAttempts = 2,
        maxSubmits = 2,
        maxScore = 3, # WARN original value is 5.0d, says Java impl
        assessmentItems = build_assessment_items(),
        lastModifiedTime = _LMT
        )
    pass

## build a test attempt
def build_assessment_attempt(learning_context=None,
                             assessment=None,):
    return caliper.entities.Attempt(
        entity_id = '{0}/{1}'.format(assessment.id,'attempt1'),
        assignable = assessment,
        actor = learning_context.agent,
        count = 1
        )
    pass

## Asessement event
def build_assessment_event(learning_context = None,
                           assessment = None,
                           action = None,
                           attempt = None,
        ):
    return caliper.events.AssessmentEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = assessment,
        generated = attempt,
        startedAtTime = _SAT
        )

### Reading Profile ###

## build a test epub volume
def build_epub_vol43():
    return caliper.entities.EpubVolume(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)',
        name = 'The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)',
        lastModifiedTime = _LMT
        )

def build_epub_subchap431():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
        name = 'Key Figures: George Washington',
        partOf = build_epub_vol43(),
        lastModifiedTime = _LMT
        )

## related resources
def build_AmRev101_landing_page():
    return caliper.entities.WebPage(
        entity_id = 'AmRev-1010-landingPage',
        name = 'American Revolution 101 Landing Page',
        partOf = build_epub_vol43(),
        lastModifiedTime = _LMT
        )

## View event
def build_epub_view_event(learning_context = None,
                          event_object = None,
                          action = None,
                          target = None):
    return caliper.events.ViewEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            partOf = event_object,
            lastModifiedTime = _LMT,
            index = 1,
            ),
        startedAtTime = _SAT
        )

## Navigation event
def build_epub_navigation_event(learning_context = None,
                                event_object = None,
                                action = None,
                                from_resource = None,
                                target = None):
    return caliper.events.NavigationEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            partOf = event_object,
            lastModifiedTime = _LMT,
            index = 1
            ),
        navigatedFrom = from_resource,
        startedAtTime = _SAT
        )
