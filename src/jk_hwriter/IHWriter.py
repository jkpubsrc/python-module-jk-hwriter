

import typing

# import jk_typing
# import jk_utils
# import jk_logging
# import jk_json
# import jk_prettyprintobj







#
# Hierarchical writer.
#
# Please note that the semantics between <code>IHwriter</code> and <code>IHwriter2</code> are slightly different.
# While the interfaces basically are the same, <code>IHwriter</code> will not fold multiple empty lines to single lines
# while <code>IHWriter2</code> implements that behavior.
# Additionally <code>IHwriter2</code> supports <code>TextChunk</code> an can automatically convert those chunks to text as needed.
#
class IHWriter:

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
	def write(self, *items):
		raise NotImplementedError()
	#

	#
	# Append the specified element to the current line.
	# Then perform a line break.
	#
	def writeln(self, *items):
		self.write(*items)
		self.lineBreak()
	#

	#
	# Add a line break if (and only if) the last item was not a line break.
	# Typically you won't want to use this method but <c>writeLn</c> instead.
	# <c>writeLn</c> will add a line in any case.
	#
	def lineBreak(self):
		raise NotImplementedError()
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

#










