==============
Caliper-python
==============

`Caliper-python` is a Python client for `Caliper <http://imsglobal.org/>`_ that
provides an implementation of the Caliper Sensor API.

.. note::

   Access to this draft code is reserved for IMS Contributing Members who are
   active participants of the IMS Learning Analytics Task Force. Dissemination
   of this code to outside participants is strictly prohibited. By accessing
   these materials you agree to abide by these rules. This code is in draft
   form and will change substantially.

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


Build and install
=================
To build the library and use, follow these steps:

#. Still to do -- write new instructions for build and install.

.. ..
   ..
      Historical instructions from Prashant's original work

      .. highlight:: bash

      #. Clone the `repository from github
         <https://github.com/IMSGlobal/caliper-python.git>`_ into your desired
         application directory::

           git clone https://github.com/IMSGlobal/caliper-python.git

      #. Set the URL for your Sensor endpoint in :file:`caliper/options.py`.

      #. To test the project, run :file:`test-caliper.py` in the repository's top
         directory::

           python test-caliper.py

      #. Build the package, in the repository's top directory::

           python setup.py build

         If you need to create a distribution of the package, you can use these
         command lines (from the top directory) to build a binary, or source,
         distribution::

           python setup.py sdist
           python setup.py bdist

      #. Install the package into your local python environment::

           python setup.py install


      Using the library
      =================
      After installation, you can use the library in your code, like this:

      .. code-block:: python

         import caliper
         import caliper.utils

         # ... your code here

         caliper.init("YOUR_API_KEY", log_level

      Happy coding!
   ..
.. ..

Copyright and License
=====================
©2014 IMS Global Learning Consortium, Inc.  All Rights Reserved.
For license information contact, info@imsglobal.org
