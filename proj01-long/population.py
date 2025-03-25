"""
    File:population.py
    Author:Ming Wang
    Purpose: Reads an imported file, while using import os to ensure the
    when you are reading files it will read them correctly. THe print of the total
    popultion per state that is listed, it's name and population.
    Lastly printing out the total number of states and total population with all the 
    states combined.
"""

import os


def main():
    this_script = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    fileName = input()
    totalPop = 0
    totalState = 0
    first_state_printed = False  # Variable to track if the first state has been printed or not

    # checks to see if the file exists
    try:
        # if it exists then it will read the file
        with open(fileName, 'r') as file:
            # for loop reads each line of the file and then splits
            for line in file:
                pop = line.split()
                try:
                    # gets the value of the state/territory
                    # gets the population
                    if pop[0].isdigit():
                        continue
                    population = int(pop[-1])
                    state_territory = ' '.join(pop[:-1])

                    # Adding "file: " only before the first state/territory
                    if not first_state_printed:
                        print("file: State/Territory:", state_territory)
                        first_state_printed = True
                    else:
                        print("State/Territory:", state_territory)
                    print("Population:     ", population)
                    print()
                    totalPop += population
                    totalState += 1
                except ValueError:
                    # ensure that the last value in the line is an int
                    print(f"Error: The last value in the line '{line.strip()}' is not an integer.")
    except FileNotFoundError:
        # catchs error if file isn't found
        print(f"Error: The file '{fileName}' was not found.")
    # prints out the total states and total population
    print("# of States/Territories:", totalState)
    print("Total Population:       ", totalPop)


if __name__ == "__main__":
    main()
