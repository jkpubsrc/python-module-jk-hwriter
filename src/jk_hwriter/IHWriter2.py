

import typing

# import jk_typing
# import jk_utils
# import jk_logging
# import jk_json
# import jk_prettyprintobj

from .TextChunk import TextChunk








class IHWriter2:

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	#
	# Complete the current line (= perform a line break on the current line if it contains data. If it is empty, do nothing.)
	# Increase indentation.
	#
	def incrementIndent(self):
		raise NotImplementedError()
	#

	#
	# Complete the current line (= perform a line break on the current line if it contains data. If it is empty, do nothing.)
	# Decrease indentation.
	#
	def decrementIndent(self):
		raise NotImplementedError()
	#

	#
	# Append the specified element to the current line.
	#
	def write(self, *items:str|TextChunk|list[TextChunk]|tuple[TextChunk]|typing.Any, **data):
		raise NotImplementedError()
	#

	#
	# Append the specified element to the current line.
	# Then perform a line break.
	#
	def writeln(self, *items:str|TextChunk|list[TextChunk]|tuple[TextChunk]|typing.Any, **data):
		self.write(*items, **data)
		self.lineBreak()
	#

	#
	# Perform a line break.
	# This ensures that the end of the buffer contains a line break.
	#
	def lineBreak(self):
		raise NotImplementedError()
	#

	#
	# Perform a double line break.
	# This ensures that the end of the buffer contains an empty line.
	#
	def doubleLineBreak(self):
		raise NotImplementedError()
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

#










