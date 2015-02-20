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


_CREATETIME = '2015-01-01T06:00:00.000Z'
_MODTIME = '2015-02-02T11:30:00.000Z'
_STARTTIME = '2015-02-15T10:15:00.000Z'
_ENDTIME = '2015-02-15T11:05:00.000Z'
_PUBTIME = '2015-01-15T09:30:00.000Z'
_ACTTIME = '2015-01-16T05:00:00.000Z'
_SHOWTIME = _ACTTIME
_STARTONTIME = _ACTTIME
_SUBMITTIME = '2015-02-28T11:59:59.000Z'


### NOTE
###
### FIXTURE_DIR assumes that the caliper fixtures repo contents are symlinked
### into the caliper_tests module's directory in a 'fixtures' subdirectory so
### that the tests can find all the json fixture files in that sub-directory
###
_FIXTURE_DIR = os.path.dirname(caliper_tests.__file__) + os.path.sep + 'fixtures' + os.path.sep

## general state and utility functions used by many tests
def get_testing_options():
    return caliper.base.HttpOptions(
        host='http://httpbin.org/post',
        api_key='6xp7jKrOSOWOgy3acxHFWA')

def get_fixture(fixture_name):
    loc = _FIXTURE_DIR+fixture_name+'.json'
    r = ''
    if os.path.exists(loc):
        with open(loc,'r') as f:
            r = f.read().replace('\n','')
    return json.dumps(json.loads(r), sort_keys=True)

### Shared entity resources ###
## build a test learning context
def build_student_554433():
    return caliper.entities.Person(
        entity_id = 'https://some-university.edu/user/554433',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_AmRev101_course_section():
    return caliper.entities.CourseSection(
        entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101',
        semester = 'Spring-2014',
        courseNumber = 'AmRev-101',
        # sectionNumber = '001',
        label = 'Am Rev 101',
        name = 'American Revolution 101',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_assessment_tool_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://com.sat/super-assessment-tool',
            name = 'Super Assessment Tool',
            dateCreated = _CREATETIME
            ),
        lisOrganization = build_AmRev101_course_section()
        )

def build_video_media_tool_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://com.sat/super-media-tool',
            name = 'Super Media Tool',
            dateCreated = _CREATETIME,
            dateModified = _MODTIME
            ),
        lisOrganization = build_AmRev101_course_section()
        )

def build_readium_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://github.com/readium/readium-js-viewer',
            name = 'Readium',
            dateCreated = _CREATETIME,
            dateModified = _MODTIME
            ),
        lisOrganization = build_AmRev101_course_section()
        )

## build a test EPUB volume
def build_epub_vol43():
    return caliper.entities.EpubVolume(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)',
        name = 'The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_epub_subchap431():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
        name = 'Key Figures: George Washington',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_epub_subchap432():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/2)',
        name = 'Key Figures: Lord North',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_epub_subchap433():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/3)',
        name = 'Key Figures: John Adams',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_epub_subchap434():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/4)',
        name = 'The Stamp Act Crisis',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )


## build a course landing page
def build_AmRev101_landing_page():
    return caliper.entities.WebPage(
        entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/index.html',
        name = 'American Revolution 101 Landing Page',
        isPartOf = build_AmRev101_course_section(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )


### Annotation Profile ###
## build test annotations
def build_bookmark_annotation(target = None):
    return caliper.entities.BookmarkAnnotation(
        entity_id = 'https://someEduApp.edu/bookmarks/00001',
        bookmarkNotes = 'The Intolerable Acts (1774)--bad idea Lord North',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        target = target
        )

def build_highlight_annotation(target = None):
    selection = caliper.entities.TextPositionSelector(start='455', end='489')
    return caliper.entities.HighlightAnnotation(
        entity_id = 'https://someEduApp.edu/highlights/12345',
        selection = selection,
        selectionText = 'Life, Liberty and the pursuit of Happiness',
        target = target,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_shared_annotation(target = None):
    return caliper.entities.SharedAnnotation(
        entity_id = 'https://someEduApp.edu/shared/9999',
        withAgents = [
            caliper.entities.Person(
                entity_id = 'https://some-university.edu/students/657585',
                dateCreated = _CREATETIME,
                dateModified = _MODTIME
                ),
            caliper.entities.Person(
                entity_id = 'https://some-university.edu/students/667788',
                dateCreated = _CREATETIME,
                dateModified = _MODTIME
                )
            ],
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_tag_annotation(target = None):
    return caliper.entities.TagAnnotation(
        entity_id = 'https://someEduApp.edu/tags/7654',
        tags = ['to-read', '1765', 'shared-with-project-team'],
        target = target,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

## build general annotation event
def build_annotation_event(learning_context = None,
                           annotation = None,
                           index = None,
                           target = None,
                           action = None):
    return caliper.events.AnnotationEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = annotation,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = target.isPartOf,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            index = index
            ),
        startedAtTime = _STARTTIME
        )

### Assignable Profile ###
## build assignable event
def build_assessment_assignable_event(learning_context = None,
                                      assessment = None,
                                      action = None):
    return caliper.events.AssignableEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = assessment,
        generated = caliper.entities.Attempt(
            entity_id = '{0}/{1}'.format(assessment.id, 'attempt1'),
            assignable_id = assessment.id,
            actor_id = learning_context.agent.id,
            count = 1,
            dateCreated = _CREATETIME,
            startedAtTime = _STARTTIME),
        startedAtTime = _STARTTIME
        )

### Assessment Profile and Outcome Profile ###
## build a test assessment
def build_assessment_items():
    _id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item'
    _name = 'Assessment Item'
    return [caliper.entities.AssessmentItem(
               entity_id = '{0}{1}'.format(_id,particle),
               name = '{0} {1}'.format(_name,particle),
               isPartOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
               maxAttempts = 2,
               maxSubmits = 2,
               maxScore = 1)
            for particle in ['1','2','3']
        ]

def build_assessment():
    return caliper.entities.Assessment(
        entity_id = 'https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1',
        name = 'American Revolution - Key Figures Assessment',
        isPartOf = 'https://some-university.edu/politicalScience/2014/american-revolution-101',
        datePublished = _PUBTIME,
        dateToActivate = _ACTTIME,
        dateToShow = _SHOWTIME,
        dateToStartOn = _STARTONTIME,
        dateToSubmit = _SUBMITTIME,
        maxAttempts = 2,
        maxSubmits = 2,
        maxScore = 3, # WARN original value is 5.0d, says Java impl
        assessmentItems = build_assessment_items(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

## build a test assessment attempt
def build_assessment_attempt(learning_context=None,
                             assessment=None):
    return caliper.entities.Attempt(
        entity_id = '{0}/{1}'.format(assessment.id,'attempt1'),
        assignable_id = assessment.id,
        actor_id = learning_context.agent.id,
        count = 1,
        dateCreated = _CREATETIME,
        startedAtTime = _STARTTIME
        )

## build a test assessment item attempt
def build_assessment_item_attempt(learning_context=None,
                                  assessment=None):
    return caliper.entities.Attempt(
        entity_id = '{0}/{1}'.format(assessment.id,'/item1/attempt1'),
        assignable_id = assessment.id,
        actor_id = learning_context.agent.id,
        count = 1,
        dateCreated = _CREATETIME,
        startedAtTime = _STARTTIME
        )

## build a test assessment item response
def build_assessment_item_response(assessment=None,
                                   attempt=None,
                                   value=None):
    return caliper.entities.Response(
        entity_id = '{0}/{1}'.format(assessment.id,'/item1/response1'),
        assignable_id = attempt.assignable,
        actor_id = attempt.actor,
        attempt = attempt,
        dateCreated = _CREATETIME,
        startedAtTime = _STARTTIME,
        value = value
        )

## build a test assessment result
def build_assessment_result(learning_context=None,
                            attempt=None):
    return caliper.entities.Result(
        entity_id = '{0}/{1}'.format(attempt.id, 'result'),
        actor_id = learning_context.agent.id,
        assignable_id = attempt.assignable,
        comment = 'Well done.',
        curvedTotalScore = 3.0,
        curveFactor = 0.0,
        extraCreditScore = 0.0,
        normalScore = 3.0,
        penaltyScore = 0.0,
        scoredBy = learning_context.edApp,
        totalScore = 3.0,
        dateCreated = _CREATETIME
        )

## Asessement event
def build_assessment_event(learning_context = None,
                           assessment = None,
                           attempt = None,
                           action = None):
    return caliper.events.AssessmentEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = assessment,
        generated = attempt,
        startedAtTime = _STARTTIME
        )

def build_assessment_item_event(learning_context = None,
                                assessment_item = None,
                                generated = None,
                                action = None):
    return caliper.events.AssessmentItemEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        isTimeDependent = False,
        event_object = assessment_item,
        generated = generated,
        startedAtTime = _STARTTIME
        )

def build_assessment_outcome_event(learning_context = None,
                                   attempt = None,
                                   result = None,
                                   action = None):
    return caliper.events.OutcomeEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = attempt,
        generated = result,
        startedAtTime = _STARTTIME
        )

### Media Profile ###
## Media event
def build_video_media_event(learning_context = None,
                            event_object = None,
                            location = None,
                            action = None):
    return caliper.events.MediaEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = location,
        startedAtTime = _STARTTIME
        )

### Reading Profile ###
## build a test video and location
def build_video_with_learning_objective():
    return caliper.entities.VideoObject(
        entity_id = 'https://com.sat/super-media-tool/video/video1',
        name = 'American Revolution - Key Figures Video',
        alignedLearningObjective = [caliper.entities.LearningObjective(
            entity_id = 'http://americanrevolution.com/personalities/learn',
            dateCreated = _CREATETIME
            )],
        duration = 1420,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_video_media_location():
    return caliper.entities.MediaLocation(
        entity_id = build_video_with_learning_objective().id,
        currentTime = 710,
        dateCreated = _CREATETIME
        )

## Navigation event
def build_epub_navigation_event(learning_context = None,
                                event_object = None,
                                from_resource = None,
                                target = None,
                                action = None):
    return caliper.events.NavigationEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = event_object,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            index = 1
            ),
        navigatedFrom = from_resource,
        startedAtTime = _STARTTIME
        )

## View event
def build_epub_view_event(learning_context = None,
                          event_object = None,
                          target = None,
                          action = None):
    return caliper.events.ViewEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = event_object,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            index = 1,
            ),
        startedAtTime = _STARTTIME
        )



### Session profile

def build_readium_session(learning_context=None):
    return caliper.entities.Session(
        entity_id = 'https://github.com/readium/session-123456789',
        name = 'session-123456789',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        startedAtTime = _STARTTIME,
        actor = learning_context.agent
        )

## Session event
def build_session_event(learning_context = None,
                        actor = None,
                        event_object = None,
                        session = None,
                        target = None,
                        action = None):
    the_endtime = None
    if target and (isinstance(target, caliper.entities.Session)):
        the_target = target
        the_target.endedAtTime = the_endtime = _ENDTIME
    else:
        the_target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = target.isPartOf,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            index = 1)
    return caliper.events.SessionEvent(
        edApp = learning_context.edApp,
        lisOrganization = learning_context.lisOrganization,
        actor = actor,
        action = action,
        event_object = event_object,
        generated = session,
        target = the_target,
        startedAtTime = _STARTTIME,
        endedAtTime = the_endtime
        )
