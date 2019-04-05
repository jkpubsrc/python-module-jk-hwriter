#!/usr/bin/python3




from jk_hwriter import *


w = HWriter()
w.write("Top level text")
w.writeLn()
w.incrementIndent()
w.writeLn("Indented text 1")
w.writeLn("Indented", "text", " 2")
w.incrementIndent()
w.writeLn("More indented text 1")
w.writeLn()
w.writeLn()
w.lineBreak()
w.lineBreak()
w.writeLn("More indented", "text", " 2")
w.decrementIndent()
w.decrementIndent()
w.writeLn(["Some", " more", " top", " level", " text"])
w.writeLn("End.")


print(w)


print()
for line in w.getLines():
	print(repr(line))



assert w.getLines() == [
	'Top level text',
	'\tIndented text 1',
	'\tIndentedtext 2',
	'\t\tMore indented text 1',
	'',
	'',
	'\t\tMore indentedtext 2',
	'Some more top level text',
	'End.',
]








