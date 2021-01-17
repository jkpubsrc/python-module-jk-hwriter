

import os
import typing

import jk_typing
import jk_prettyprintobj







class HWriter2(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self):
		self.__lines = []				# holds all completed lines
		self.__nIndent = 0				# holds the current indentation level
		self.__buffer = []				# holds all fragments for the next line to add
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dump(self, ctx:jk_prettyprintobj.DumpCtx):
		ctx.dumpVar("__lines", self.__lines)
		ctx.dumpVar("__nIndent", self.__nIndent)
		ctx.dumpVar("__buffer", self.__buffer)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __len__(self):
		if self.__buffer:
			s = "".join(self.__buffer).rstrip()
			if s:
				return len(self.__lines) + 1
		else:
			return self.__lines
	#

	def write(self, *items):
		for item in items:
			if isinstance(item, str):
				if item:
					self.__buffer.append(item)
			elif hasattr(type(item), "__iter__"):
				for item2 in item:
					s = str(item2)
					if s:
						self.__buffer.append(s)
			else:
				s = str(item)
				if s:
					self.__buffer.append(s)
	#

	def lineBreak(self):
		if self.__buffer:
			s = "".join(self.__buffer).rstrip()
			if s:
				self.__lines.append("\t" * self.__nIndent + s)
			self.__buffer.clear()
	#

	def doubleLineBreak(self):
		self.lineBreak()
		if self.__lines and self.__lines[-1]:
			self.__lines.append("")
	#

	def writeLn(self, *items):
		self.write(*items)
		self.lineBreak()
	#

	def __enter__(self):
		if self.__buffer:
			self.lineBreak()
		self.__nIndent += 1
	#

	def __exit__(self, ex, exType, exStackTrace):
		if self.__buffer:
			self.lineBreak()
		if self.__nIndent == 0:
			raise Exception("Deindentation error!")
		self.__nIndent -= 1
	#

	def incrementIndent(self):
		if self.__buffer:
			self.lineBreak()
		self.__nIndent += 1
	#

	def decrementIndent(self):
		if self.__buffer:
			self.lineBreak()
		if self.__nIndent == 0:
			raise Exception("Deindentation error!")
		self.__nIndent -= 1
	#

	#
	# Get a list of lines (without line breaks).
	#
	def toLines(self) -> typing.List[str]:
		self.lineBreak()
		return list(self.__lines)
	#

	def toString(self) -> str:
		self.lineBreak()
		return "\n".join(self.__lines)
	#

	def __str__(self):
		self.lineBreak()
		return " ".join(self.__lines)
	#

	def __repr__(self):
		return "HWriter<" + str(len(self.__lines)) + " lines>"
	#

#






