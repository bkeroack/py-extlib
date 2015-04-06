__author__ = 'bk'

from typecheck import typecheck
import typecheck as tc
import collections.abc as abc

@typecheck
def filter_dict_keys(obj: abc.MutableMapping, char: str, rep: str):
    '''
    Recursively replaces char in nested dict keys with rep (for sanitizing input to mongo, for example)
    '''
    new_obj = obj
    for k in new_obj:
            if isinstance(k, list):
                filter_dict_keys(k, char, rep)
            if isinstance(obj, dict):
                if isinstance(obj[k], dict):
                        filter_dict_keys(obj[k], char, rep)
                if char in k:
                        obj[k.replace(char, rep)] = obj[k]
                        del obj[k]

@typecheck
def insert_node(obj: abc.MutableMapping, path: abc.Sequence, value):
    '''
    In the dict-like obj (assumed to be a nested set of dicts), walk path and insert value.
    '''
    for k in path[:-1]:
        obj = obj.setdefault(k, {})
    obj[path[-1]] = value

@typecheck
def get_paths(obj: abc.MutableMapping, path: tc.optional(abc.MutableSequence)=None):
    '''
    Given an arbitrarily-nested dict-like object, generate a list of unique tree path tuples.
    The last object in any path will be the deepest leaf value in that path.
    '''
    path = path if path else list()
    unique_paths = list()
    for i, item in enumerate(obj.items()):
        if isinstance(item[1], abc.Mapping):
            for nested_item in get_paths(item[1], path=path+[item[0]]):
                unique_paths.append(nested_item)
        else:
            unique_paths.append(tuple(path + [item[0]] + [item[1]]))
    return unique_paths


@typecheck
def bfs(tree: dict, start: str, end: str) -> tc.optional(tc.seq_of(str)):
    '''
    Breadth-first search.
    Requires tree in adjacency list representation. Assumes no cycles.
    '''
    q = [[start]]
    while q:
        print("q: {}".format(q))
        p = q.pop(0)
        print("p: {}".format(p))
        node = p[-1]
        if node == end:
            return p
        for adj in tree.get(node, []):
            print("adj: {}".format(adj))
            np = list(p)
            np.append(adj)
            q.append(np)

@typecheck
def dfs(tree: dict, start: str, end: str) -> tc.optional(tc.seq_of(str)):
    '''
    Similar to above except depth-first search
    '''
    s = [[start]]
    while s:
        print("s: {}".format(s))
        p = s.pop()
        print("p: {}".format(p))
        node = p[-1]
        if node == end:
            return p
        for adj in tree.get(node, []):
            print("adj: {}".format(adj))
            np = list(p)
            np.append(adj)
            s.append(np)


@typecheck
def adjacency_list(tree: dict) -> dict:
    '''
    Given a nested dictionary, return nodes in adjacency list format
    '''
    edges = {}
    for item in tree.items():
        if isinstance(item[1], dict):
            keys = [k for k in item[1].keys()]
            edges[item[0]] = edges[item[0]] + keys if item[0] in edges else keys
            nested_edges = adjacency_list(item[1])
            for ne in nested_edges:
                edges[ne] = edges[ne] + nested_edges[ne] if ne in edges else nested_edges[ne]
        else:
            edges[item[0]] = edges[item[0]] + [item[1]] if item[0] in edges else [item[1]]
    return edges