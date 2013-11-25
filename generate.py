# monopoly.py -  A simple implementation of Monopoly in python3.3

import sys

names="Mediterranean Ave.\n\
Baltic Ave.\n\
Oriental Ave.\n\
Vermont Ave.\n\
Connecticut Ave.\n\
St. Charles Place\n\
States Ave.\n\
Virginia Ave.\n\
St. James Place\n\
Tennessee Ave.\n\
New York Ave.\n\
Kentucky Ave.\n\
Indiana Ave.\n\
Illinois Ave.\n\
Atlantic Ave.\n\
Ventnor Ave.\n\
Marvin Gardens\n\
Pacific Ave.\n\
North Carolina Ave.\n\
Pennsylvania Ave.\n\
Park Place\n\
Boardwalk\n\
Electric Company\n\
Water Works\n\
Reading Railroad\n\
Pennsylvania Railroad\n\
B. & O. Railroad\n\
Short Line Railroad\n\
GO\n\
Jail\n\
Free Parking\n\
Go to Jail\n\
Community Chest\n\
Chance\n\
Community Chest\n\
Chance\n\
Community Chest\n\
Chance"

def fixStringForXml(str):
	str = str.replace("&", "&amp;")
	str = str.replace("<", "&lt;")
	str = str.replace(">", "&gt;")
	str = str.replace("\"", "&quot;")
	str = str.replace("'", "&apos;")
	return str

names = fixStringForXml(names)
names = names.split("\n");

positions=[2, 4, 7, 9, 10, 12, 14, 15, 17, 19, \
	20, 22, 24, 25, 27, 28, 30, 32, 33, 35, \
	38, 40, 13, 29, 6, 16, 26, 36, 1, 11, 21, \
	31, 3, 8, 18, 23, 34, 37]

positions = list(map(lambda x : x - 1, positions))

prices=[60, 60, 100, 100, 120, 140, \
	140, 160, 180, 180, 200, 220, \
	220, 240, 260, 260, 280, 300, \
	300, 320, 350, 400, 150, 150, \
	200, 200, 200, 200, \
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	# 10 special props

# properties = rent, utilities = multiplier, special = 0
rents=[2, 4, 6, 6, 8, 10, 10, 12, 14, 14, \
	16, 18, 18, 20, 22, 22, 22, 26, 26, 28, 35, 50, \
	4, 4, \
	50, 50, 50, 50, \
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

groups="Purple\n\
Purple\n\
Light-Green\n\
Light-Green\n\
Light-Gree\n\
Violet\n\
Violet\n\
Violet\n\
Orange\n\
Orange\n\
Orange\n\
Red\n\
Red\n\
Red\n\
Yellow\n\
Yellow\n\
Yellow\n\
Dark-Green\n\
Dark-Green\n\
Dark-Green\n\
Dark-Blue\n\
Dark-Blue\n\
Utilities\n\
Utilities\n\
Railroad\n\
Railroad\n\
Railroad\n\
Railroad\n\
Corner\n\
Corner\n\
Corner\n\
Corner\n\
Community Chest\n\
Chance\n\
Community Chest\n\
Chance\n\
Community Chest\n\
Chance"

groups = fixStringForXml(groups)
groups = groups.split("\n")

assert(len(names) == len(positions))
assert(len(names) == len(groups))
assert(len(names) == len(prices))
assert(len(names) == len(rents))

def getPropertyElement(name, position, price, rent, group):
	str = "\t<property position=\"%d\">\n" % position
	str += "\t\t<name>%s</name>\n" % name
	str += "\t\t<group>%s</group>\n" % group
	if (price != 0): str += "\t\t<price>%d</price>\n" % price
	if (rent != 0): str += "\t\t<rent>%d</rent>\n" % rent
	str += "\t</property>\n"
	return str

def printDefaultBoard(filename=None):
	if (filename is None):
		print("Printing default board to stdout.")
		output = sys.stdout
	else:	
		print("Printing default board to '%s'." % filename)
		output = open(filename, "w")
	output.write("<?xml version='1.0' encoding='us-ascii'?>\n\n")
	output.write("<map name=\"default\">n\">\n")
	for msg in map(getPropertyElement, \
	names, positions, prices, rents, groups):
		output.write(msg)
	output.write("</map>\n")
	if (output is not sys.stdout): output.close()

if __name__ == "__main__":
	printDefaultBoard()


