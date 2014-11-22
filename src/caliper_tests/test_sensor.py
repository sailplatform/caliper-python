# -*- coding: utf-8 -*-
# Caliper-python testing package (testing sensor cases)
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

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.learning_context = util.buildLearningContext()
        self.reading_profile = util.buildReadingProfile(learning_context=self.learning_context)
        self.sensor = caliper.build_sensor_from_config(config_options=util.getTestingOptions())

    def testEvent(self):
        rp = util.navigateToReadingTarget(reading_profile=self.reading_profile)

        for i in range(4):
            self.sensor.send(util.buildNavigationEvent(rp))

        count = self.sensor.statistics.measures.count
        self.sensor.statistics.clear()
        self.assertEqual(count, 4)

    def testEventBatch(self):
        rp = util.navigateToReadingTarget(reading_profile=self.reading_profile)

        batch = [util.buildNavigationEvent(rp) for x in range(4)]
        self.sensor.send_batch(batch)
        count = self.sensor.statistics.measures.count
        self.sensor.statistics.clear()
        self.assertEqual(count, 4)
