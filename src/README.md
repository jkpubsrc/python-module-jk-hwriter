jk_hwriter
==========

Introduction
------------

This python module provides a single class: A buffer that can be used to create indented output. This is useful for producing pretty printed texts for XML, HTML or programming languages.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-hwriter)
* [pypi.python.org](https://pypi.python.org/pypi/jk_hwriter)

Why this module?
----------------

A lot of output generation requires indentation. Furthermore it would be convenient in writing to automatically merge line breaks to beautify output. Therefore this module has been created
that assists in such matter.

How to use this module
----------------------

### Loading the module

If you want to use the functionality provided by this module you're best adviced to include the module with following statement:

```python
from jk_hwriter import *
```

### Producing Output

For producing output you have a variety of methods:

* `write(...)` : This will write the output into the current line.
* `lineBreak()` : Perform a line break. This line break is ignored if the very last output already was a line break.
* `writeLn(...)` : Write something and add a line break.

```python
from jk_hwriter import *
```



Bugs
----

Yes, there will still be some bugs. If you find a bug please report it as an issue on GitHub. Please provide the following information:

* a small python snipplet required to reproduce the bug
* the output of the python snipplet
* the result that you would expect

Thank you!

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



