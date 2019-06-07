# -*- coding: utf-8 -*-
# Caliper-python testing package (testing sensor behaviour)
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
from builtins import *

import json
import os
import sys
import unittest

from .context import caliper
from . import util


class TestCaliperSimpleSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = util.build_simple_sensor()
        self.iterations = 4

    def tearDown(self):
        del (self.sensor)

    # test the simple ability to construct the same envelope as in the fixture
    def testEventPayloadSingle(self):
        fixture = 'caliperEnvelopeEventSingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    def testEventPayloadBatch(self):
        fixture = 'caliperEnvelopeEventBatch'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    def testEntityPayloadSingle(self):
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    def testEntityPayloadSingle(self):
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    # test the ability to fetch the endpoint's config
    def testGetConfig(self):
        fixture = 'caliperEndpointConfigPayload'
        cfg_from_endoint = json.loads(util.sensor_config(self.sensor, util.get_fixture(fixture)))
        endpoint_config_object = util.rebuild_endpoint_config(cfg_from_endoint)
        self.assertEqual(endpoint_config_object.as_json(), util.get_fixture(fixture))

    # test transmission stats for sensor.send()
    def testEventSend(self):
        fixture = 'caliperEventGeneralCreated'
        for i in range(self.iterations):
            _, statistics = util.sensor_send(
                self.sensor,
                caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture))))
        for stats in statistics:
            counted = stats.sent.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEventSendBatch(self):
        fixture = 'caliperEventGeneralCreated'
        batch = [
            caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture)))
            for x in range(self.iterations)
        ]
        _, statistics = util.sensor_send(self.sensor, batch)
        for stats in statistics:
            counted = stats.sent.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    # simple sensor uses only send()
    def testEntityDescribe(self):
        fixture = 'caliperEntityPerson'
        for i in range(self.iterations):
            _, statistics = util.sensor_send(
                self.sensor,
                caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture))))
        for stats in statistics:
            counted = stats.sent.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEntityDescribeBatch(self):
        fixture = 'caliperEntityPerson'
        batch = [
            caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture)))
            for x in range(self.iterations)
        ]
        _, statistics = util.sensor_send(self.sensor, batch)
        for stats in statistics:
            counted = stats.sent.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)


class TestCaliperSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = util.build_default_sensor()
        self.iterations = 4

    def tearDown(self):
        del (self.sensor)

    # test the simple ability to construct the same envelope as in the fixture
    def testEventPayloadSingle(self):
        fixture = 'caliperEnvelopeEventSingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    def testEventPayloadBatch(self):
        fixture = 'caliperEnvelopeEventBatch'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    def testEntityPayloadSingle(self):
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    def testEntityPayloadSingle(self):
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(envelope.as_json(thin_props=True, thin_context=True),
                         util.get_fixture(fixture))

    # test transmission stats for sensor.send()
    def testEventSend(self):
        fixture = 'caliperEventGeneralCreated'
        for i in range(self.iterations):
            _, statistics = util.sensor_send(
                self.sensor,
                caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture))))
        for stats in statistics:
            counted = stats.measures.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEventSendBatch(self):
        fixture = 'caliperEventGeneralCreated'
        batch = [
            caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture)))
            for x in range(self.iterations)
        ]
        _, statistics = util.sensor_send(self.sensor, batch)
        for stats in statistics:
            counted = stats.measures.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEntityDescribe(self):
        fixture = 'caliperEntityPerson'
        for i in range(self.iterations):
            _, statistics = util.sensor_describe(
                self.sensor,
                caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture))))
        for stats in statistics:
            counted = stats.describes.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)

    def testEntityDescribeBatch(self):
        fixture = 'caliperEntityPerson'
        batch = [
            caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture)))
            for x in range(self.iterations)
        ]
        _, statistics = util.sensor_describe(self.sensor, batch)
        for stats in statistics:
            counted = stats.describes.count
            succeeded = stats.successful.count
            failed = stats.failed.count
            stats.clear()
            self.assertEqual(counted, self.iterations)
            self.assertEqual(succeeded, self.iterations)
            self.assertEqual(failed, 0)


class TestDebugSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = util.build_debug_sensor()
        self.iterations = 4

    def testEventSend(self):
        fixture = 'caliperEventGeneralCreated'
        for i in range(self.iterations):
            util.sensor_send(
                self.sensor,
                caliper.condensor.from_json_dict(json.loads(util.get_fixture(fixture))))
        for response in self.sensor.client_registry['default'].debug:
            self.assertEqual(response.status_code, 201)
