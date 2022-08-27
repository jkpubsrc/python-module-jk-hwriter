jk_hwriter
==========

Introduction
------------

This python module provides a single class: A buffer that can be used to create indented output. This is useful for producing pretty printed texts for XML, HTML or programming languages.

Information about this module can be found here:

* [github.com](https://github.com/jkpubsrc/python-module-jk-hwriter)
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

### Producing output

For producing output you now can use the class `HWriter2`. This class provides the following methods:

* `write(...)` : Write some output to the current line.
* `writeLn(...)` : Write something and automatically add a single line break. If you don't output something this method will behave exactly as you would call `lineBreak()`
* `lineBreak()` : Perform a line break. This line break is ignored if the very last output already was a line break.
* `doubleLineBreak()` : Perform a double line break. This line break is ignored if the very last output already was a double line break.
* `incrementIndent()` : Perform a sinlge line break and increment indent.
* `decrementIndent()` : Perform a sinlge line break and decrement indent.

Example:

```python
w = HWriter2()
w.write("Foo Bar")
w.incrementIndent()
w.write("foo")
w.incrementIndent()
w.write("bar")
w.decrementIndent()
w.decrementIndent()
w.write("Foo Bar")
```

### Context manager

You can use the `HWriter` as context manager:

```python
w = HWriter2()
w.write("Foo Bar")
with w:
	w.write("foo")
	with w:
		w.write("bar")
w.write("Foo Bar")
```

Contact
-------

This work is open source. This way you can use this work for free.

Please note that this also enables you to make a contribution. We, the subspecies of software developers, can make great things. However, the more we all work together, the more fantastic these things can get. Therefore feel free to contact the author(s) listed below, either for giving feedback, provide comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



