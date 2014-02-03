#!/usr/bin/env python
# encoding: utf-8

import unittest
import json

from datetime import datetime, timedelta

from random import randint
from time import sleep, time
from decimal import *

import logging
logging.basicConfig()

from dateutil.tz import tzutc

import caliper
import caliper.utils

secret = 'testsecret'


def on_success(data, response):
    print 'Success', response


def on_failure(data, error):
    print 'Failure', error


class CaliperCaliperTests(unittest.TestCase):

    def setUp(self):
        caliper.init(secret, log_level=logging.DEBUG)

        caliper.on_success(on_success)
        caliper.on_failure(on_failure)

    def test_async_basic_describe(self):
        # flush after every message
        caliper.default_client.flush_at = 1
        caliper.default_client.async = True

        last_describes = caliper.stats.describes
        last_successful = caliper.stats.successful
        last_flushes = caliper.stats.flushes

        caliper.describe(entity_type='student', entity_id='student-1234', properties={}, timestamp=None)
        caliper.describe(entity_type='teacher', entity_id='teacher-1234', properties={'foo': 'bar', 'b': 3}, timestamp=None)

        caliper.describe(entity_type='student', entity_id='student-5678', properties={}, timestamp=1383423536478)
        caliper.describe(entity_type='teacher', entity_id='teacher-5678', properties={'foo': 'bar', 'b': 3}, timestamp=1383423536478)

        self.assertEqual(caliper.stats.describes, last_describes + 2)

        # this should flush because we set the flush_at to 1
        self.assertEqual(caliper.stats.flushes, last_flushes + 1)

        # this should do nothing, as the async thread is currently active
        caliper.flush()

        # we should see no more flushes here
        self.assertEqual(caliper.stats.flushes, last_flushes + 1)

        sleep(1)

        self.assertEqual(caliper.stats.successful, last_successful + 2)

    def test_async_basic_measure(self):
        # flush after every message
        caliper.default_client.flush_at = 1
        caliper.default_client.async = True

        last_measures = caliper.stats.measures
        last_successful = caliper.stats.successful
        last_flushes = caliper.stats.flushes

        caliper.measure(action='HILIGHT', learning_context={"courseId": "course-1234"}, activity_context={"activityId": "reading-1234"}, timestamp=None)
        caliper.measure(action='ANNOTATE', learning_context={"courseId": "course-1234"}, activity_context={"activityId": "reading-1234"}, timestamp=None)

        caliper.measure(action='HILIGHT', learning_context={"courseId": "course-1234"}, activity_context={"activityId": "reading-1234"}, timestamp=1383423536478)
        caliper.measure(action='ANNOTATE', learning_context={"courseId": "course-1234"}, activity_context={"activityId": "reading-1234"}, timestamp=1383423536478)

        self.assertEqual(caliper.stats.measures, last_measures + 2)

        # this should flush because we set the flush_at to 1
        self.assertEqual(caliper.stats.flushes, last_flushes + 1)

        # this should do nothing, as the async thread is currently active
        caliper.flush()

        # we should see no more flushes here
        self.assertEqual(caliper.stats.flushes, last_flushes + 1)

        sleep(1)

        self.assertEqual(caliper.stats.successful, last_successful + 2)

if __name__ == '__main__':
    unittest.main()
