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
from future.utils import with_metaclass
from builtins import *

import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import caliper
import caliper.condensor as condensor

# needed to root the fixtures directory
import caliper_tests

###
# NOTE: FIXTURE_DIR assumes that the caliper fixtures repo contents are hosted
# in the tests module's directory in a 'fixtures_common' subdirectory so
# that the tests can find all the json fixture files in that sub-directory
###
_FIXTURE_PREFIX = 'fixtures'
_FIXTURE_BASE_DIR = os.path.join(os.path.dirname(caliper_tests.__file__), _FIXTURE_PREFIX)
_FIXTURE_COMMON_DIR = os.path.join(_FIXTURE_BASE_DIR, 'src', 'test', 'resources', _FIXTURE_PREFIX)

_SENSOR_ID = 'https://example.edu/sensors/1'


def get_testing_options():
    return caliper.base.HttpOptions(
        host='http://httpbin.org/post',
        optimize_serialization=True,
        api_key='6xp7jKrOSOWOgy3acxHFWA',
        auth_scheme='Bearer')


def build_default_sensor():
    return caliper.build_sensor_from_config(
        config_options=get_testing_options(), sensor_id=_SENSOR_ID)


# basic condensor functions to condense and extract json starting from fixtures
def _shape_fixture(s):
    return s.replace('{"', '{\n"').replace(', "', ',\n"')


def get_fixture(name):
    loc = os.path.join(_FIXTURE_COMMON_DIR, '{}.{}'.format(name, 'json'))
    with open(loc, 'r') as f:
        return json.dumps(json.load(f), sort_keys=True)


def get_fixtures_of_type(name):
    return [
        os.path.splitext(file)[0] for file in os.listdir(_FIXTURE_COMMON_DIR)
        if file.startswith('caliper{}'.format(name.title()))
    ]


def _rebuild_caliper_serializable(d, thin_props, thin_context, described_objects):
    return condensor.from_json_dict(d).as_json(
        thin_props=thin_props, thin_context=thin_context, described_objects=described_objects)


def rebuild_event(fixture, thin_props=True, thin_context=True, described_objects=None):
    f_dict = json.loads(get_fixture(fixture))
    return _rebuild_caliper_serializable(f_dict, thin_props, thin_context, described_objects)


def rebuild_entity(fixture, thin_props=True, thin_context=True, described_objects=None):
    f_dict = json.loads(get_fixture(fixture))
    return _rebuild_caliper_serializable(f_dict, thin_props, thin_context, described_objects)


def rebuild_envelope(fixture, thin_props=True, thin_context=True, described_objects=None):
    env_dict = json.loads(get_fixture(fixture))
    payload = condensor.from_json_list(env_dict.get('data'))
    return caliper.request.Envelope(
        data=payload, send_time=env_dict.get('sendTime'),
        sensor_id=env_dict.get('sensor')).as_json(
            thin_props=thin_props, thin_context=thin_context, described_objects=None)


# build an envelope from a sensor and the contents of a fixture
def get_envelope(sensor, fixture):
    env_dict = json.loads(get_fixture(fixture))
    payload = condensor.from_json_list(env_dict.get('data'))
    return caliper.request.Envelope(
        data=payload, send_time=env_dict.get('sendTime'), sensor_id=sensor.id)
