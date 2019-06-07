# -*- coding: utf-8 -*-
# Caliper-python testing package (utility functions for testing)
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
import responses
import sys

from .context import caliper, TESTDIR
from caliper import CALIPER_VERSION
import caliper.condensor as condensor

###
# NOTE: FIXTURE_DIR assumes that the caliper fixtures repo contents are hosted
# in the tests module's directory in a 'fixtures_common' subdirectory so
# that the tests can find all the json fixture files in that sub-directory
###
_FIXTURE_PREFIX = os.path.join('caliper-spec', 'fixtures')
_BROKEN_FIXTURE_SUFFIX = 'commonErrorFixtures'
_FIXTURE_BASE_DIR = os.path.join(TESTDIR, _FIXTURE_PREFIX)
_FIXTURE_COMMON_DIR = os.path.join(_FIXTURE_BASE_DIR, CALIPER_VERSION)
_BROKEN_FIXTURE_DIR = os.path.join(_FIXTURE_COMMON_DIR, _BROKEN_FIXTURE_SUFFIX)
_SENSOR_ID = 'https://example.edu/sensors/1'
_TEST_ENDPOINT = 'https://example.edu/caliper/endpoint'


def _get_options(debug=False):
    return caliper.base.HttpOptions(host=_TEST_ENDPOINT,
                                    optimize_serialization=True,
                                    api_key='6xp7jKrOSOWOgy3acxHFWA',
                                    auth_scheme='Bearer',
                                    debug=debug)


def get_testing_options():
    return _get_options()


def get_debug_options():
    return _get_options(debug=True)


def build_default_sensor():
    return caliper.build_sensor_from_config(config_options=get_testing_options(),
                                            sensor_id=_SENSOR_ID)


def build_debug_sensor():
    return caliper.build_sensor_from_config(config_options=get_debug_options(),
                                            sensor_id=_SENSOR_ID + '/debug')


def build_simple_sensor():
    return caliper.build_simple_sensor(config_options=get_testing_options(), sensor_id=_SENSOR_ID)

# TestError caliper serializable to make error handling more uniform to ease testing
class TestError(caliper.base.CaliperSerializable):
    def __init__(self, error=None, fixture=None, **kwargs):
        caliper.base.CaliperSerializable.__init__(self)
        self._update_props('error', str(error))
        self._update_props('fixture', fixture)

    @property
    def error(self):
        return self._get_prop('error')

    @property
    def fixture(self):
        return self._get_prop('fixture')


# basic condensor functions to condense and extract json starting from fixtures
def _shape_fixture(s):
    return s.replace('{"', '{\n"').replace(', "', ',\n"')


def get_fixture(name, broken=False):
    if not broken:
        _path = _FIXTURE_COMMON_DIR
    else:
        _path = _BROKEN_FIXTURE_DIR
    loc = os.path.join(_path, '{}.{}'.format(name, 'json'))
    try:
        with open(loc, 'r') as f:
            return json.dumps(json.load(f), sort_keys=True)
    except Exception as e:
        return json.dumps(TestError(e, name).as_dict(), sort_keys=True)

def get_fixtures_of_type(name, broken=False):
    if not broken:
        _path = _FIXTURE_COMMON_DIR
    else:
        _path = _BROKEN_FIXTURE_DIR
    return [
        os.path.splitext(file)[0] for file in os.listdir(_path)
        if file.startswith('caliper{}'.format(name.title()))
    ]


def _rebuild_caliper_serializable(d, thin_props, thin_context, described_objects):
    try:
        r = condensor.from_json_dict(d, strict=True)
        return r.as_json(thin_props=thin_props,
                         thin_context=thin_context,
                         described_objects=described_objects)
    except Exception as e:
        return TestError(e, d).as_json()


def rebuild_event(fixture,
                  broken=False,
                  thin_props=True,
                  thin_context=True,
                  described_objects=None):
    f_dict = json.loads(get_fixture(fixture, broken))
    return _rebuild_caliper_serializable(f_dict, thin_props, thin_context, described_objects)


def rebuild_entity(fixture,
                   broken=False,
                   thin_props=True,
                   thin_context=True,
                   described_objects=None):
    f_dict = json.loads(get_fixture(fixture, broken))
    return _rebuild_caliper_serializable(f_dict, thin_props, thin_context, described_objects)


def rebuild_envelope(fixture,
                     broken=False,
                     thin_props=True,
                     thin_context=True,
                     described_objects=None):
    env_dict = json.loads(get_fixture(fixture, broken))
    try:
        payload = condensor.from_json_list(env_dict.get('data'), strict=True)
        return caliper.request.Envelope(data=payload,
                                        send_time=env_dict.get('sendTime'),
                                        sensor_id=env_dict.get('sensor')).as_json(
                                            thin_props=thin_props,
                                            thin_context=thin_context,
                                            described_objects=None)
    except Exception as e:
        return TestError(e, env_dict)


# build an envelope from a sensor and the contents of a fixture
def get_envelope(sensor, fixture):
    env_dict = json.loads(get_fixture(fixture))
    try:
        payload = condensor.from_json_list(env_dict.get('data'), strict=True)
        return caliper.request.Envelope(data=payload,
                                        send_time=env_dict.get('sendTime'),
                                        sensor_id=sensor.id)
    except Exception as e:
        return TestError(e, env_dict)


# rebuild an endpoint config from a json dict
def rebuild_endpoint_config(cfg_dict):
    try:
        cfg = caliper.request.EndpointConfig(**cfg_dict)
        cfg.ensure_compatibility()
        return cfg
    except Exception as e:
        return TestError(e, cfg_dict)

# sensor send functions for mocking out endopint

def _send(fn, sensor, data):
    with responses.RequestsMock() as resps:
        resps.add(responses.POST, _TEST_ENDPOINT, status=201)
        ids = fn(data)
    return ids, sensor.statistics

def sensor_config(sensor, data):
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, _TEST_ENDPOINT, status=200, json=data)
        cfg = sensor.get_config()
    return cfg

def sensor_describe(sensor, data):
    return _send(sensor.describe, sensor, data)

def sensor_send(sensor, data):
    return _send(sensor.send, sensor, data)
