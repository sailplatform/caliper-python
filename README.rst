==============
Caliper-python
==============

`Caliper-python` is a Python client for `Caliper <http://imsglobal.org/>`_ that
provides an implementation of the Caliper Sensor API.

**NOTE**: Access to this draft code is reserved for IMS Contributing Members
who are active participants of the IMS Learning Analytics Task
Force. Dissemination of this code to outside participants is strictly
prohibited. By accessing these materials you agree to abide by these
rules. This code is in draft form and will change substantially.
   

Dependencies
============
To effectively use this `Caliper-python` package, you will need to have Python,
pip, and setuptools installed. This package also depends on several third-party
packages:

* requests

* rfc3987

* six

To work with this package (maintain, use, run tests) you'll need to have these
third-party packages in your local Python environment.


Which platform
--------------
We developed `Caliper-python` primarily using the Python 3 platform; however,
we've taken steps to make it portably usbale with Python 2 as well. Changes to
the code base should ensure the tests run clean under Python 3 *and* 2.



Build and install
=================
We built the `Caliper-python` to be packagable for loading from PyPi, or direct
from a source bundle, with `pip`.

If it's on PyPi, you can simply install it into your site-packages with::

  pip install caliper-python

Building and installing from a source bundle
--------------------------------------------
If you want to install it from a source bundle, then use these steps:

#. Clone the `repository from GitHub <https://github.com/IMSGlobal/caliper-python.git>`_
   onto your local machine.

#. Use pip to install the package as a writable source bundle; there's no need
   to do a package build step ahead of time::

     pip install -e caliper-python

Changing and testing
--------------------
All the caliper-python code you would use to build and use a caliper sensor in
your application you can find in the `caliper` main module. The package also
includes a set of test files in a `caliper_tests` main module; we did this not
because we expect you'll use `caliper_tests` in production, but so that the
various tests sub-modules in `caliper_test` can have portable visibility to one
another.

In general, whenever you might make changes to code in `caliper`, you should,
from within `caliper_tests`, run the unit tests::

  python3 test_sensor.py
  python3 test_events.py


**Fixtures**. Your copy of the caliper-python repository (or the package) may
include a set of JSON fixtures in `caliper_tests/fixtures` -- these are
the canonical event serializations used to test the sensor against. The
canonical source for these fixtures you can find in the
`Caliper common fixtures repository <https://github.com/IMSGlobal/caliper-common-fixtures>`_.
If there's a local version of these fixtures that came with your
`caliper-python` package or repository, then it's likely the code has been
built to test aginst these fixtures.

Ideally, if you make changes to `caliper-python` you should ensure that your
changes will test well against the fixtures from the main common fixtures
repository. When IMS makes updates to the `caliper-python` repository, it
ensures that the updates do test well against the common fixtures repository.



Copyright and License
=====================
Copyright © 2015 IMS Global Learning Consortium, Inc. All Rights Reserved.

Trademark Information -- http://www.imsglobal.org/copyright.html

IMS Global Learning Consortium, Inc. Caliper Analytics™ APIs are publicly
licensed as Open Source Software via the GNU Lesser General Public License,
LGPL v3 (https://www.gnu.org/licenses/lgpl.html).

Use of these APIs and/or code libraries does not signify achievement of IMS
conformance certification.  The official list of conformance certifications is
available at http://www.imscert.org.

IMS Global also makes available an Alternative License based on the Apache 2.0
license. Licensees (via the Alternative License) are required to be IMS Global
members. Membership in IMS Global is a commitment by a supplier to the IMS
community for ongoing support for achieving "plug and play" integration. IMS
Global Membership dues pay for ongoing maintenance for the Alternative License
to be applicable to updates to the Caliper Analytics APIs and code libraries.
The rationale for this dual-license approach and membership component is to
help assure a requisite level of ongoing development, project management, and
support for the software.

Licensees of IMS Global Caliper Analytics APIs and code libraries are strongly
encouraged to become active contributors to the Caliper Analytics project and
other projects within IMS Global. Prospective licensees should understand that
their initial base contribution and ongoing membership fees are insufficient to
fully fund the ongoing development and maintenance of Caliper APIs/code
libraries and that voluntary contributions are the primary "fuel" ensuring any
open source project's viability. Contributions can include development, bug
fixing, bug reporting, performance analysis, and other aspects of the overall
development process.

Contributor status at the "Github" level will be individual-based. Contributors
will need to sign an IMS Global Contributor License Agreement (CLA) that grants
IMS Global a license to contributions.  If you are interested in licensing the
IMS Global Caliper Analytics APIs/code libraries please email IMS Global
(mailto:licenses@imsglobal.org).

IMS Caliper is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, version 3 of the License.

IMS Caliper is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License along
with this program. If not, see http://www.gnu.org/licenses/.
