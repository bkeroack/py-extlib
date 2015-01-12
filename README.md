Python Extended Lib
===================

Random snippets of code that I have found useful/essential.


extlib.logging
--------------

```LoggingMetaClass```

Log the parameters and return value of every method call on class (debug log via logging.debug).

**CAUTION**: may be extremely verbose if you pass a lot of data in method parameters or return values

Usage:

```
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

extlib.dict_tools
-----------------

```change_dict_keys(obj, char, rep)```

Given a nested dictionary object of arbitrary depth ```obj```, replace any instances of ```char``` found in keys with
```rep```. 

**NOTE**: modifies ```obj``` in place (returns None).

Example: (sanitizing nested dictionaries for MongoDB which does not allow '.' in keys):
```
data = { "foo.bar": "baz.123" }
change_dict_keys(data, '.', '_')
print(data)
# { "foo_bar": "baz.123 }
```


```set_dict_key(obj, path, value)```

Given a nested dictionary object of arbitrary depth ```obj```, walk ```path``` and insert ```value```.


**NOTE**: modifies ```obj``` in place (returns None)

Example:
```
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
```