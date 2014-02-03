
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import caliper-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'caliper'))
from version import VERSION

long_description = '''
caliper API for Python.  Provides implementation for Caliper Sensor API

'''

setup(
    name='caliper-python',
    version=VERSION,
    url='https://github.com/IMSGlobal/caliper-python.git',
    author='Prashant Nayak',
    author_email='prashant@intellifylearning.com',
    maintainer='IMS Global',
    maintainer_email='info@imsglobal.org',
    packages=['caliper'],
    license='IMS Global',
    install_requires=[
        'requests',
        'python-dateutil'
    ],
    description='caliper API for Python.  Provides implementation for Caliper Sensor API',
    long_description='caliper API for Python.  Provides implementation for Caliper Sensor API'
)
