# -*- coding: utf-8 -*-
# Caliper-python testing package (testing events cases)
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
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from future.utils import with_metaclass
from builtins import *

import sys, os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import caliper
import caliper_tests.util as util


class AnnotationProfile(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.learning_context = util.build_readium_app_learning_context()

    def testBookmarkAnnotationEvent(self):
        fixture = 'caliperBookmarkAnnotationEvent'
        event_object = util.build_epub_subchap432()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            actor = self.student,
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
            actor = self.student,
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
            actor = self.student,
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
            actor = self.student,
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
        self.student = util.build_student_554433()
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()
        self.assessment_item = util.build_assessment_items(assessment=self.assessment)[0]
        self.attempt = util.build_assessment_attempt(actor = self.student,
                                                     assessment=self.assessment)
        self.item_attempt = util.build_assessment_item_attempt(actor = self.student,
                                                               assessment=self.assessment)
        
    def testAssessmentEvent(self):
        fixture = 'caliperAssessmentEvent'
        assessment_event = util.build_assessment_event(
            learning_context = self.learning_context,
            actor = self.student,
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
            actor = self.student,
            assessment_item = self.assessment_item,
            generated = self.item_attempt,
            action = caliper.profiles.AssessmentItemProfile.Actions['STARTED']
            )
        util.put_fixture(fixture, assessment_item_event)
        self.assertEqual(assessment_item_event.as_json(),
                         util.get_fixture(fixture))


    def testAssessmentItemCompletedEvent(self):
        fixture = 'caliperAssessmentItemCompletedEvent'
        assessment_item_event = util.build_assessment_item_event(
            learning_context = self.learning_context,
            actor = self.student,
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
        self.student = util.build_student_554433()
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()

    def testAssignableEvent(self):
        fixture = 'caliperAssignableEvent'
        assignable_event = util.build_assessment_assignable_event(
            learning_context = self.learning_context,
            actor = self.student,
            assessment = self.assessment,
            action = caliper.profiles.AssignableProfile.Actions['ACTIVATED']
            )
        util.put_fixture(fixture, assignable_event)
        self.assertEqual(assignable_event.as_json(),
                         util.get_fixture(fixture))

class MediaProfile(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.learning_context = util.build_video_media_tool_learning_context()
        self.video = util.build_video_with_learning_objective()
        self.location = util.build_video_media_location()

    def testVideoMediaEvent(self):
        fixture = 'caliperMediaEvent'
        video_media_event = util.build_video_media_event(
            learning_context = self.learning_context,
            actor = self.student,
            event_object = self.video,
            location = self.location,
            action = caliper.profiles.MediaProfile.Actions['PAUSED']
            )
        util.put_fixture(fixture, video_media_event)
        self.assertEqual(video_media_event.as_json(),
                         util.get_fixture(fixture))

class OutcomeProfile(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()
        self.attempt = util.build_assessment_attempt(actor = self.student,
                                                     assessment=self.assessment)
        self.result = util.build_assessment_result(learning_context=self.learning_context,
                                                   actor = self.student,
                                                   attempt=self.attempt)

    def testAssessmentOutcomeEvent(self):
        fixture = 'caliperAssessmentOutcomeEvent'
        assessment_outcome_event = util.build_assessment_outcome_event(
            learning_context = self.learning_context,
            actor = self.student,
            attempt = self.attempt,
            result = self.result,
            action = caliper.profiles.OutcomeProfile.Actions['GRADED']
            )
        util.put_fixture(fixture, assessment_outcome_event)
        self.assertEqual(assessment_outcome_event.as_json(),
                         util.get_fixture(fixture))
        
        
class ReadingProfile(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.learning_context = util.build_readium_app_learning_context()
        self.epub = util.build_epub_vol43()
        self.target = util.build_epub_subchap431()

    def testNavigationEvent(self):
        fixture = 'caliperNavigationEvent'
        navigation_event = util.build_epub_navigation_event(
            learning_context = self.learning_context,
            actor = self.student,
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
            actor = self.student,
            event_object = self.epub,
            target = self.target,
            action = caliper.profiles.CaliperProfile.Actions['VIEWED']
            )
        util.put_fixture(fixture, reading_event)
        self.assertEqual(reading_event.as_json(),
                         util.get_fixture(fixture))


class SessionProfile(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.learning_context = util.build_readium_app_learning_context()
        self.epub = util.build_epub_vol43()
        self.session = util.build_readium_session(actor=self.student)


    def testSessionLoginEvent(self):
        fixture = 'caliperSessionLoginEvent'
        session_event = util.build_session_event(
            learning_context = self.learning_context,
            actor = self.student,
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
            actor = self.student,
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

