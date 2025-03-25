"""
    File: indentation_print.py
    Author: Ming Wang
    Purpose: Computes and counts the number of indents
    before each line that the user inputs and then prints
    the number of indents in this case spaces before the first
    letter appears. And if it's a blank line it prints 0.
"""

while True:
    try:
        # prompts and asks the user for input
        userLine = input()
    except EOFError:
        break

    # checks to see if the user inputted "quit" to exit the loop
    if userLine.strip() == "quit":
        break

    # count represents the count of indents
    count = 0
    # for loop to count the number of leading spaces
    for x in userLine:
        if x != " ":
            break
        count += 1

    # print 0 if the line is empty or consists only of spaces
    if count == len(userLine):
        print(0)
    else:
        print(count)
