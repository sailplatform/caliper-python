#!/usr/bin/env python3


"""
distutils/setuptools install script.
"""

import os
import sys
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

_packages = ['caliper']

_requires = ['requests >= 2.0.0',
            'rfc3987 >= 1.3.4',
            'six >= 1.8.0',
             ]

with open('README.rst', 'r', 'utf-8') as f:
          readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
          history = f.read()

setup(
    name = 'caliper-python',
    version = caliper.__version__,
    description = 'Caliper API for Python. Provides implementation for the IMS Caliper Sensor API.',
    long_description = readme + '\n\n' + history,
    maintainer = 'IMS Global',
    maintainer_email = 'info@imsglobal.org',
    url = 'https://github.com/IMSGlobal/caliper-python',
    packages = _packages,
    package_data = {'': ['LICENSE', 'NOTICE' ] },
    include_package_data = True,
    install_requires = _requires,
    license = 'GPLv3',
    zip_safe = False,
    classifiers = (
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
