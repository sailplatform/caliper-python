# -*- coding: utf-8 -*-
# Caliper-python testing package (testing sensor cases)
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


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.sensor = util.build_default_sensor()
        self.student = util.build_student_554433()
        self.learning_context = util.build_readium_app_learning_context(actor=self.student)
        self.epub = util.build_epub_vol43()
        self.from_resource = util.build_AmRev101_landing_page()
        self.target = util.build_epub_subchap431()
        self.iterations = 4

    def testPayload(self):
        fixture = 'eventStorePayload'
        event = util.build_epub_navigation_event(
                learning_context = self.learning_context,
                actor = self.student,
                event_object = self.epub,
                federated_session = util.build_federated_session(actor=self.student),
                action = caliper.profiles.CaliperProfile.Actions['NAVIGATED_TO'],
                from_resource = self.from_resource,
                target = self.target
            )
        envelope = util.get_caliper_envelope(self.sensor, [event])
        util.put_fixture(fixture, envelope)
        self.assertEqual(envelope.as_json(),
                         util.get_fixture(fixture))
        

    def testEvent(self):
        for i in range(self.iterations):
            event = util.build_epub_navigation_event(
                learning_context = self.learning_context,
                actor = self.student,
                event_object = self.epub,
                action = caliper.profiles.CaliperProfile.Actions['NAVIGATED_TO'],
                from_resource = self.from_resource,
                target = self.target
            )
            self.sensor.send(event)
        for stats in self.sensor.statistics:
            counted = stats.measures.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted,self.iterations)
            self.assertEqual(succeeded,self.iterations)
            self.assertEqual(failed,0)

    def testEventBatch(self):
        batch = [
            util.build_epub_navigation_event(
                learning_context = self.learning_context,
                actor = self.student,
                event_object = self.epub,
                action = caliper.profiles.CaliperProfile.Actions['NAVIGATED_TO'],
                from_resource = self.from_resource,
                target = self.target
                )
            for x in range(self.iterations)]
        self.sensor.send_batch(batch)
        for stats in self.sensor.statistics:
            counted = stats.measures.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted,self.iterations)
            self.assertEqual(succeeded,self.iterations)
            self.assertEqual(failed,0)

if __name__ == '__main__':
    unittest.main()
