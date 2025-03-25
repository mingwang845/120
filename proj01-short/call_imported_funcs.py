"""
    File:call_imported_funcs.py
    Author:Ming Wang
    Purpose: Computes functions foo, bar, and baz by
    importing them and then generating results using
    the functions from short1_thing
"""

#import short1_thing functions
from short1_thing import *

#prompts and ask the users to the inputs
oneLine = input()
secondLine = input()
thirdLine = input()

#initializes and generates foo
fooValue = foo(str(oneLine))
print(fooValue)
#initializes and generates bar

barValue = bar(str(oneLine), str(secondLine), str(thirdLine))
print(barValue)

#initializes and generates baz by using the bar and food results
bazValue = baz(fooValue, barValue)
print(bazValue,)



