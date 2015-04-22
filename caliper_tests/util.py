# -*- coding: utf-8 -*-
# Caliper-python testing package (testing util functions)
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements. See the NOTICE file distributed with this
# work for additional information.
#
# IMS Caliper is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# IMS Caliper is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#

import sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import caliper, caliper_tests


_DEBUG = False

_CREATETIME = '2015-08-01T06:00:00.000Z'
_MODTIME = '2015-09-02T11:30:00.000Z'
_STARTTIME = '2015-09-15T10:15:00.000Z'
_ENDTIME = '2015-09-15T11:05:00.000Z'
_PUBTIME = '2015-08-15T09:30:00.000Z'
_ACTTIME = '2015-08-16T05:00:00.000Z'
_SHOWTIME = _ACTTIME
_STARTONTIME = _ACTTIME
_SUBMITTIME = '2015-09-28T11:59:59.000Z'
_DURATION = 'PT3000S'
_MEDIA_CURTIME = 710
_MEDIA_DURTIME = 1420
_VERNUM = '1.0'
_VERED = '2nd ed.'


### NOTE
###
### FIXTURE_DIR assumes that the caliper fixtures repo contents are symlinked
### into the caliper_tests module's directory in a 'fixtures' subdirectory so
### that the tests can find all the json fixture files in that sub-directory
###
_FIXTURE_DIR = os.path.dirname(caliper_tests.__file__) + os.path.sep + 'fixtures' + os.path.sep
_FIXTURE_OUT_DIR = os.path.dirname(caliper_tests.__file__) + os.path.sep + 'fixtures_out' + os.path.sep

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

## without DEBUG, a no-op: useful to generate more readable/diffable
## side-by-side comparisons of the stock fixtures with the generated events
def put_fixture(fixture_name, event, debug=_DEBUG):
    if debug:
        loc = _FIXTURE_OUT_DIR+fixture_name
        with open(loc+'_out.json', 'w') as f:
            f.write(event.as_json()
                    .replace('{"','{\n"')
                    .replace(', "',',\n"')
                    )
        with open(loc+'.json', 'w') as f:
            f.write(get_fixture(fixture_name)
                    .replace('{"','{\n"')
                    .replace(', "',',\n"')
                    )
    else:
        pass

### Shared entity resources ###
## build a test learning context
def build_student_554433():
    return caliper.entities.Person(
        entity_id = 'https://some-university.edu/user/554433',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        membership = [
            build_AmRev101_membership(),
            build_AmRev101_section_membership(),
            build_AmRev101_group_membership()
            ]
        )

def build_AmRev101_course():
    return caliper.entities.CourseOffering(
        entity_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101',
        academicSession = 'Fall-2015',
        courseNumber = 'POL101',
        name = 'Political Science 101: The American Revolution',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_AmRev101_course_section():
    return caliper.entities.CourseSection(
        entity_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101/section/001',
        academicSession = 'Fall-2015',
        courseNumber = 'POL101',
        membership = [ build_AmRev101_section_membership() ],
        name = 'American Revolution 101',
        subOrganizationOf = build_AmRev101_course(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_AmRev101_group_001():
    return caliper.entities.Group(
        entity_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101/section/001/group/001',
        name = 'Discussion Group 001',
        membership = [build_AmRev101_group_membership()],
        subOrganizationOf = build_AmRev101_course_section(),
        dateCreated = _CREATETIME
        )

def build_AmRev101_membership():
    return caliper.entities.Membership(
        entity_id = 'https://some-university.edu/membership/001',
        member_id = 'https://some-university.edu/user/554433',
        organization_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101',
        roles = [caliper.entities.Role.Roles['LEARNER']],
        status = caliper.entities.Status.Statuses['ACTIVE'],
        dateCreated = _CREATETIME
        )

def build_AmRev101_section_membership():
    return caliper.entities.Membership(
        entity_id = 'https://some-university.edu/membership/002',
        member_id = 'https://some-university.edu/user/554433',
        organization_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101/section/001',
        roles = [caliper.entities.Role.Roles['LEARNER']],
        status = caliper.entities.Status.Statuses['ACTIVE'],
        dateCreated = _CREATETIME
        )

def build_AmRev101_group_membership():
    return caliper.entities.Membership(
        entity_id = 'https://some-university.edu/membership/003',
        member_id = 'https://some-university.edu/user/554433',
        organization_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101/section/001/group/001',
        roles = [caliper.entities.Role.Roles['LEARNER']],
        status = caliper.entities.Status.Statuses['ACTIVE'],
        dateCreated = _CREATETIME
        )

def build_assessment_tool_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = caliper.entities.SoftwareApplication(
            entity_id = 'https://com.sat/super-assessment-tool',
            name = 'Super Assessment Tool',
            dateCreated = _CREATETIME
            ),
        group = build_AmRev101_group_001()
        )

def build_media_app():
    return caliper.entities.SoftwareApplication(
        entity_id = 'https://com.sat/super-media-tool',
        name = 'Super Media Tool',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_video_media_tool_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = build_media_app(),
        group = build_AmRev101_group_001()
        )

def build_readium_app():
    return caliper.entities.SoftwareApplication(
        entity_id = 'https://github.com/readium/readium-js-viewer',
        name = 'Readium',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_readium_app_learning_context():
    app = build_readium_app()
    return caliper.entities.LearningContext(
        agent = app,
        edApp = app,
        group = build_AmRev101_group_001()
        )

def build_readium_student_learning_context():
    return caliper.entities.LearningContext(
        agent = build_student_554433(),
        edApp = build_readium_app(),
        group = build_AmRev101_group_001()
        )

## build a test EPUB volume
def build_epub_vol43():
    return caliper.entities.EpubVolume(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)',
        name = 'The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERED
        )

def build_epub_subchap431():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)',
        name = 'Key Figures: George Washington',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERED
        )

def build_epub_subchap432():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/2)',
        name = 'Key Figures: Lord North',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERED
        )

def build_epub_subchap433():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/3)',
        name = 'Key Figures: John Adams',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERED
        )

def build_epub_subchap434():
    return caliper.entities.EpubSubChapter(
        entity_id = 'https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/4)',
        name = 'The Stamp Act Crisis',
        isPartOf = build_epub_vol43(),
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERED
        )


## build a course landing page
def build_AmRev101_landing_page():
    return caliper.entities.WebPage(
        entity_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101/index.html',
        name = 'American Revolution 101 Landing Page',
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERNUM
        )


### Annotation Profile ###
## build test annotations
def build_bookmark_annotation(annotated = None):
    return caliper.entities.BookmarkAnnotation(
        entity_id = 'https://someEduApp.edu/bookmarks/00001',
        bookmarkNotes = 'The Intolerable Acts (1774)--bad idea Lord North',
        annotated = annotated,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_highlight_annotation(annotated = None):
    selection = caliper.entities.TextPositionSelector(start='455', end='489')
    return caliper.entities.HighlightAnnotation(
        entity_id = 'https://someEduApp.edu/highlights/12345',
        selection = selection,
        selectionText = 'Life, Liberty and the pursuit of Happiness',
        annotated = annotated,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

def build_shared_annotation(annotated = None):
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
        annotated = annotated,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        )

def build_tag_annotation(annotated = None):
    return caliper.entities.TagAnnotation(
        entity_id = 'https://someEduApp.edu/tags/7654',
        tags = ['to-read', '1765', 'shared-with-project-team'],
        annotated = annotated,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME
        )

## build general annotation event
def build_annotation_event(learning_context = None,
                           event_object = None,
                           index = None,
                           annotation = None,
                           action = None):
    return caliper.events.AnnotationEvent(
        edApp = learning_context.edApp,
        group = learning_context.group,
        actor = learning_context.agent,
        action = action,
        event_object = caliper.entities.Frame(
            entity_id = event_object.id,
            name = event_object.name,
            isPartOf = event_object.isPartOf,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            version = event_object.version,
            index = index
            ),
        generated = annotation,
        startedAtTime = _STARTTIME
        )

### Assignable Profile ###
## build assignable event
def build_assessment_assignable_event(learning_context = None,
                                      assessment = None,
                                      action = None):
    return caliper.events.AssignableEvent(
        edApp = learning_context.edApp,
        group = learning_context.group,
        actor = learning_context.agent,
        action = action,
        event_object = assessment,
        generated = caliper.entities.Attempt(
            entity_id = '{0}/{1}'.format(assessment.id, 'attempt1'),
            assignable = assessment,
            actor = learning_context.agent,
            count = 1,
            dateCreated = _CREATETIME,
            startedAtTime = _STARTTIME),
        startedAtTime = _STARTTIME
        )

### Assessment Profile and Outcome Profile ###
## build a test assessment
def build_assessment_items(assessment = None):
    return [caliper.entities.AssessmentItem(
               entity_id = '{0}/item{1}'.format(assessment.id,particle),
               name = 'Assessment Item {1}'.format(assessment.name,particle),
               isPartOf = assessment,
               version = _VERNUM,
               maxAttempts = 2,
               maxSubmits = 2,
               maxScore = 1)
            for particle in ['1','2','3']
        ]

def build_assessment():
    asmnt = caliper.entities.Assessment(
        entity_id = 'https://some-university.edu/politicalScience/2015/american-revolution-101/assessment1',
        name = 'American Revolution - Key Figures Assessment',
        datePublished = _PUBTIME,
        dateToActivate = _ACTTIME,
        dateToShow = _SHOWTIME,
        dateToStartOn = _STARTONTIME,
        dateToSubmit = _SUBMITTIME,
        maxAttempts = 2,
        maxSubmits = 2,
        maxScore = 3, # WARN original value is 5.0d, says Java impl
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERNUM )
    asmnt.assessmentItems = build_assessment_items(assessment=asmnt)
    return asmnt
    

## build a test assessment attempt
def build_assessment_attempt(learning_context=None,
                             assessment=None):
    return caliper.entities.Attempt(
        entity_id = '{0}/{1}'.format(assessment.id,'attempt1'),
        assignable = assessment,
        actor = learning_context.agent,
        count = 1,
        dateCreated = _CREATETIME,
        startedAtTime = _STARTTIME
        )

## build a test assessment item attempt
def build_assessment_item_attempt(learning_context=None,
                                  assessment=None):
    return caliper.entities.Attempt(
        entity_id = '{0}/{1}'.format(assessment.id,'item1/attempt1'),
        assignable = assessment,
        actor = learning_context.agent,
        count = 1,
        dateCreated = _CREATETIME,
        startedAtTime = _STARTTIME
        )

## build a test assessment item response
def build_assessment_item_response(assessment=None,
                                   attempt=None,
                                   values=None):
    return caliper.entities.FillinBlankResponse(
        entity_id = '{0}/{1}'.format(assessment.id,'item1/response1'),
        assignable = attempt.assignable,
        actor = attempt.actor,
        attempt = attempt,
        dateCreated = _CREATETIME,
        startedAtTime = _STARTTIME,
        values = values
        )

## build a test assessment result
def build_assessment_result(learning_context=None,
                            attempt=None):
    return caliper.entities.Result(
        entity_id = '{0}/{1}'.format(attempt.id, 'result'),
        actor = learning_context.agent,
        assignable = attempt.assignable,
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
        group = learning_context.group,
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
        group = learning_context.group,
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
        group = learning_context.group,
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
        group = learning_context.group,
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
        duration = _MEDIA_DURTIME,
        dateCreated = _CREATETIME,
        dateModified = _MODTIME,
        version = _VERNUM
        )

def build_video_media_location():
    return caliper.entities.MediaLocation(
        entity_id = build_video_with_learning_objective().id,
        currentTime = _MEDIA_CURTIME,
        dateCreated = _CREATETIME,
        version = _VERNUM
        )

## Navigation event
def build_epub_navigation_event(learning_context = None,
                                event_object = None,
                                from_resource = None,
                                target = None,
                                action = None):
    return caliper.events.NavigationEvent(
        edApp = learning_context.edApp,
        group = learning_context.group,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = event_object,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            version = _VERED,
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
        group = learning_context.group,
        actor = learning_context.agent,
        action = action,
        event_object = event_object,
        target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = event_object,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            version = _VERED,
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
    the_duration = None
    if target and (isinstance(target, caliper.entities.Session)):
        the_target = target
        the_target.endedAtTime = the_endtime = _ENDTIME
        the_target.duration = the_duration = _DURATION
    else:
        the_target = caliper.entities.Frame(
            entity_id = target.id,
            name = target.name,
            isPartOf = target.isPartOf,
            dateCreated = _CREATETIME,
            dateModified = _MODTIME,
            version = _VERED,
            index = 1)
    return caliper.events.SessionEvent(
        edApp = learning_context.edApp,
        group = learning_context.group,
        actor = actor,
        action = action,
        event_object = event_object,
        generated = session,
        target = the_target,
        startedAtTime = _STARTTIME,
        endedAtTime = the_endtime,
        duration = the_duration
        )
