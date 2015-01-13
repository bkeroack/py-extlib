__author__ = 'bk'

import collections

def flatten(list_obj):
    '''
    Iterate through n-dimensional list yielding items
    '''
    assert list_obj
    assert isinstance(list_obj, collections.Iterable)
    for item in list_obj:
        if isinstance(item, collections.Iterable) and not type_check.is_string(item):
            for x in flatten(item):
                yield x
        else:
            yield item

def flatten_list(list_obj):
    '''
    Flatten n-dimensional list
    '''
    return [x for x in flatten(list_obj)]