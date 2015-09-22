#!/usr/bin/env python3


"""
distutils/setuptools install script.
"""

import os
import re
import sys
from codecs import open

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

_packages = [ 'caliper',
              'caliper.extern',
              'caliper.util',
              'caliper_tests' ]

_requires = [ 'future >= 0.14.3',
              'oauthlib >= 0.7.2',
              'requests >= 2.7.0' ]

_fixtures = [ 'fixtures_local/*.json',
              'fixtures_common/src/test/resources/fixtures/*.json' ]

def _get_val_from_mod(k):
    with open('caliper/__init__.py', 'r') as fd:
        return re.search(r'^__{0}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(k),
                         fd.read(),
                         re.MULTILINE).group(1)

_author = _get_val_from_mod('author')
_license = _get_val_from_mod('license')
_title = _get_val_from_mod('title')
_version = _get_val_from_mod('version')

with open('README.rst', 'r', 'utf-8') as f:
          _readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
          _history = f.read()

setup(
    name = _title,
    version = _version,
    description = 'Caliper API for Python. Provides implementation for the IMS Caliper Sensor API.',
    long_description = _readme + '\n\n' + _history,
    maintainer = _author,
    maintainer_email = 'info@imsglobal.org',
    url = 'https://github.com/IMSGlobal/caliper-python',
    packages = _packages,
    package_data = {'caliper_tests' : _fixtures },
    install_requires = _requires,
    license = _license,
    zip_safe = False,
    classifiers = (
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ),
)
