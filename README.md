PyRP
====

Python-based Runtime Platform

Using a development environment
-------------------------------

Commands can be run through:
```shell
$ bin/pyrp-env COMMAND
```

There is an interactive shell for development:
```shell
$ bin/pyrp-env
[$] COMMAND
```

The file interpreter
--------------------

The basic usage of pyrp is:
```shell
$ pyrp FILE
```

Writting PyRP code
------------------

See code examples in the ``examples`` directory.

Testing PyRP
------------

There is an automated testing suite.
```shell
$ pyrp-test
```
This will run all tests located at the ``tests`` directory.
