Colubrid
========

Programming language interpreter.

Using a development environment
-------------------------------

Commands can be run through:
```shell
$ bin/colubrid-env COMMAND
```

There is an interactive shell for development:
```shell
$ bin/colubrid-env
[$] COMMAND
```

The file interpreter
--------------------

The basic usage of pyrp is:
```shell
$ colubrid FILE
```

Writting Colubrid code
----------------------

See code examples in the ``examples`` directory.

Testing Colubrid
----------------

There is an automated testing suite.
```shell
$ colubrid
```
This will run all tests located at the ``tests`` directory.

Editing Colubrid code with a text editor
----------------------------------------

The Javascript syntax is the most simmilar highlighter to Colubrid.

To set up this as default in vim, you need to add to your vimrc file the
following line:
```viml
au BufNewFile,BufRead, *.clsc set filetype=javascript
```
