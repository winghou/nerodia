import six

from .logger import Logger

__version__ = '0.8.0'

ttc = None

tag_to_class = ttc or {}

#
# Whether or not Watip should wait for an element to be found or present before taking an action.
# Defaults to true.
#

relaxed_locate = True

#
# Default wait time for wait methods.
#

default_timeout = 30

#
# Custom logger
#

logger = Logger()

#
# For py2/py3 compatibility
#

_str_types = (six.binary_type, six.text_type)


from . import tag_map


def element_class_for(tag_name):
    return tag_to_class.get(tag_name)
