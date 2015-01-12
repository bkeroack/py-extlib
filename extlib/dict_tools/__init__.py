__author__ = 'bk'

def change_dict_keys(obj, char, rep):
    '''
    Recursively replaces char in nested dict keys with rep (for sanitizing input to mongo, for example)
    '''
    new_obj = obj
    for k in new_obj:
            if isinstance(k, list):
                change_dict_keys(k, char, rep)
            if isinstance(obj, dict):
                if isinstance(obj[k], dict):
                        change_dict_keys(obj[k], char, rep)
                if char in k:
                        obj[k.replace(char, rep)] = obj[k]
                        del obj[k]

def set_dict_key(obj, path, value):
    '''
    In the dict-like obj (assumed to be a nested set of dicts), walk path and insert value.
    '''
    for k in path[:-1]:
        obj = obj.setdefault(k, {})
    obj[path[-1]] = value

def paths_from_nested_dict(dict_obj, path=None):
    '''
    Given an arbitrarily-nested dict-like object, generate a list of unique tree path tuples.
    The last object in any path will be the deepest leaf value in that path.
    Ex:
    dict_obj = {
        'a': {
            0: 1,
            1: 2
        },
        'b': {
            'foo': 'bar'
        }
    }

    returns:
    [
        ('a', 0, 1),
        ('a', 1, 2),
        ('b', 'foo', 'bar')
    ]

    @type dict_obj: dict
    @type path: list
    '''
    assert not path or hasattr(path, '__getitem__')
    assert type_check.is_dictlike(dict_obj)
    assert not path or isinstance(path, list)
    path = path if path else list()
    unique_paths = list()
    for i, item in enumerate(dict_obj.iteritems()):
        if type_check.is_dictlike(item[1]):
            for nested_item in paths_from_nested_dict(item[1], path=path+[item[0]]):
                unique_paths.append(nested_item)
        else:
            unique_paths.append(tuple(path + [item[0]] + [item[1]]))
    return unique_paths