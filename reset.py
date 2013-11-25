# reset.py - resets the program file's state to a default value

import os

def reset():
	print("Deleting default.board.xml ...")
	os.remove("default.board.xml")


if __name__ == "__main__":
	print("This script will reset this program's state to an \
	uninitialized\nstate. Are you sure you want to do this?\n")
	response = input("y/n: ")
	if response.tolower() == "y": reset()
		
