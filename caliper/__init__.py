
import version
import logging

VERSION = version.VERSION
__version__ = VERSION

import sys
this_module = sys.modules[__name__]

from stats import Statistics
stats = Statistics()

logging_enabled = True
logger = logging.getLogger('caliper')

def log(level, *args, **kwargs):
    if logging_enabled:
        method = getattr(logger, level)
        method(*args, **kwargs)

def init(secret, **kwargs):
    """Create a default instance of a caliper-python client

    :param str secret: The Caliper API Secret

    Kwargs:

    :param logging.LOG_LEVEL log_level: The logging log level for the client
    talks to. Use log_level=logging.DEBUG to troubleshoot
    : param bool log: False to turn off logging completely, True by default
    : param int flush_at: Specicies after how many messages the client will flush
    to the server. Use flush_at=1 to disable batching
    : param datetime.timedelta flush_after: Specifies after how much time
    of no flushing that the server will flush. Used in conjunction with
    the flush_at size policy
    : param bool async: True to have the client flush to the server on another
    thread, therefore not blocking code (this is the default). False to
    enable blocking and making the request on the calling thread.

    """
    from client import Client

    # if we have already initialized, no-op
    if hasattr(this_module, 'default_client'):
        return

    default_client = Client(secret=secret, stats=stats, **kwargs)

    setattr(this_module, 'default_client', default_client)


def _get_default_client():
    default_client = None
    if hasattr(this_module, 'default_client'):
        default_client = getattr(this_module, 'default_client')
    else:
        sys.stderr.write('Please call caliper.init(secret) ' +
                         'before calling caliper methods.\n')
    return default_client

def describe(entity_type=None, entity_id=None, properties={}, timestamp=None):
    """Describe an entity in the learning graph

    :param str entity_type: Type of entity.  E.g. Course, Person, Activity, etc.

    :param str entity_id: the entity id. 

    : param dict properties: a dictionary with key/value pairs for 
    attributes. You only need to record an attribute once, no need to send it again.
    Accepted value types are string, boolean, ints,, longs, and
    datetime.datetime.

    : param timestamp: Time in millis since epoch.  If this event happened in the
    past, the timestamp  can be used to designate when the identification
    happened.  Careful with this one,  if it just happened, leave it None.
    If you do choose to provide a timestamp, make sure it has a timezone.
    """

    log('debug', 'caliper describe ' +  ' entity_type = ' + entity_type + ' entity_id = ' + entity_id)

    default_client = _get_default_client()
    if default_client:
        default_client.describe(entity_type=entity_type, entity_id=entity_id, properties=properties, timestamp=timestamp)

def measure(action=None, learning_context={}, activity_context={}, timestamp=None):
    """Measure an interaction between entities

    :param str action: type of action - one of the activity metric verbs (e.g. HILIGHT, BOOKMARK, etc.)

    : param dict learning_context: a dictionary with key/value pairs for 
    attributes that describe the learning context

     : param dict activity_context: a dictionary with key/value pairs for 
    attributes that describe the activity context

    : param timestamp: Time in millis since epoch. If this event happened in the
    past, the timestamp  can be used to designate when the identification
    happened.  Careful with this one,  if it just happened, leave it None.
    If you do choose to provide a timestamp, make sure it has a timezone.
    """

    log('debug', 'caliper measure ')

    default_client = _get_default_client()
    if default_client:
        default_client.measure(action=action, learning_context=learning_context, activity_context=activity_context, timestamp=timestamp)

def flush(async=None):
    """ Forces a flush from the internal queue to the server

    :param bool async: True to block until all messages have been flushed
    """
    default_client = _get_default_client()
    if default_client:
        default_client.flush(async=async)


def on_success(callback):
    """
    Assign a callback to fire after a successful flush

    :param func callback: A callback that will be fired on a flush success
    """
    default_client = _get_default_client()
    if default_client:
        default_client.on_success(callback)


def on_failure(callback):
    """
    Assign a callback to fire after a failed flush

    :param func callback: A callback that will be fired on a failed flush
    """
    default_client = _get_default_client()
    if default_client:
        default_client.on_failure(callback)
