Python Extended Lib
===================

Random snippets of code that I have found useful/essential.


extlib.logging
--------------

**LoggingMetaClass**

Log the parameters and return value of every method call on class (debug log via logging.debug).

**CAUTION**: may be extremely verbose if you pass a lot of data in method parameters or return values

Usage:

```python
from extlib.logging import LoggingMetaClass

class MyClass:
    __metaclass__ = LoggingMetaClass
    
    def count_msg(msg):
        return len(msg)

mc = MyClass()
mc.count_msg("foobar")
# debug log output:
# CALLING: count_msg (args: ["foobar"], kwargs: {})
# count_msg returned 6
```

extlib.tree_tools
-----------------

**filter\_dict\_keys(obj, char, rep)**

Given a nested dictionary object of arbitrary depth, replace any instances of ``char`` found in keys with
``rep``. 

**NOTE**: modifies ``obj`` in place (returns None).

Example:
    
```python
data = { "foo.bar": "baz.123" }
change_dict_keys(data, '.', '_')
print(data)
# { "foo_bar": "baz.123 }
```


**insert\_node(obj, path, value)**

Given a nested dictionary object of arbitrary depth ``obj``, walk ``path`` and insert ``value``.

**NOTE**: modifies ``obj`` in place (returns None)

Example:

```python
obj = {
    'person': {
        'mary': { }
    },
    'other': [1,2,3]
}
path = ('person', 'mary', 'contact_info')
value = { 'phone': '123-456-7890' }
insert_node(obj, path, value)
print(json.dumps(obj, indent=4))
#{
#    "person": {
#        "mary": {
#            "contact_info": {
#               "phone": "123-456-7890"
#            }
#        }
#    },
#    "other": [ 1, 2, 3 ]
#}
```
    
**get\_paths(obj, path=None)**

Given an arbitrarily-nested dict-like object, generate a list of unique tree path tuples.
The last object in any path will be the deepest leaf value in that path.

Example:

```python
tree_obj = {
    'a': {
        0: 1,
        1: 2
    },
    'b': {
        'foo': 'bar'
    }
}
paths = paths_from_nested_dict(tree_obj)
# returns:
#[
#    ('a', 0, 1),
#    ('a', 1, 2),
#    ('b', 'foo', 'bar')
#]
``` 
    
extlib.seq_tools
----------------

**flatten(list\_obj)**

Iterate through n-dimensional list yielding items

Example:

```python
my_list = [ "foo", [ 1, 2, (3,) ], "bar" ]
for i in flatten(my_list):
   print(i)
# output:
# foo
# 1
# 2
# 3
# bar
```
   
**flatten\_list(list\_obj)**
    
Flatten n-dimensional list

Example:

```python
my_list = [ "foo", [ 1, 2, (3,) ], "bar" ]
flattened = flatten_list(my_list)
# returns:
# [ "foo", 1, 2, 3, "bar" ]
```

extlib.zip
----------

**zipfolder(path, zipname, subpath="")**

Create zip archive of a directory ("folder"), preserving layout and filenames. Prepend subpath to all archive paths if supplied.

Example:

```python
# Files:
# foo/a.txt
# foo/b.dat
# foo/data/c.dat
# foo/bar/baz/d.txt

zipfolder("./foo", "foo_archive.zip")
# foo_archive.zip contents:
# a.txt
# b.dat
# data/c.dat
# bar/baz/d.txt

zipfolder("./foo", "foo_archive2.zip", "foobar/zzz/")
# foo_archive2.zip contents:
# foobar/zzz/a.txt
# foobar/zzz/b.dat
# foobar/zzz/data/c.dat
# foobar/zzz/bar/baz/d.txt
```