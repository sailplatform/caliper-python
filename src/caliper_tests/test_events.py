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

class TestAssessmentProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.buildLearningContext()
        self.assessment = util.buildAssessment()

    def testAssessmentItemEvent(self):
        ap = util.buildAssessmentProfile(
            learning_context = self.learning_context,
            assessment = self.assessment
            )
        ai = util.startAssessmentItem(
            assessment_profile=ap,
            assessment_item=ap.assessment.assessmentItems[0])
        assessment_item_event = util.buildAssessmentItemEvent(
            assessment_profile = ap,
            assessment_item = ai)

        self.assertEqual(assessment_item_event.as_json(),
                         util.getFixtureStr(fixtures.ASSESSMENT_ITEM_EVENT))

    def testAssessmentEvent(self):
        ap = util.buildAssessmentProfile(
            learning_context = self.learning_context,
            assessment = self.assessment
            )
        ap = util.startAssessment(assessment_profile=ap)
        assessment_event = util.buildAssessmentEvent(assessment_profile=ap)

        self.assertEqual(assessment_event.as_json(),
                         util.getFixtureStr(fixtures.ASSESSMENT_EVENT))

class TestOutcomeProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.buildLearningContext()
        self.assessment = util.buildAssessment()

    def testAssessmentOutcomeEvent(self):
        ap = util.buildAssessmentProfile(
            learning_context = self.learning_context,
            assessment = self.assessment
            )
        ap = util.startAssessment(assessment_profile=ap)
        res = util.buildAssessmentResult(assessment_profile=ap)
        op = util.buildAssessmentOutcomeProfile(assessment_profile=ap,
                                                result=res)
        assessment_outcome_event = util.buildAssessmentOutcomeEvent(outcome_profile=op)

        self.assertEqual(assessment_outcome_event.as_json(),
                         util.getFixtureStr(fixtures.ASSESSMENT_OUTCOME_EVENT))

class TestMediaProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.buildLearningContext()
        self.video_media_profile = util.buildMediaProfile(learning_context=self.learning_context)

    def testMediaEvent(self):
        mp = util.pauseVideo(media_profile=self.video_media_profile)
        video_media_event = util.buildMediaEvent(media_profile=mp)

        self.assertEqual(video_media_event.as_json(),
                         util.getFixtureStr(fixtures.MEDIA_EVENT))

class TestReadingProfile(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.buildLearningContext()

    def testViewEvent(self):
        rp = util.buildReadingProfile(learning_context=self.learning_context)
        rp = util.viewReadingTarget(reading_profile=rp)
        view_event = util.buildViewEvent(reading_profile=rp)

        self.assertEqual(view_event.as_json(),
                         util.getFixtureStr(fixtures.VIEW_EVENT))
        
    def testNavigationEvent(self):
        rp = util.buildReadingProfile(learning_context=self.learning_context)
        rp = util.navigateToReadingTarget(reading_profile=rp)
        navigation_event = util.buildNavigationEvent(reading_profile=rp)

        self.assertEqual(navigation_event.as_json(),
                         util.getFixtureStr(fixtures.NAVIGATION_EVENT))


                
if __name__ == '__main__':
    unittest.main()

