#!/usr/bin/env python3
"""
distutils/setuptools install script.
"""

import os
import re
import sys
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

_packages = ['caliper', 'caliper.util']
_test_requirements = ['pytest', 'pytest-cov', 'responses', 'tox']

with open('requirements.txt', 'r', 'utf-8') as fd:
    _install_requirements = fd.read().splitlines()

with open('README.rst', 'r', 'utf-8') as f:
    _readme = f.read()


def _get_val_from_mod(k):
    with open('caliper/__init__.py', 'r', 'utf-8') as fd:
        return re.search(r'^__{0}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(k), fd.read(),
                         re.MULTILINE).group(1)


_author = _get_val_from_mod('author')
_license = _get_val_from_mod('license')
_title = _get_val_from_mod('title')
_version = _get_val_from_mod('version')

setup(
    name=_title,
    version=_version,
    description='Caliper API for Python. Provides implementation for the IMS Caliper Sensor API.',
    long_description=_readme + '\n\n',
    maintainer=_author,
    maintainer_email='info@imsglobal.org',
    url='https://github.com/IMSGlobal/caliper-python',
    packages=_packages,
    install_requires=_install_requirements,
    tests_require=_test_requirements,
    license=_license,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Beta', 'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python', 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy'
    ])
