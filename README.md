Python Extended Lib
===================

Random snippets of code that I have found useful/essential.


extlib.logging
--------------

```LoggingMetaClass```

Log the parameters and return value of every method call on class (debug log via logging.debug).

**CAUTION**: may be extremely verbose if you pass a lot of data in method parameters or return values

Usage:

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


extlib.tree_tools
-----------------

```change_dict_keys(obj, char, rep)```

Given a nested dictionary object of arbitrary depth ```obj```, replace any instances of ```char``` found in keys with
```rep```. 

**NOTE**: modifies ```obj``` in place (returns None).

Example: (sanitizing nested dictionaries for MongoDB which does not allow '.' in keys):
    
    data = { "foo.bar": "baz.123" }
    change_dict_keys(data, '.', '_')
    print(data)
    # { "foo_bar": "baz.123 }
    


```set_dict_key(obj, path, value)```

Given a nested dictionary object of arbitrary depth ```obj```, walk ```path``` and insert ```value```.


**NOTE**: modifies ```obj``` in place (returns None)

Example:
    
    obj = {
        'app': {
            'myapp': { }
        }
    }
    path = ('app', 'myapp', 'builds')
    value = { 'foo': 'bar' }
    set_dict_key(obj, path, value)
    print(json.dumps(obj, indent=4))
    #{
    #    'app': {
    #        'myapp': {
    #            'builds': {
    #                'foo': 'bar'
    #            }
    #        }
    #    }
    #}
    
**paths_from_nested_dict(obj, path=None)**

Given an arbitrarily-nested dict-like object, generate a list of unique tree path tuples.
The last object in any path will be the deepest leaf value in that path.

Example:

    dict_obj = {
        'a': {
            0: 1,
            1: 2
        },
        'b': {
            'foo': 'bar'
        }
    }

    paths = paths_from_nested_dict(dict_obj)
    # returns:
    #[
    #    ('a', 0, 1),
    #    ('a', 1, 2),
    #    ('b', 'foo', 'bar')
    #]
    
    
extlib.seq_tools
----------------

**flatten(list_obj)**

Iterate through n-dimensional list yielding items

Example:

   my_list = [ "foo", [ 1, 2, (3,) ], "bar" ]
   for i in flatten(my_list):
       print(i)
   # output:
   # foo
   # 1
   # 2
   # 3
   # bar
   
**flatten_list(list_obj)**
    
Flatten n-dimensional list

Example:

   my_list = [ "foo", [ 1, 2, (3,) ], "bar" ]
   flattened = flatten_list(my_list)
   # returns:
   # [ "foo", 1, 2, 3, "bar" ]
   

extlib.zip
----------

**zipfolder(path, zipname, subpath="")**

Create zip archive of a directory ("folder"), preserving layout and filenames. Prepend subpath to all archive paths if supplied.

Example:

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
   
   zipfolder("./foo", "foo_archive2.zip", "foobar/zzz")
   
   # foo_archive2.zip contents:
   # foobar/zzza.txt
   # foobar/zzzb.dat
   # foobar/zzzdata/c.dat
   # foobar/zzzbar/baz/d.txt
   