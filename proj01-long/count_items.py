"""
File: count_items.py
Author: Ming Wang
Purpose: Counts the number of items per value within a dictionary and updates
the value for each key that is the dictionary, but updating it's value, by either adding or subtracting
the total for each key if a key appears multiple times. And if it doesn't appear multiple times then
it will create a new key. Printing out the ascending order of the keys.
"""
import os


def main():
    this_script = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    file_name = input()
    word_count = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                pop = line.split()
                if len(pop) < 2:
                    continue
                try:
                    value = int(pop[-1])
                    word = str(pop[0])
                    if word in word_count:
                        word_count[word] += value
                    else:
                        word_count[word] = value
                except ValueError:
                    # checks to ensure the second value entered is an integer
                    print(f"Error: The last value in the line '{line.strip()}' is not an integer.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return


    word_count_sorted = {key: value for key, value in sorted(word_count.items(), key=lambda item: (str(item[0]), item[1]))}

    # STEP 1: Print the original dictionary
    print("File to scan: " +"STEP 1: THE ORIGINAL DICTIONARY")
    for key, value in word_count_sorted.items():
        print(f"  Key: {key} Value: {value}")

    # convert the dictionary to a list of (value, key) tuples
    items = [(value, key) for key, value in word_count_sorted.items()]
    print()
    # STEP 2: Print the list of value->key tuples
    print("STEP 2: A LIST OF VALUE->KEY TUPLES")
    print(items)
    print()
    # Sort the list of tuples based on the values (which are the first elements in the tuples)
    items.sort()

    # STEP 3: Print the sorted list of tuples
    print("STEP 3: AFTER SORTING")
    print(items)

    # create a new sorted dictionary based on the sorted list of tuples
    sorted_word_count = {key: value for value, key in items}
    print()
    # STEP 4: Print the final output
    print("STEP 4: THE ACTUAL OUTPUT")
    for key, value in sorted_word_count.items():
        print(key, value)


if __name__ == "__main__":
    main()
