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
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from future.utils import with_metaclass
from builtins import *

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import caliper
import tests.util as util


class TestCaliperSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = util.build_default_sensor()

    def tearDown(self):
        del (self.sensor)

    # test the simple ability to construct the same envelope as in the fixture
    def testEventPayloadSingle(self):
        fixture = 'caliperEnvelopeEventSingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(
            envelope.as_json(
                thin_props=True, thin_context=True), util.get_fixture(fixture))

    def testEventPayloadBatch(self):
        fixture = 'caliperEnvelopeEventBatch'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(
            envelope.as_json(
                thin_props=True, thin_context=True), util.get_fixture(fixture))

    def testEntityPayloadSingle(self):
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(
            envelope.as_json(
                thin_props=True, thin_context=True), util.get_fixture(fixture))

    def testEntityPayloadSingle(self):
        fixture = 'caliperEnvelopeEntitySingle'
        envelope = util.get_envelope(self.sensor, fixture)
        self.assertEqual(
            envelope.as_json(
                thin_props=True, thin_context=True), util.get_fixture(fixture))
