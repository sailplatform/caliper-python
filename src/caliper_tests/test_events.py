# -*- coding: utf-8 -*-
# Caliper-python testing package (testing events cases)
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
from caliper_tests import fixtures, util

import unittest

class AnnotationProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_readium_learning_context()

    def testBookmarkAnnotationEvent(self):
        target = util.build_epub_subchap432()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_bookmark_annotation(target=target),
            index = 2,
            target = target,
            action = caliper.profiles.AnnotationProfile.Actions['BOOKMARKED']
            )

        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture_str(fixtures.BOOKMARK_ANNOTATION_EVENT))

    def testHighlightAnnotationEvent(self):
        target = util.build_epub_subchap431()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_highlight_annotation(target=target),
            target = target,
            index = 1,
            action = caliper.profiles.AnnotationProfile.Actions['HIGHLIGHTED']
            )
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture_str(fixtures.HIGHLIGHT_ANNOTATION_EVENT))

    def testSharedAnnotationEvent(self):
        target = util.build_epub_subchap433()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_shared_annotation(target=target),
            target = target,
            index = 3,
            action = caliper.profiles.AnnotationProfile.Actions['SHARED']
            )
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture_str(fixtures.SHARED_ANNOTATION_EVENT))

    def testTagAnnotationEvent(self):
        target = util.build_epub_subchap434()
        annotation_event = util.build_annotation_event(
            learning_context = self.learning_context,
            annotation = util.build_tag_annotation(target=target),
            target = target,
            index = 4,
            action = caliper.profiles.AnnotationProfile.Actions['TAGGED']
            )
        self.assertEqual(annotation_event.as_json(),
                         util.get_fixture_str(fixtures.TAG_ANNOTATION_EVENT))
        

class AssessmentProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()
        self.assessment_item = self.assessment.assessmentItems[0]
        self.attempt = util.build_assessment_attempt(learning_context=self.learning_context,
                                                     assessment=self.assessment)
        
    def testAssessmentEvent(self):
        assessment_event = util.build_assessment_event(
            learning_context = self.learning_context,
            assessment = self.assessment,
            attempt = self.attempt,
            action = caliper.profiles.AssessmentProfile.Actions['STARTED']
            )

        self.assertEqual(assessment_event.as_json(),
                         util.get_fixture_str(fixtures.ASSESSMENT_EVENT))

    def testAssessmentItemEvent(self):
        assessment_item_event = util.build_assessment_item_event(
            learning_context = self.learning_context,
            assessment_item = self.assessment_item,
            action = caliper.profiles.AssessmentItemProfile.Actions['STARTED']
            )

        self.assertEqual(assessment_item_event.as_json(),
                         util.get_fixture_str(fixtures.ASSESSMENT_ITEM_EVENT))


class AssignableProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()

    def testAssignableEvent(self):
        assignable_event = util.build_assessment_assignable_event(
            learning_context = self.learning_context,
            assessment = self.assessment,
            action = caliper.profiles.AssignableProfile.Actions['ACTIVATED']
            )

        self.assertEqual(assignable_event.as_json(),
                         util.get_fixture_str(fixtures.ASSIGNABLE_EVENT))

class MediaProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_video_media_tool_learning_context()
        self.video = util.build_video_with_learning_objective()
        self.location = util.build_video_media_location()

    def testVideoMediaEvent(self):
        video_media_event = util.build_video_media_event(
            learning_context = self.learning_context,
            event_object = self.video,
            location = self.location,
            action = caliper.profiles.MediaProfile.Actions['PAUSED']
            )

        self.assertEqual(video_media_event.as_json(),
                         util.get_fixture_str(fixtures.MEDIA_EVENT))

class OutcomeProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_assessment_tool_learning_context()
        self.assessment = util.build_assessment()
        self.attempt = util.build_assessment_attempt(learning_context=self.learning_context,
                                                     assessment=self.assessment)
        self.result = util.build_assessment_result(attempt=self.attempt)

    def testAssessmentOutcomeEvent(self):
        assessment_outcome_event = util.build_assessment_outcome_event(
            learning_context = self.learning_context,
            attempt = self.attempt,
            result = self.result,
            action = caliper.profiles.OutcomeProfile.Actions['GRADED']
            )

        self.assertEqual(assessment_outcome_event.as_json(),
                         util.get_fixture_str(fixtures.ASSESSMENT_OUTCOME_EVENT))
        
        
class ReadingProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.build_readium_learning_context()
        self.epub = util.build_epub_vol43()
        self.target = util.build_epub_subchap431()

    def testViewedEvent(self):
        viewed_event = util.build_epub_view_event(
            learning_context = self.learning_context,
            event_object = self.epub,
            action = caliper.profiles.ReadingProfile.Actions['VIEWED'],
            target = self.target
            )

        self.assertEqual(viewed_event.as_json(),
                         util.get_fixture_str(fixtures.VIEW_EVENT))

                
if __name__ == '__main__':
    unittest.main()

