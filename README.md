caliper-php
================

caliper-php is a php client for [Caliper](http://www.imsglobal.org) that provides an implementation of the Caliper Sensor API.

## Documentation

### Pre-requisites for development:  

* Ensure you have python and pip installed.  

### Installing and using the Library:

To build the library, clone the repository from github into your desired application directory

* git clone https://github.com/IMSGlobal/caliper-python.git
* In caliper/options.py - set the URL for the Sensor endpoint
* Then build using - python setup.py build
* To create a binary distribution - python setup.py bdist
* To install - python setup.py install
* To run tests - python test-caliper.py

Now, you're ready to use the Caliper module as follows:

import caliper
import caliper.utils

...

caliper.init("SOME_API_KEY", log_level=logging.DEBUG)


©2013 IMS Global Learning Consortium, Inc.  All Rights Reserved.
For license information contact, info@imsglobal.org
