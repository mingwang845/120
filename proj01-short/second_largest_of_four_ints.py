"""
    File:second_largest_of_four_ints.py
    Author:Ming Wang
    Purpose: Compute four inputs from a users and outputs the second
    largest value.
"""

# asks the user for the four different int inputs
# assumed to be only int inputs
inputOne = input()
inputTwo = input()
inputThree = input()
inputFour = input()

#converts the inputted string values into int values
w = int(inputOne)
x = int(inputTwo)
y = int(inputThree)
z = int(inputFour)

#creates a list that contains the four values from the input
lst = [w, x, y, z]

#bubble sort is done in order to sort the values 
for i in range(len(lst)):
    for j in range(0, len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j +1] = lst[j+1], lst[j]



print(lst[2])

