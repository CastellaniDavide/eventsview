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
	assert eventsview.check_PC("localhost", 1) == True, "Checker PC fails (personal_code: 1)"
	assert eventsview.check_PC("localhost", 2) == True, "Checker PC fails (personal_code: 1)"
	assert eventsview.check_PC("localhost", 10) == True, "Checker PC fails (personal_code: 1)"

	assert eventsview.make_csv_standard("'test','test'\n'example value','example value 2'\n'example value','example value 2'\n'example value','example value 2'") == "'test','test'\n'example value','example value 2'\n'example value','example value 2'\n'example value','example value 2'", "Maker CSV standard fails (personal_code: 2)"

	assert eventsview.csv2array("'test','test'\n'example value','example value 2'\n'example value','example value 2'\n'example value','example value 2'") == [["'test'","'test'"], ["'example value'","'example value 2'"], ["'example value'","'example value 2'"], ["'example value'","'example value 2'"]], "CSV2Array fails (personal_code: 3a)"
	
	assert eventsview.array2csv([["test","test"], ["example value","example value 2"], ["example value","example value 2"], ["example value","example value 2"]]) == '"test","test"\n"example value","example value 2"\n"example value","example value 2"\n"example value","example value 2"\n', "Array2CSV fails (personal_code: 3b)"

	assert eventsview(), "test failed (personal_code: 0)"
	#assert eventsview.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
