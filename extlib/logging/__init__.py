__author__ = 'bk'

import functools
import logging
import collections

def log_wrapper(func):
    @functools.wraps(func)
    def log(*args, **kwargs):
        logging.debug("CALLING: {} (args: {}, kwargs: {}".format(func.__name__, args, kwargs))
        ret = func(*args, **kwargs)
        logging.debug("{} returned: {}".format(func.__name__, ret))
        return ret
    return log


class LoggingMetaClass(type):
    def __new__(mcs, classname, bases, class_dict):
        new_class_dict = dict()
        for attr_name, attr in class_dict.items():
            new_class_dict[attr_name] = log_wrapper(attr) if isinstance(attr, collections.Callable) else attr
        return type.__new__(mcs, classname, bases, new_class_dict)
