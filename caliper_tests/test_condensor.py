# -*- coding: utf-8 -*-
# Caliper-python testing package (testing condensor cases)
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
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
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
        pass

    def testBookmarkAnnotationEvent(self):
        fixture = 'caliperEventAnnotationBookmarked'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testHighlightAnnotationEvent(self):
        fixture = 'caliperEventAnnotationHighlighted'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testSharedAnnotationEvent(self):
        fixture = 'caliperEventAnnotationShared'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testTagAnnotationEvent(self):
        fixture = 'caliperEventAnnotationTagged'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))


class AssessmentProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testAssessmentEvent(self):
        fixture = 'caliperEventAssessmentStarted'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testAssessmentItemStartedEvent(self):
        fixture = 'caliperEventAssessmentItemStarted'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testAssessmentItemCompletedEvent(self):
        fixture = 'caliperEventAssessmentItemCompleted'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))


class AssignableProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testAssignableEvent(self):
        fixture = 'caliperEventAssignableActivated'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))


class MediaProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testVideoMediaEvent(self):
        fixture = 'caliperEventMediaPausedVideo'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))


class OutcomeProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testAssessmentOutcomeEvent(self):
        fixture = 'caliperEventOutcomeGraded'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))


class ReadingProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testNavigationEvent(self):
        fixture = 'caliperEventNavigationNavigatedTo'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testViewEvent(self):
        fixture = 'caliperEventViewViewed'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testViewEventCoerced(self):
        fixture = 'caliperEventViewViewedCoerced'
        student = util.build_student_554433()
        edApp = util.build_readium_app()
        section = util.build_AmRev101_course_section()
        described = [student.id, edApp.id, section.id]
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_props=True,
                               thin_context=True,
                               described_entities=described),
            util.get_local_fixture(fixture))


class SessionProfile(unittest.TestCase):
    def setUp(self):
        pass

    def testSessionLoginEvent(self):
        fixture = 'caliperEventSessionLoggedIn'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testSessionLogoutEvent(self):
        fixture = 'caliperEventSessionLoggedOut'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))

    def testSessionTimeoutEvent(self):
        fixture = 'caliperEventSessionTimedOut'
        self.assertEqual(
            util.rebuild_event(fixture,
                               thin_context=False,
                               thin_props=False),
            util.get_local_fixture(fixture))
        self.assertEqual(
            util.rebuild_event(fixture, local=False),
            util.get_common_fixture(fixture))


class EntityTests(unittest.TestCase):
    def SetUp(self):
        pass

    def testAssessment(self):
        fixture = 'caliperEntityAssessment'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testAssessmentItem(self):
        fixture = 'caliperEntityAssessmentItem'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testAttempt(self):
        fixture = 'caliperEntityAttempt'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testBookmarkAnnotation(self):
        fixture = 'caliperEntityBookmarkAnnotation'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testCourseOffering(self):
        fixture = 'caliperEntityCourseOffering'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testCourseSection(self):
        fixture = 'caliperEntityCourseSection'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testEpubSubChapter(self):
        fixture = 'caliperEntityEpubSubChapter'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testEpubVolume(self):
        fixture = 'caliperEntityEpubVolume'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testFillInBlankResponse(self):
        fixture = 'caliperEntityFillInBlankResponse'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testFrame(self):
        fixture = 'caliperEntityFrame'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testGroup(self):
        fixture = 'caliperEntityGroup'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testHighlightAnnotation(self):
        fixture = 'caliperEntityHighlightAnnotation'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testLearningObjective(self):
        fixture = 'caliperEntityLearningObjective'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testMediaLocation(self):
        fixture = 'caliperEntityMediaLocation'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testMembership(self):
        fixture = 'caliperEntityMembership'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testPerson(self):
        fixture = 'caliperEntityPerson'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testResult(self):
        fixture = 'caliperEntityResult'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testSession(self):
        fixture = 'caliperEntitySession'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testSharedAnnotation(self):
        fixture = 'caliperEntitySharedAnnotation'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testSoftwareApplication(self):
        fixture = 'caliperEntitySoftwareApplication'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testTagAnnotation(self):
        fixture = 'caliperEntityTagAnnotation'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testVideoObject(self):
        fixture = 'caliperEntityVideoObject'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))

    def testWebPage(self):
        fixture = 'caliperEntityWebPage'
        self.assertEqual(
            util.rebuild_entity(fixture), util.get_common_fixture(fixture))


if __name__ == '__main__':
    unittest.main()
