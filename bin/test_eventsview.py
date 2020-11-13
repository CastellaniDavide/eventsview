"""Test eventsview file
"""
from eventsview import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-11-13"

def test():
	"""Tests the eventsview function in the eventsview class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert eventsview.eventsview() == "eventsview", "test failed"
	#assert eventsview.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
