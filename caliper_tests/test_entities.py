# -*- coding: utf-8 -*-
# Caliper-python testing package (testing entities cases)
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

class EntityTests(unittest.TestCase):
    def setUp(self):
        pass

    def testAssessment(self):
        fixture = 'caliperEntityAssessment'
        the_entity = util.build_assessment()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

    def testAssessmentItem(self):
        fixture = 'caliperEntityAssessmentItem'
        the_entity = util.build_assessment_items(assessment = util.build_assessment())[0]
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testAttempt(self):
        fixture = 'caliperEntityAttempt'
        the_entity = util.build_assessment_attempt(
            actor = util.build_student_554433(),
            assessment = util.build_assessment())
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testBookmarkAnnotation(self):
        fixture = 'caliperEntityBookmarkAnnotation'
        the_entity = util.build_bookmark_annotation(annotated = util.build_epub_subchap432())
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testCourseOffering(self):
        fixture = 'caliperEntityCourseOffering'
        the_entity = util.build_AmRev101_course()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testCourseSection(self):
        fixture = 'caliperEntityCourseSection'
        the_entity = util.build_AmRev101_course_section()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testEpubSubChapter(self):
        fixture = 'caliperEntityEpubSubChapter'
        the_entity = util.build_epub_subchap431()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testEpubVolume(self):
        fixture = 'caliperEntityEpubVolume'
        the_entity = util.build_epub_vol43(with_author=True)
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testFillInBlankResponse(self):
        fixture = 'caliperEntityFillInBlankResponse'
        student = util.build_student_554433()
        asmnt = util.build_assessment()
        attempt = util.build_assessment_item_attempt(actor=student,assessment=asmnt)
        the_entity = util.build_assessment_item_response(
            assessment = asmnt,
            attempt = attempt,
            values=['2 July 1776'])
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testFrame(self):
        fixture = 'caliperEntityFrame'
        epsc = util.build_epub_subchap431()
        the_entity = util.build_frame_of_epub(entity_id=epsc.id,
                                              name=epsc.name,
                                              isPartOf=util.build_epub_vol43())
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testGroup(self):
        fixture = 'caliperEntityGroup'
        the_entity = util.build_AmRev101_group_001()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testHighlightAnnotation(self):
        fixture = 'caliperEntityHighlightAnnotation'
        the_entity = util.build_highlight_annotation(annotated = util.build_epub_subchap431())
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testLearningObjective(self):
        fixture = 'caliperEntityLearningObjective'
        the_entity = util.build_video_with_learning_objective().alignedLearningObjective[0]
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testMediaLocation(self):
        fixture = 'caliperEntityMediaLocation'
        the_entity = util.build_video_media_location()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testMembership(self):
        fixture = 'caliperEntityMembership'
        the_entity = util.build_readium_app_learning_context().membership
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testPerson(self):
        fixture = 'caliperEntityPerson'
        the_entity = util.build_student_554433()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testResult(self):
        fixture = 'caliperEntityResult'
        student = util.build_student_554433()
        the_entity = util.build_assessment_result(
            learning_context = util.build_readium_app_learning_context(),
            actor = student,
            attempt = util.build_assessment_attempt(
                actor = student,
                assessment = util.build_assessment()) )
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testSession(self):
        fixture = 'caliperEntitySession'
        the_entity = util.build_readium_app_learning_context().session
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))

    def testLtiSession(self):
        fixture = 'caliperEntityLtiSession'
        the_entity = util.build_lti_tool_provider_learning_context().session
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testSharedAnnotation(self):
        fixture = 'caliperEntitySharedAnnotation'
        the_entity = util.build_shared_annotation(annotated=util.build_epub_subchap433())
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testSoftwareApplication(self):
        fixture = 'caliperEntitySoftwareApplication'
        the_entity = util.build_readium_app_learning_context().edApp
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testTagAnnotation(self):
        fixture = 'caliperEntityTagAnnotation'
        the_entity = util.build_tag_annotation(annotated=util.build_epub_subchap434())
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testVideoObject(self):
        fixture = 'caliperEntityVideoObject'
        the_entity = util.build_video_with_learning_objective()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


    def testWebPage(self):
        fixture = 'caliperEntityWebPage'
        the_entity = util.build_AmRev101_landing_page()
        self.assertEqual(the_entity.as_json(thin_props=True, thin_context=True),
                         util.get_common_fixture(fixture))


if __name__ == '__main__':
    unittest.main()

