"""
File: twine.py
Author: Ming Wang
Purpose: Compute and create a twine, where the user
can interact and move around
"""

def checkFiles(fileName):
    """
    Read obstacle coordinates from a file.
    Arguments:
    fileName (str): Name of the file containing obstacle coordinates.
    Return Value:
    list or None: A list of obstacle coordinates as tuples, or None if file is not found.
    Pre-condition:
    The file specified by fileName must exist and be readable.
    Each line in the file should contain two integers separated by whitespace.
    """

    try:
        with open(fileName, 'r') as f:
            content = f.readlines()
            obstacle = []
            for line in content:
                obstacle.append(tuple(map(int, line.split())))
            return obstacle
    except FileNotFoundError:
        return None

def update_north(position, obstacles):
    """
    Move the position north and update the position history.
    Arguments:
    position (list): List of tuples representing the current position history.
    obstacles (list): List of obstacle coordinates (not used in this function).
    Return Value:
    list: Updated position history after moving north.
    Pre-condition: None
    """

    last_position = position[-1]
    new_position = (last_position[0], last_position[1] + 1)
    if new_position in obstacles:
        print("You could not move in that direction, because there is an obstacle in the way.\n"
              + "You stay where you are.")
        return position
    else:
        position.append(new_position)
        return position

def update_south(position, obstacles):
    """
     Move the position south and update the position history.
     Arguments:
     position (list): List of tuples representing the current position history.
     obstacles (list): List of obstacle coordinates (not used in this function).
     Return Value:
     list: Updated position history after moving south.
     Pre-condition:
     None
     """
    last_position = position[-1]
    new_position = (last_position[0], last_position[1] - 1)
    if new_position in obstacles:
        print("You could not move in that direction, because there is an obstacle in the way.\n"
              + "You stay where you are.")
        return position
    else:
        position.append(new_position)
        return position

def update_east(position, obstacles):
    """
    Move the position east and update the position history.
    Arguments:
    position (list): List of tuples representing the current position history.
    obstacles (list): List of obstacle coordinates (not used in this function).
    Return Value:
    list: Updated position history after moving east.
    Pre-condition:
    None
    """
    last_position = position[-1]
    new_position = (last_position[0] + 1, last_position[1])
    if new_position in obstacles:
        print("You could not move in that direction, because there is an obstacle in the way.\n"
              + "You stay where you are.")
        return position
    else:
        position.append(new_position)
        return position

def update_west(position, obstacles):
    """
    Move the position west and update the position history.
    Arguments:
    position (list): List of tuples representing the current position history.
    obstacles (list): List of obstacle coordinates (not used in this function).
    Return Value:
    list: Updated position history after moving west.
    Pre-condition: None
    """
    last_position = position[-1]
    new_position = (last_position[0] - 1, last_position[1])
    if new_position in obstacles:
        print("You could not move in that direction, because there is an obstacle in the way.\n"
        +"You stay where you are.")
        return position
    else:
        position.append(new_position)
        return position
def update_back(position):
    """
    Move back to the previous position in the history.
    Arguments:
    position (list): List of tuples representing the current position history.
    Return Value:
    list: Updated position history after moving back.
    Pre-condition: The position list must contain at least one element.
    """
    if len(position) == 1:
        print("Cannot move back, as you are at the start!")
    else:
        position.pop()
        print("You retrace your steps by one space")
    return position

def crossAmount(position):
    """
    Count occurrences of the current position in the position history.
    Arguments:
    position (list): List of tuples representing the current position history.
    Return Value: None
    Pre-condition: None
    """
    amount = 0
    currentPosition = position[-1]
    for cross in position:
        if cross == currentPosition:
            amount += 1
    print(f"There have been {amount} times in the history when you were at this point.")


def print_map(position, obstacles):
    """
    Print a map representation of the current position and path, including obstacles.
    Arguments:
    position (list): List of tuples representing the current position history.
    obstacles (list): List of obstacle coordinates as tuples.
    Return Value: None
    Pre-condition: None
    """
    print("+-----------+")
    box = [["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
           ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"]]

    for values in position:
        x = int(values[0]) + 6
        y = 5 - int(values[1])
        if 1 <= x <= 11 and 0 <= y <= 10:
            box[y][x] = "."
        if x == 6 and y == 5:
            box[y][x] = "*"

    for obstacle in obstacles:
        x = int(obstacle[0]) + 6
        y = 5 - int(obstacle[1])
        if 1 <= x <= 11 and 0 <= y <= 10:
            box[y][x] = "X"

    lastPosition = position[-1]
    x = int(lastPosition[0]) + 6
    y = 5 - int(lastPosition[1])
    if 1 <= x <= 11 and 0 <= y <= 10:
        box[y][x] = "+"

    for inner_list in box:
        print("".join(inner_list))
    print("+-----------+\n")


def calculate_ranges(position):
    """
    Calculate the furthest extents of the player's path.
    Arguments:
    position (list): List of tuples representing the current position history.
    Return Value: None
    Pre-condition: None
    """
    if not position:
        print("No positions recorded yet.")
        return

    min_x = max_x = position[0][0]
    min_y = max_y = position[0][1]

    for pos in position[1:]:
        if pos[0] < min_x:
            min_x = pos[0]
        elif pos[0] > max_x:
            max_x = pos[0]

        if pos[1] < min_y:
            min_y = pos[1]
        elif pos[1] > max_y:
            max_y = pos[1]

    print(f"The furthest West your twine goes is {min_x}")
    print(f"The furthest East your twine goes is {max_x}")
    print(f"The furthest South your twine goes is {min_y}")
    print(f"The furthest North your twine goes is {max_y}\n")


def check_movement(position, movement, obstacles):
    """
       Process the user's movement command and perform corresponding actions.
       Arguments:
       position (list): List of tuples representing the current position history.
       movement (str): User command indicating the movement direction or action.
       obstacles (list): List of obstacle coordinates.
       Return Value: None
       Pre-condition: None
       Note: This function handles movement commands ('n', 's', 'e', 'w'), backtracking ('back'),
       displaying crossings ('crossings'), showing the map ('map'), and calculating ranges ('ranges').
       """
    if movement == "n":
        update_north(position, obstacles)
    elif movement == "s":
        update_south(position, obstacles)
    elif movement == "w":
        update_west(position, obstacles)
    elif movement == "e":
        update_east(position, obstacles)
    elif movement == "back":
        update_back(position)
    elif movement == "crossings":
        crossAmount(position)
    elif movement == "map":
        print_map(position,obstacles)
    elif movement == "ranges":
        calculate_ranges(position)
    else:
        print(f"ERROR: Invalid command: {movement}")


def main():
    try:
        twineStack = [(0, 0)]
        obstacleInput = input("Please give the name of the obstacles filename, or - for none: \n").strip()
        obstacleList = checkFiles(obstacleInput)

        while True:
                print(f"Current position: {twineStack[-1]}")
                print(f"Your history:     {twineStack}")
                movement = input("What is your next command?\n").strip()

                if not movement:
                    print("You do nothing.\n")
                else:
                    check_movement(twineStack, movement, obstacleList)

    except EOFError:
        pass


if __name__ == "__main__":
    main()
