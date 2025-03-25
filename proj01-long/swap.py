"""
    File:swap.py
    Author:Ming Wang
    Purpose: Swaps the string based on splitting the string in half
    and then swapping it, if it's even just swap havles, if odd
    then swap order the middle value.
"""

inputString = str(input())
stringStrip = inputString.strip()
lenString = len(stringStrip)
# swaps evenly without worrying about a middle value because the len
# is even
if lenString % 2 == 0:
    firstPart = stringStrip[:lenString//2]
    secondPart = stringStrip[lenString//2:]
    print("Please give a string to swap:", secondPart + firstPart)

# swaps unevenly and will have a middle value and swap around ti
# as a pivot point because the len is odd
else:
    middle = stringStrip[lenString // 2]
    firstPart = stringStrip[:lenString//2]
    secondPart = stringStrip[1 + lenString//2:]
    print("Please give a string to swap:", secondPart + middle + firstPart)


