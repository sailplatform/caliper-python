[![Master Build Status](https://img.shields.io/travis/IMSGlobal/caliper-python.svg?label=master)](https://travis-ci.org/IMSGlobal/caliper-python)
[![Develop Build Status](https://img.shields.io/travis/IMSGlobal/caliper-python/develop.svg?label=develop)](https://travis-ci.org/IMSGlobal/caliper-python/develop)


# IMS Global Learning Consortium, Inc.

The Caliper Analytics® Specification provides a structured approach to describing, collecting and
exchanging learning activity data at scale. Caliper also defines an application programming
interface (the Sensor API™) for marshalling and transmitting event data from instrumented
applications to target endpoints for storage, analysis and use.

caliper-python is a reference implementation of the Sensor API™ written in Python.


## Dependencies

To effectively use this `imsglobal_caliper` bundle, you will need to have Python, pip, and
setuptools installed. This package also depends on several third-party packages:

* aniso8601 -- (3-clause BSD licensed)

* future -- (MIT licensed)

* requests -- (Apache 2 licensed)

* rfc3986 -- (Apache 2 licensed)

To work with the `imsglobal_caliper` bundle (maintain, use, run tests) you'll need to have these
third-party packages in your local Python environment.



### Which platform

We developed `imsglobal_caliper` primarily using the Python 3.6+ platform; however, we've taken
steps to make it portably usbale with Python 2.7 as well (using the `future` package). Changes to
the code base should ensure the tests run clean under Python 3.6 *and* 2.7.


## Build and install

We built `imsglobal_caliper` to be packagable for loading from PyPi, or direct from a source
bundle, with `pip`.

If it's on PyPi, you can simply install it into your site-packages with:

``` shell
pip install imsglobal_caliper
```


### Building and installing from a source bundle

If you want to install it from a source bundle, then use these steps (note that the name of the
repository on GitHub is different to the distribution package name):

#. Clone the [repository from GitHub](https://github.com/IMSGlobal/caliper-python.git>)
   onto your local machine.

#. Use pip to install the package as a writable source bundle; there's no need
   to do a package build step ahead of time:

   ``` shell
   pip install -e caliper-python
   ```


## Changing and testing

All the `imsglobal_caliper` code you would use to build and use a caliper sensor in your
application you can find in the `caliper` main module.

**Branches and tags**. This project organizes around two, long-running branches:

- *master*. Stable, deployable branch that stores the official release history.

- *develop*. Unstable development branch; current work that targets a future release is merged to
  this branch.

Project releases are tagged and versioned using git tags of the form
*MAJOR*.*MINOR*.*PATCH*[-*label*] (for example: `1.1.0`; or, for signalling a pre-release version
with a label extension, `1.2.0-RC01`).

**Making contributions**. We welcome the posting of issues by those who are not members of IMS
Global Learning Consortium (for example, for feature requests, bug reports, questions, and so on)
but we do not accept contributions in the form of pull requests from non-members. See
`CONTRIBUTING.md` for more information.

**Testing**. When you work with the source bundle, we include tests in the `tests` directory. The
tests use the `tox` test runner, so you will need that in your environment. In general, whenever
you might make changes to code in `caliper`, you should run the fixture tests. From the source
repo's top-level directory, use `tox` to run all the tests on Python 2.7, Python 3.7, PyPy, and
PyPy3.

Before you can run the tests, you will also need a copy of the Caliper fixtures (see below).

**Fixtures**. The test suites are principally designed to test against the
canonical common JSON fixtures. To set up your tests, you should clone the
[Caliper common fixtures repository](https://github.com/IMSGlobal/caliper-common-fixtures-public>)
repository into the `tests/fixtures` directory, and pull changes there.

Ideally, if you make changes to `imsglobal_caliper` you should ensure that your changes will test
well against the fixtures from the main common fixtures repository. When IMS makes updates to the
`imsglobal_caliper` repository, it ensures that the updates do test well against the common
fixtures repository.


## Using the package

We made `imsglobal_caliper` with a lean integration layer for your application. To use the package,
your application needs only:

``` python
import caliper
```


Your application will need awareness of these parts of the package:

* The `caliper.HttpOptions` class (for use with simple HTTP transport to a Caliper endpoint).

* The `caliper.Sensor` class and its API.

* The appropriate `caliper.profiles` metric profile enumeration classes that contain the metric
  profile actions you want to support.

* The `Event` and `Entity` subclasses (found in `caliper.events` and `caliper.entities`,
  respectively) that you will need to use for the metric profile actions you want to support.

Here is a  very simple example code scrap  that demonstrates how an application might  send a basic
navigation event to a caliper endpoint::

``` python
import caliper

the_config = caliper.HttpOptions(
    host='http://caliper-endpoint.your-school.edu/events/',
    auth_scheme='Bearer',
    api_key='your-caliper-API-key' )

# Here you build your sensor; it will have one client in its registry,
# with the key 'default'.
the_sensor = caliper.build_sensor_from_config(
    sensor_id = 'http://learning-app.your-school.edu/sensor',
    config_options = the_config )

# Here, you will have caliper entity representations of the various
# learning objects and entities in your wider system, and you provide
# them into the constructor for the event that has just happened.
#
# Note that you don't have to pass an action into the constructor because
# the NavigationEvent only supports one action, part of the
# Caliper base profile: caliper.constants.BASE_PROFILE_ACTIONS['NAVIGATED_TO']
#
the_event = caliper.events.NavigationEvent(
    actor = the_user_currently_acting_as_caliper_Person_entity,
    edApp = your_application_as_caliper_SoftwareApplication_entity,
    group = the_course_offering_in_play_as_caliper_Organization_entity,
    object = the_caliper_DigitalResource_the_actor_is_using,
    referrer = the_caliper_DigitalResource_the_actor_came_from,
    target = the_caliper_DigitalResource_the_actor_is_going_to,
    eventTime = the_time_when_the_actor_did_the_action )

# Once built, you can use your sensor to describe one or more often used
# entities; suppose for example, you'll be sending a number of events
# that all have the same actor

ret = the_sensor.describe(the_event.actor)

# The return structure from the sensor will be a dictionary of lists: each
# item in the dictionary has a key corresponding to a client key,
# so ret['default'] fetches back the list of URIs of all the @ids of
# the fully described Caliper objects you have sent with that describe call.
#
# Now you can use this list with event sendings to send only the identifiers
# of already-described entities, and not their full forms:

the_sensor.send(the_event, described_objects=ret['default'])

# You can also just send the event in its full form, with all fleshed out
# entities:

the_sensor.send(the_event)
```

Your actual use of the caliper code will certainly be more complex than this. For assistance
getting from this very simple example through to more complex and realistic code-use, we encourage
you to look at the unit tests in the package, and the common fixtures they test against.


## Copyright and License

This project is licensed under the terms of the GNU Lesser General Public License (LGPL),
version 3. See the LICENSE file for details. For additional information on licensing options for
IMS members, please see the NOTICE file.

©2019 IMS Global Learning Consortium, Inc. All Rights Reserved.  Trademark Information -
http://www.imsglobal.org/copyright.html
