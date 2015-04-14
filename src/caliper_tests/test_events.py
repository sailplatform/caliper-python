# -*- coding: utf-8 -*-
# Caliper-python testing package (testing events cases)
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

import sys, os
sys.path.insert(0, os.path.abspath('..'))
import caliper, caliper_tests
from caliper_tests import util

import unittest

class AnnotationProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_readium_student_learning_context()

    def testBookmarkAnnotationEvent(self):
        fixture = 'caliperBookmarkAnnotationEvent'
        event_object = util.build_epub_subchap432()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_bookmark_annotation(annotated=event_object),
            index = 2,
            event_object = event_object,
            action = caliper.profiles.AnnotationProfile.Actions['BOOKMARKED']
            )
        util.put_fixture(fixture, annotation_event)
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture(fixture))

    def testHighlightAnnotationEvent(self):
        fixture = 'caliperHighlightAnnotationEvent'
        event_object = util.build_epub_subchap431()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_highlight_annotation(annotated=event_object),
            event_object = event_object,
            index = 1,
            action = caliper.profiles.AnnotationProfile.Actions['HIGHLIGHTED']
            )
        util.put_fixture(fixture, annotation_event)
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture(fixture))

    def testSharedAnnotationEvent(self):
        fixture = 'caliperSharedAnnotationEvent'
        event_object = util.build_epub_subchap433()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_shared_annotation(annotated=event_object),
            event_object = event_object,
            index = 3,
            action = caliper.profiles.AnnotationProfile.Actions['SHARED']
            )
        util.put_fixture(fixture, annotation_event)
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture(fixture))

    def testTagAnnotationEvent(self):
        fixture = 'caliperTagAnnotationEvent'
        event_object = util.build_epub_subchap434()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_tag_annotation(annotated=event_object),
            event_object = event_object,
            index = 4,
            action = caliper.profiles.AnnotationProfile.Actions['TAGGED']
            )
        util.put_fixture(fixture, annotation_event)
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture(fixture))
        

class AssessmentProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()
        self.assessment_item = self.assessment.assessmentItems[0]
        self.attempt = util.build_assessment_attempt(learning_context=self.learning_context,
                                                     assessment=self.assessment)
        self.item_attempt = util.build_assessment_item_attempt(learning_context=self.learning_context,
                                                               assessment=self.assessment)
        
    def testAssessmentEvent(self):
        fixture = 'caliperAssessmentEvent'
        assessment_event = util.build_assessment_event(
            learning_context = self.learning_context,
            assessment = self.assessment,
            attempt = self.attempt,
            action = caliper.profiles.AssessmentProfile.Actions['STARTED']
            )
        util.put_fixture(fixture, assessment_event)
        self.assertEqual(assessment_event.as_json(),
                         util.get_fixture(fixture))

    def testAssessmentItemStartedEvent(self):
        fixture = 'caliperAssessmentItemStartedEvent'
        assessment_item_event = util.build_assessment_item_event(
            learning_context = self.learning_context,
            assessment_item = self.assessment_item,
            generated = util.build_assessment_item_attempt(learning_context=self.learning_context,
                                                           assessment=self.assessment),
            action = caliper.profiles.AssessmentItemProfile.Actions['STARTED']
            )
        util.put_fixture(fixture, assessment_item_event)
        self.assertEqual(assessment_item_event.as_json(),
                         util.get_fixture(fixture))


    def testAssessmentItemCompletedEvent(self):
        fixture = 'caliperAssessmentItemCompletedEvent'
        assessment_item_event = util.build_assessment_item_event(
            learning_context = self.learning_context,
            assessment_item = self.assessment_item,
            generated = util.build_assessment_item_response(assessment=self.assessment,
                                                            attempt=self.item_attempt,
                                                            values=['2 July 1776']),
            action = caliper.profiles.AssessmentItemProfile.Actions['COMPLETED']
            )
        util.put_fixture(fixture, assessment_item_event)
        self.assertEqual(assessment_item_event.as_json(),
                         util.get_fixture(fixture))


class AssignableProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()

    def testAssignableEvent(self):
        fixture = 'caliperAssignableEvent'
        assignable_event = util.build_assessment_assignable_event(
            learning_context = self.learning_context,
            assessment = self.assessment,
            action = caliper.profiles.AssignableProfile.Actions['ACTIVATED']
            )
        util.put_fixture(fixture, assignable_event)
        self.assertEqual(assignable_event.as_json(),
                         util.get_fixture(fixture))

class MediaProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_video_media_tool_learning_context()
        self.video = util.build_video_with_learning_objective()
        self.location = util.build_video_media_location()

    def testVideoMediaEvent(self):
        fixture = 'caliperMediaEvent'
        video_media_event = util.build_video_media_event(
            learning_context = self.learning_context,
            event_object = self.video,
            location = self.location,
            action = caliper.profiles.MediaProfile.Actions['PAUSED']
            )
        util.put_fixture(fixture, video_media_event)
        self.assertEqual(video_media_event.as_json(),
                         util.get_fixture(fixture))

class OutcomeProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()
        self.attempt = util.build_assessment_attempt(learning_context=self.learning_context,
                                                     assessment=self.assessment)
        self.result = util.build_assessment_result(learning_context=self.learning_context,
                                                   attempt=self.attempt)

    def testAssessmentOutcomeEvent(self):
        fixture = 'caliperAssessmentOutcomeEvent'
        assessment_outcome_event = util.build_assessment_outcome_event(
            learning_context = self.learning_context,
            attempt = self.attempt,
            result = self.result,
            action = caliper.profiles.OutcomeProfile.Actions['GRADED']
            )
        util.put_fixture(fixture, assessment_outcome_event)
        self.assertEqual(assessment_outcome_event.as_json(),
                         util.get_fixture(fixture))
        
        
class ReadingProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_readium_student_learning_context()
        self.epub = util.build_epub_vol43()
        self.target = util.build_epub_subchap431()

    def testNavigationEvent(self):
        fixture = 'caliperNavigationEvent'
        navigation_event = util.build_epub_navigation_event(
            learning_context = self.learning_context,
            event_object = self.epub,
            from_resource = util.build_AmRev101_landing_page(),
            target = self.target,
            action = caliper.profiles.CaliperProfile.Actions['NAVIGATED_TO']
            )
        util.put_fixture(fixture, navigation_event)
        self.assertEqual(navigation_event.as_json(),
                         util.get_fixture(fixture))
        
    def testViewEvent(self):
        fixture = 'caliperViewEvent'
        reading_event = util.build_epub_view_event(
            learning_context = self.learning_context,
            event_object = self.epub,
            target = self.target,
            action = caliper.profiles.CaliperProfile.Actions['VIEWED']
            )
        util.put_fixture(fixture, reading_event)
        self.assertEqual(reading_event.as_json(),
                         util.get_fixture(fixture))


class SessionProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_readium_student_learning_context()
        self.epub = util.build_epub_vol43()
        self.session = util.build_readium_session(learning_context=self.learning_context)


    def testSessionLoginEvent(self):
        fixture = 'caliperSessionLoginEvent'
        session_event = util.build_session_event(
            learning_context = self.learning_context,
            actor = self.learning_context.agent,
            event_object = self.learning_context.edApp,
            session = self.session,
            target = util.build_epub_subchap431(),
            action = caliper.profiles.SessionProfile.Actions['LOGGED_IN']
            )
        util.put_fixture(fixture, session_event)
        self.assertEqual(session_event.as_json(),
                         util.get_fixture(fixture))

    def testSessionLogoutEvent(self):
        fixture = 'caliperSessionLogoutEvent'
        session_event = util.build_session_event(
            learning_context = self.learning_context,
            actor = self.learning_context.agent,
            event_object = self.learning_context.edApp,
            target = self.session,
            action = caliper.profiles.SessionProfile.Actions['LOGGED_OUT']            
            )
        util.put_fixture(fixture, session_event)
        self.assertEqual(session_event.as_json(),
                         util.get_fixture(fixture))

    def testSessionTimeoutEvent(self):
        fixture = 'caliperSessionTimeoutEvent'
        session_event = util.build_session_event(
            learning_context = self.learning_context,
            actor = self.learning_context.edApp,
            event_object = self.learning_context.edApp,
            target = self.session,
            action = caliper.profiles.SessionProfile.Actions['TIMED_OUT']            
            )
        util.put_fixture(fixture, session_event)
        self.assertEqual(session_event.as_json(),
                         util.get_fixture(fixture))

        
if __name__ == '__main__':
    unittest.main()

