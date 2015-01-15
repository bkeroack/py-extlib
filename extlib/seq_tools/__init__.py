__author__ = 'bk'

from typecheck import typecheck
import collections.abc as abc
import collections


@typecheck
def flatten(list_obj: abc.MutableSequence):
    '''
    Iterate through n-dimensional list yielding items
    '''
    for item in list_obj:
        if isinstance(item, collections.Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item

@typecheck
def flatten_list(list_obj: abc.MutableSequence):
    '''
    Flatten n-dimensional list
    '''
    return [x for x in flatten(list_obj)]