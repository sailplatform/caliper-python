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
def getTestingOptions():
    return caliper.base.HttpOptions(
        host='http://httpbin.org/post',
        api_key='6xp7jKrOSOWOgy3acxHFWA')

def getFixtureStr(fixture=None):
    return json.dumps(json.loads(fixture), sort_keys=True)


## build a test learning context
def buildLearningContext():
    return caliper.entities.LearningContext(
        agent = caliper.entities.Person(
            entity_id = 'https://some-university.edu/user/554433',
            lastModifiedTime = _LMT
            ),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://github.com/readium/readium-js-viewer',
            name = 'Readium',
            lastModifiedTime = _LMT
            ),
        lisOrganization = caliper.entities.CourseSection(
            entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101',
            semester = 'Spring-2014',
            courseNumber = 'AmRev-101',
            label = 'Am Rev 101',
            name = 'American Revolution 101',
            lastModifiedTime = _LMT
            )
        )

## Assessment Profile related funcs
def buildAssessment():
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
        maxScore = 3,
        lastModifiedTime = _LMT,
        assessmentItems = [
            caliper.entities.AssessmentItem(
                entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item1',
                name = 'Assessment Item 1',
                partOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
                maxAttempts = 2,
                maxSubmits = 2,
                maxScore = 1
                ),
            caliper.entities.AssessmentItem(
                entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item2',
                name = 'Assessment Item 2',
                partOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
                maxAttempts = 2,
                maxSubmits = 2,
                maxScore = 1
                ),
            caliper.entities.AssessmentItem(
                entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item3',
                name = 'Assessment Item 3',
                partOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
                maxAttempts = 2,
                maxSubmits = 2,
                maxScore = 1
                )
            ]
        )

def buildAssessmentProfile(learning_context=None, assessment=None):
    if not learning_context:
        learning_context = buildLearningContext()
    if not assessment:
        assessment = buildAssessment()
    return caliper.profiles.AssessmentProfile(
        learningContext = learning_context,
        assessment = assessment)

def startAssessment(assessment_profile=None):
    if not assessment_profile:
        assessment_profile = buildAssessmentProfile()
    assessment_profile.add_action(caliper.actions.Action.AssessmentActions['STARTED'])
    assessment_profile.add_generated(
        new_generated = caliper.entities.Attempt(
            entity_id = assessment_profile.assessment.id + '/attempt1',
            assignable = assessment_profile.assessment,
            actor = assessment_profile.learningContext.agent,
            count = 1
            )
        )
    return assessment_profile

def buildAssessmentEvent(assessment_profile=None):
    if not assessment_profile:
        assessment_profile = startAssessment()
    return caliper.events.AssessmentEvent(
        action = assessment_profile.actions[-1],
        edApp = assessment_profile.learningContext.edApp,
        group = assessment_profile.learningContext.lisOrganization,
        actor = assessment_profile.learningContext.agent,
        event_object = assessment_profile.assessment,
        generated = assessment_profile.generateds[-1],
        startedAtTime = _SAT
        )

## Media Profile related funcs
def buildMediaProfile(learning_context=None):
    if not learning_context:
        learning_context=buildLearningContext()
    return caliper.profiles.MediaProfile(
        learningContext = learning_context,
        mediaObject = caliper.entities.VideoObject(
            entity_id = 'https://com.sat/super-media-tool/video/video1',
            name = 'American Revolution - Key Figures Video',
            alignedLearningObjective = [caliper.entities.LearningObjective(
                entity_id = 'http://americanrevolution.com/personalities/learn',
                )],
            duration = 1420,
            lastModifiedTime = _LMT
            ),
        mediaLocation = caliper.entities.MediaLocation(
            entity_id = 'https://com.sat/super-media-tool/video/video1',
            currentTime = 0
            )
        )

def pauseVideo(media_profile=None):
    if not media_profile:
        media_profile = buildMediaProfile()
    media_profile.add_action(caliper.actions.Action.MediaActions['PAUSED'])
    media_profile.add_mediaLocation(
        new_location = caliper.entities.MediaLocation(
            entity_id = media_profile.mediaObject.id,
            currentTime = 710
            )
        )
    return media_profile

def buildMediaEvent(media_profile=None):
    if not media_profile:
        media_profile = buildMediaProfile()
    return caliper.events.MediaEvent(
        action = media_profile.actions[-1],
        edApp = media_profile.learningContext.edApp,
        group = media_profile.learningContext.lisOrganization,
        actor = media_profile.learningContext.agent,
        event_object = media_profile.mediaObject,
        mediaLocation = media_profile.mediaLocations[-1],
        startedAtTime = _SAT
        )

## Reading Profile related funcs
def buildReadingProfile(learning_context=None):
    if not learning_context:
        learning_context = buildLearningContext()
    return caliper.profiles.ReadingProfile(
        learningContext = learning_context,
        reading = caliper.entities.EpubVolume(
            entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)',
            name = 'The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)',
            lastModifiedTime = _LMT
            ),
        )

def navigateToReadingTarget(reading_profile=None):
    if not reading_profile:
        reading_profile = buildReadingProfile()
    reading_profile.add_action(caliper.actions.Action.ReadingActions['NAVIGATED_TO'])
    reading_profile.add_target(
        new_target = caliper.entities.Frame(
            entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
            name = 'Key Figures: George Washington',
            partOf = reading_profile.reading,
            lastModifiedTime = _LMT,
            index = 1
            )
        )
    reading_profile.add_fromResource(
        new_from_resource = caliper.entities.WebPage(
            entity_id = 'AmRev-101-landingPage',
            name = 'American Revolution 101 Landing Page',
            partOf = reading_profile.learningContext.lisOrganization,
            lastModifiedTime = _LMT
            )
        )
    return reading_profile
    
def viewReadingTarget(reading_profile=None):
    if not reading_profile:
        reading_profile = buildReadingProfile()
    reading_profile.add_action(caliper.actions.Action.ReadingActions['VIEWED'])
    reading_profile.add_target(
        new_target = caliper.entities.Frame(
            entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
            name = 'Key Figures: George Washington',
            partOf = reading_profile.reading,
            lastModifiedTime = _LMT,
            index = 1
            )
        )
    return reading_profile

def buildNavigationEvent(reading_profile=None):
    if not reading_profile:
        reading_profile = buildReadingProfile()
    return caliper.events.NavigationEvent(
        action = reading_profile.actions[-1],
        edApp = reading_profile.learningContext.edApp,
        group = reading_profile.learningContext.lisOrganization,
        actor = reading_profile.learningContext.agent,
        event_object = reading_profile.reading,
        navigatedFrom = reading_profile.fromResources[-1],
        target = reading_profile.targets[-1],
        startedAtTime = _SAT
        )
    
def buildViewEvent(reading_profile=None):
    if not reading_profile:
        reading_profile = buildReadingProfile()
    return caliper.events.ViewEvent(
        action = reading_profile.actions[-1],
        edApp = reading_profile.learningContext.edApp,
        group = reading_profile.learningContext.lisOrganization,
        actor = reading_profile.learningContext.agent,
        event_object = reading_profile.reading,
        target = reading_profile.targets[-1],
        startedAtTime = _SAT
        )

