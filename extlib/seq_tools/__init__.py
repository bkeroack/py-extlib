__author__ = 'bk'

from typecheck import typecheck
import typecheck as tc
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

@typecheck
def merge_sort(list_obj: list) -> tc.optional(list):
    '''
    Sorts in place. Mutates input argument.
    '''
    print("Splitting ", list_obj)
    if len(list_obj) > 1:
        mid = len(list_obj)//2
        left = list_obj[:mid]
        right = list_obj[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_obj[k] = left[i]
                i += 1
            else:
                list_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_obj[k] = right[j]
            j += 1
            k += 1
    print("Merging ", list_obj)

@typecheck
def quick_sort(list_obj: list) -> list:
    '''
    Returns sorted list
    '''
    if not list_obj:
        return list_obj
    else:
        pivot = list_obj[0]
        lesser = quick_sort([x for x in list_obj[1:] if x < pivot])
        greater = quick_sort([x for x in list_obj[1:] if x >= pivot])
        return lesser + [pivot] + greater
