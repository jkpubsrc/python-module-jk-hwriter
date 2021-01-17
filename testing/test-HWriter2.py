#!/usr/bin/python3



from jk_testing import *

from jk_hwriter import *




@TestCase()
def test_1(ctx):
	w = HWriter2()
	w.write("Foo Bar")

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
		]
	)
#



@TestCase()
def test_2(ctx):
	w = HWriter2()
	w.writeLn("Foo Bar")

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
		]
	)
#



@TestCase()
def test_3(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	w.writeLn()
	w.writeLn()

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
		]
	)
#



@TestCase()
def test_4(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	w.lineBreak()

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
		]
	)
#



@TestCase()
def test_5(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	w.lineBreak()
	w.write("foo")

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
			"foo"
		]
	)
#



@TestCase()
def test_6(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	w.doubleLineBreak()

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
			""
		]
	)
#



@TestCase()
def test_7(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	w.doubleLineBreak()
	w.write("foo")

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
			"",
			"foo"
		]
	)
#



@TestCase()
def test_100(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	w.incrementIndent()
	w.write("foo")
	w.incrementIndent()
	w.write("bar")
	w.decrementIndent()
	w.decrementIndent()
	w.write("Foo Bar")

	w.dump()

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
			"\tfoo",
			"\t\tbar",
			"Foo Bar",
		]
	)
#



@TestCase()
def test_101(ctx):
	w = HWriter2()
	w.write("Foo Bar")
	with w:
		w.write("foo")
		with w:
			w.write("bar")
	w.write("Foo Bar")

	Assert.isEqual(
		w.toLines(),
		[
			"Foo Bar",
			"\tfoo",
			"\t\tbar",
			"Foo Bar",
		]
	)
#








testDriver = TestDriver()

results = testDriver.runTests([
	(test_1, True),
	(test_2, True),
	(test_3, True),
	(test_4, True),
	(test_5, True),
	(test_6, True),
	(test_7, True),
	(test_100, True),
	(test_101, True),
])

reporter = TestReporterHTML()
reporter.report(results)






