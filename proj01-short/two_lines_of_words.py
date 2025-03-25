"""
    File: two_lines_of_words.py
    Author: Ming Wang
    Purpose: Computes two lines and displays them as lists
    and then by doing so display the len of the combined
    list while also sorting the list using bubble sort.
    Then displaying pairs of values within the lists.
"""

# read the entire input passage
# read the entire input passage
# read the entire input passage

# split the passage into lines
firstInput = input()
secondInput = input()

# gets the first two lines
lineOne = str(firstInput)
lineSecond = str(secondInput)

listOne = lineOne.split()
listTwo = lineSecond.split()

print("The first line was:", listOne)
print("The second line was:", listTwo)
print()

# combined list of listOne and listTwo
combinedList = listOne + listTwo

print("The combination of both lines had", len(combinedList), "words.")
print("The combined set of words was:", combinedList)
print()

# Bubble sort
for x in range(len(combinedList)):
    for j in range(0, len(combinedList) - x - 1):
        if combinedList[j] > combinedList[j + 1]:
            combinedList[j], combinedList[j + 1] = combinedList[j + 1], combinedList[j]

print("After sorting, the words were:", combinedList)
print()

# prints out the pairs for the code
firstLen = len(listOne)
secondLen = len(listTwo)
print("Pairs:")
for x in range(min(firstLen, secondLen)):
    print(f"{x}: {listOne[x]},{listTwo[x]}")
print()
