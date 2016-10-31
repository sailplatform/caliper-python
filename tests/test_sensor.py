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
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from future.utils import with_metaclass
from builtins import *

import sys, os
import unittest

from tests.context import caliper, util


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.learning_context = util.build_readium_app_learning_context(
            actor=self.student)
        self.epub_volume = util.build_epub_vol43()
        self.epub_subchapter = util.build_epub_subchap431()
        self.referrer = util.build_AmRev101_landing_page()
        self.iterations = 4

    def testEventPayloadSingle(self):
        sensor = util.build_default_sensor()
        fixture = 'caliperEnvelopeEventSingle'
        event = util.build_epub_navigation_event(
            learning_context=self.learning_context,
            actor=self.student,
            event_object=self.epub_volume,
            federated_session=util.build_federated_session(actor=self.student),
            action=caliper.constants.BASE_PROFILE_ACTIONS['NAVIGATED_TO'],
            referrer=self.referrer,
            target=self.epub_subchapter)
        envelope = util.get_caliper_envelope(sensor, [event])
        util.put_fixture(fixture, envelope)
        self.assertEqual(envelope.as_json(), util.get_local_fixture(fixture))
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True),
            util.get_common_fixture(fixture))

    def testEventPayloadBatch(self):
        sensor = util.build_default_sensor()
        fixture = 'caliperEnvelopeEventBatch'
        batch = [
            util.build_epub_navigation_event(
                learning_context=self.learning_context,
                actor=self.student,
                event_object=self.epub_volume,
                federated_session=util.build_federated_session(
                    actor=self.student),
                action=caliper.constants.BASE_PROFILE_ACTIONS['NAVIGATED_TO'],
                referrer=self.referrer,
                target=self.epub_subchapter) for x in range(self.iterations)
        ]
        envelope = util.get_caliper_envelope(sensor, batch)
        util.put_fixture(fixture, envelope)
        self.assertEqual(envelope.as_json(), util.get_local_fixture(fixture))
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True),
            util.get_common_fixture(fixture))

    def testEventPayloadSingleCoerced(self):
        sensor = util.build_default_sensor()
        fixture = 'caliperEnvelopeEventViewViewedCoerced'
        ret = sensor.describe(
            [self.student, self.epub_volume, self.epub_subchapter])
        event = util.build_epub_view_event(
            learning_context=self.learning_context,
            actor=self.student,
            event_object=self.epub_volume,
            target=self.epub_subchapter,
            action=caliper.constants.READING_PROFILE_ACTIONS['VIEWED'])
        envelope = util.get_caliper_envelope(sensor, [event])
        util.put_fixture(fixture,
                         envelope,
                         thin_props=True,
                         thin_context=True,
                         described_entities=ret['default'])
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True,
                             described_entities=ret['default']),
            util.get_local_fixture(fixture))
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True,
                             described_entities=ret['default']),
            util.get_common_fixture(fixture))

    def testEventPayloadMinimal(self):
        sensor = util.build_default_sensor()
        fixture = 'caliperEnvelopeEventViewViewedMinimal'
        event = util.build_epub_view_event(
            learning_context=self.learning_context,
            actor=self.student,
            event_object=self.epub_volume,
            target=self.epub_subchapter,
            action=caliper.constants.READING_PROFILE_ACTIONS['VIEWED'])
        envelope = util.get_caliper_envelope(sensor,
                                             [event.as_minimal_event()])
        util.put_fixture(fixture, envelope)
        self.assertEqual(envelope.as_json(), util.get_local_fixture(fixture))
        self.assertEqual(envelope.as_json(), util.get_common_fixture(fixture))

    def testEvent(self):
        sensor = util.build_default_sensor()
        for i in range(self.iterations):
            event = util.build_epub_navigation_event(
                learning_context=self.learning_context,
                actor=self.student,
                event_object=self.epub_volume,
                federated_session=util.build_federated_session(
                    actor=self.student),
                action=caliper.constants.BASE_PROFILE_ACTIONS['NAVIGATED_TO'],
                referrer=self.referrer,
                target=self.epub_subchapter)
            sensor.send(event)
        for stats in sensor.statistics:
            counted = stats.measures.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEventBatch(self):
        sensor = util.build_default_sensor()
        batch = [
            util.build_epub_navigation_event(
                learning_context=self.learning_context,
                actor=self.student,
                event_object=self.epub_volume,
                federated_session=util.build_federated_session(
                    actor=self.student),
                action=caliper.constants.BASE_PROFILE_ACTIONS['NAVIGATED_TO'],
                referrer=self.referrer,
                target=self.epub_subchapter) for x in range(self.iterations)
        ]
        sensor.send(batch)
        for stats in sensor.statistics:
            counted = stats.measures.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.student = util.build_student_554433()
        self.epub_volume = util.build_epub_vol43()
        self.epub_subchapter = util.build_epub_subchap431()
        self.iterations = 4

    def testEntityPayloadSingle(self):
        sensor = util.build_default_sensor()
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_caliper_envelope(sensor, [self.student])
        util.put_fixture(fixture, envelope)
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True),
            util.get_local_fixture(fixture))
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True),
            util.get_common_fixture(fixture))

    def testEntityPayloadBatch(self):
        sensor = util.build_default_sensor()
        fixture = 'caliperEnvelopeEntityBatch'
        envelope = util.get_caliper_envelope(
            sensor, [self.student, self.epub_volume, self.epub_subchapter])
        util.put_fixture(fixture, envelope)
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True),
            util.get_local_fixture(fixture))
        self.assertEqual(
            envelope.as_json(thin_props=True,
                             thin_context=True),
            util.get_common_fixture(fixture))

    def testEntity(self):
        sensor = util.build_default_sensor()
        for i in range(self.iterations):
            entity = self.student
            sensor.describe(entity)
        for stats in sensor.statistics:
            counted = stats.describes.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEntityBatch(self):
        sensor = util.build_default_sensor()
        entities = [self.student, self.epub_volume, self.epub_subchapter]
        sensor.describe(entities)
        for stats in sensor.statistics:
            counted = stats.describes.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, len(entities))
            self.assertEqual(succeeded, len(entities))
            self.assertEqual(failed, 0)


if __name__ == '__main__':
    unittest.main()
