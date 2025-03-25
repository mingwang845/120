"""
    File:strings_and_input.py
    Author:Ming Wang
    Purpose: The program will read an input string from the
    user. A prompt will be printed, additionally the code
    will execute various prints.
"""

stringInput = str(input())
stringLen = len(stringInput)
print("input string:", stringLen)
print(stringInput[1])
# prints the first ten values in the string.
if stringLen >= 10:
    print(stringInput[:10])
else:
    print(stringInput)
# prints the last five values in the string.
if stringLen > 5:
    print(stringInput[-5:])
else:
    print(stringInput)
# prints a all caps stringInput
print(stringInput.upper())
# checks to see if what the value of the value in the input is
if stringInput[0] in "qwertyQWERTY":
    print("QWERTY")
elif stringInput[0] in "uiop":
    print("UIOP")
elif stringInput[0].isalpha():
    print("LETTER")
elif stringInput[0].isdigit():
    print("DIGIT")
else:
    print("OTHER")
# asks user to enter two values and then multiple them together
# to print out an answer
firstNum = int(input())
secondNum = int(input())
print(firstNum * secondNum)