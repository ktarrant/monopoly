# board.py - module for board class

import sys
from xml.etree.ElementTree import ElementTree
import generate
import quickies

default_board_fn = "default.board.xml"

class Property:
	# Name and position are necessary members
	def __init__(self):
		pass

	def __str__(self):
		head = "<Property object '%s'" % self.name
		head = " ".join([head, \
			"(Pos. %d)" % self.position, \
			"[Grp. '%s']" % self.group])

		elems = []
		try: elems.append("price=%d" % self.price)
		except AttributeError: pass
		try: elems.append("rent=%d" % self.rent)
		except AttributeError: pass

		if elems is not []:
			head += " {" + " ".join(elems) + "}"
		return head


class Board(ElementTree):
	#def __init__(self, filename=default_board_fn):
	#	try:
	#		self.parse(filename)
	#	except IOError:
	#		print("Board file '%s'  not found.\
	#			Generating default..." % filename)
	#		generate.printDefaultBoard(default_board_fn)
	#	this.parse(default_board_fn)

	def parse(self, filename, parser=None):
		super().parse(filename, parser)
		self.updateProperties()

		
	def updateProperties(self):
		root = self.getroot()
		assert(root.tag=="map")
		self.boardName = root.attrib.get("name")
		self.properties = []
		print("Parsing '%s'... " % self.boardName, end="")
		for prop in root:
			np = Property()
			np.position = int(prop.attrib.get("position"))
			np.name = prop.find("name").text
			np.group = prop.find("group").text
			try: np.price = int(prop.find("price").text)
			except AttributeError: pass
			try: np.rent = int(prop.find("rent").text)
			except AttributeError: pass
			self.properties.append(np)
		print("Success!")

	"""def loadProperties(self, filename):
		tree = ET.parse(filename)
		root = tree.getroot()
		assert(root.tag == "map")
		self.name = root.attrib.get("name")
		print("Parsing '%s'." % self.name)"""


if __name__ == "__main__":
	b = Board()
	b.parse(default_board_fn)