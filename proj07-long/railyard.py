"""
    File: railyard.py
    Author: Ming Wang
    Purpose: Creates a railyard game that allows the users to move
    and play a train game by interatcing with the terminal and playing
    moving the trains, until you either "quit" or you move all the trains.
"""

def main():
    """
    This is the main function that access all other functions, and
    is what the user interacts with inorder to play the game
    Arguments: N/A
    Return Value: N/A
    """
    file_name = input("Please give the yard file: \n")
    contents = []

    try:
        with open(file_name, "r") as f:
            contents = f.readlines()
            # Removes the newline character from each line
            contents = [line.strip() for line in contents]

    except FileNotFoundError:
        print(f"ERROR: Could not open the yard file")
        return

    user_input = ""

    while True:
        check_departure(contents)
        print_track(contents)

        if loco_counts(contents) == 0:
            break

        user_input = input("What is your next command?\n\n")

        if user_input.startswith("move"):
            # Extract move parameters from user input
            move_params = user_input.split()[1:]
            if len(move_params) != 3:
                print("ERROR: The only valid command formats are (where each X represents an integer):")
                print("move X X X")
                print("quit")
                print()
            else:
                # Check if move parameters can be converted to integers
                if all(is_valid_integer(param) for param in move_params):
                    # Convert to integers
                    num_cars = int(move_params[0])
                    from_track = int(move_params[1])
                    to_track = int(move_params[2])

                    # Perform the move
                    move(contents, num_cars, from_track, to_track)
                    destination_ct = destination_count(contents)
                else:
                    if not is_valid_integer(move_params[0]):
                        print(f"ERROR: Could not convert the 'count' value to an integer: '{move_params[0]}'")
                    if not is_valid_integer(move_params[1]):
                        print(f"ERROR: Could not convert the 'from-track' value to an integer: '{move_params[1]}'")
                    if not is_valid_integer(move_params[2]):
                        print(f"ERROR: Could not convert the 'to-track' value to an integer: '{move_params[2]}'")
                    print()
        elif user_input == "dump":
            dump(contents)
        elif user_input =="quit":
            print("Quitting!")
            break
        else:
            print(f"ERROR: The only valid command formats are (where each X represents an integer):")
            print("move X X X")
            print("quit")
            print()
        

    pass



def is_valid_integer(s):
    """
    This function checks whether or not the value is an integer.
    Which uses isdigit() however will also check if there is
    a '-' sign if it's negative and then continue on
    Arguments: s is the integer value
    Return Value: returns true if is an int and false if not
    """
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()


def destination_count(arr):
    """
    This functions counts the unqiue destinations with the tracks
    Arguments: arr is an array that contains the tracks of the game
    Return Value: returns the total count of destination
    """
    unique = []
    # The first for loop represents the values within the contents of the tracks
    for value in arr:
        # The second for loop is to iterate through each char in the string of tracks
        for character in value:
            # Checks and adds a unique value into the unique list
            if character not in ('-', 'T') and character not in unique:
                unique.append(character)
            
    return len(unique)

def loco_counts(arr):
    """
    This functions counts the locomotives within the tracks
    Arguments: arr is an array that contains the tracks of the game
    Return Value: returns the total count of locomotives
    """
    loco_count = 0
    for value in arr:
        if value[-2] == 'T':
            loco_count += 1
    return loco_count

def print_track(arr):
    """
    This functions prints out the current track state for the
    user to know what and where can they make there next move.
    Arguments: arr is an array that contains the tracks of the game
    Return Value: N/A
    """
    destination_ct = destination_count(arr)

    i = 1
    loco_count = 0
    # Iterates through the content of the tracks and prints each
    # track out until there aren't any tracks left
    for value in arr:
        if value[-2] == 'T':
            loco_count += 1
        print(f"{i}: {value}")
        i = i + 1
    print("Locomotive count: ", loco_count)
    print("Destination count:", destination_ct)
    print()


def print_departure(arr):
    """
    This functions prints out the depature state of the track out
    Arguments: arr is an array that contains the tracks of the game
    Return Value: N/A
    """
    i = 1
    loco_count = 0
    # Iterates through the content of the tracks and prints each
    # track out until there aren't any tracks left
    for value in arr:
        if value[-2] == 'T':
            loco_count += 1
        print(f"{i}: {value}")
        i = i + 1

def dump(arr):
    """
    This functions will dump out the track and the current
    cars and locomotives that are in each track out, which is 
    mainly used for debugging. 
    Arguments: arr is an array that contains the tracks of the game
    Return Value: N/A
    """
    print("DEBUG OUTPUT:")
    # Iterates and prints out the track value with enumerate
    for i, value in enumerate(arr):
        print(f"Track #{i}")
        print(f"  Length:   {len(value) - 2}")
        content = value.replace('-', '')
        content_list = list(content)
        print(f"  Contents: {content_list[::-1]}")
    print()



def check_departure(arr):
    """
    This functions checks to see if any of the tracks need to be departed
    as departure in this game is automatic once you've met the requirements
    Arguments: arr is an array that contains the tracks of the game
    Return Value: returns True if a track has depatured and false otherwise
    """
    track_number = 1
    # Iterates through the arr track and see whether or not a track can depart
    for i in range(len(arr)): 
        track = arr[i]
        # Check if there is a locomotive on the track
        if 'T' in track:
            # Find all unique destinations on the track
            destinations = set()
            for char in track:
                if char not in ('-', 'T'):
                    destinations.add(char)
            # checks if there is only one destination and it's not empty (no cars), depart
            if len(destinations) == 1 and '' not in destinations:
                destination = destinations.pop() 
                cars_count = track.count(destination)
                print_departure(arr)
                print(f"*** ALERT*** The train on track {track_number}, which had {cars_count} cars, departs for destination {destination}.")
                print()

                # Clear the track after departure (replace cars and 'T' with '-')
                arr[i] = track.replace(destination, '-').replace('T', '-')  
                if lastDepart(arr):
                    print("The last locomotive has departed!")
                    print()
                return True
        track_number += 1
    return False

def move(arr, num_cars, from_track, to_track):
    """
    This functions will do the move commoand the user prompts
    and moves the cars from_track to the to_track and has many rules
    that need to be fulled in order to move without worry. And once moved
    will update the track
    Arguments: arr is an array that contains the tracks of the game
    Return Value: N/A
    """
    from_index = from_track - 1
    to_index = to_track - 1
    from_track_len = len(arr[from_index])
    toLen = len(arr[to_index])
    # All the conditions that need to be meant in order for the move to be possible
    if to_track == from_track:
        print(f"ERROR: The 'to' track is the same as the 'from' track.")
        return
    if num_cars < 0:
        print("ERROR: Cannot move a negative number of cars.")
        return
    if to_index < 0 or to_index > len(arr) -1 or from_index< 0 or from_index > len(arr) -1:
        print("ERROR: The to-track or from-track number is invalid.")
        return 
    # Check if the move is valid
    if 'T' not in arr[from_index]:
        print(f"ERROR: Cannot  move from track {from_track} because it doesn't have a locomotive.")
        return
    if 'T' in arr[to_index]:
        print(f"ERROR: Cannot move to track {to_track} because it already has a locomotive.")
        return
    if len(arr[from_index]) - 2 < num_cars:  # Subtract 2 to exclude 'T' and '-' at the ends
        print(f"ERROR: Track {from_track} does not have {num_cars} cars to move.")
        return
    empty = arr[from_index].replace('-', '')
    if len(empty) < num_cars and 'T' not in empty:
        print(f"ERROR: Cannot move {num_cars} cars from track {from_track} because it doesn't have that many cars.")
        return
    elif len(empty)-1 < num_cars:
        print(f"ERROR: Cannot move {num_cars} cars from track {from_track} because it doesn't have that many cars.")
        return
    lenValues = len(arr[to_index].replace('-', ''))
    if lenValues + num_cars > toLen - 2:
        print(f"ERROR: Cannot move {num_cars} cars to track {to_track} because it doesn't have enough space.")
        return
    # if the empty just contains the locomotive and has no cars then it will move the cars
    if empty == 'T':
        locomotive_position = arr[from_index].index('T')
        updateLocation = locomotive_position - num_cars
        updateTrack = list(arr[to_index])
        updateTrack[-1] = 'T'
        updateTrack = updateTrack[1:]
        updateTrack.append("-")
        arr[to_index] = "".join(updateTrack)
        arr[from_index] = "-" * from_track_len
    else:
        # This else will iterate and update positiosn in the tracks that isn't just
        # only the locomotive but as direction based boxes already within it
        # Perform the move
        locomotive_position = arr[from_index].index('T')

        updateLocation = locomotive_position-num_cars
        fromTrackValues = "".join(arr[from_index][updateLocation:-1])
        toTrackValues = "".join(arr[to_index].strip('-'))
        mutliLen = toLen - len(fromTrackValues) - len(toTrackValues) - 1

        finalToTrackValue = '-'*mutliLen + toTrackValues +fromTrackValues + '-'
        arr[to_index] = finalToTrackValue
        

        updateFrom = []
        # Updates the from track after you've moved the cars to the to_track
        for x in range(len(arr[from_index])):
            if x < updateLocation:
                updateFrom.append(arr[from_index][x])

        emptySpace = "-" * (from_track_len- updateLocation - 1)
        fromTrack = emptySpace + "".join(updateFrom) + "-"
        arr[from_index] = fromTrack


    print(f"The locomotive on track {from_track} moved {num_cars} cars to track {to_track}.")
    print()

def lastDepart(arr):
    """
    This functions checks to see if there is a locomotive at all within
    the track and if there isn't then all the tracks have departed
    Arguments: arr is an array that contains the tracks of the game
    Return Value: return True if all have departed and False otherwise
    """
    # Iterates through the tracks and see whether or not there is a locomotive
    for track in arr:
        if 'T' in track:
            return False 
    return True  




if __name__ == "__main__":
    main()
