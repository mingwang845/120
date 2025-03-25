"""
    File: dijkstra_on_grid.py
    Author: Ming Wang
    Purpose: A grid if provided through a input text,
    and then a user will then choose a coordinate and
    then Dijkstra's alogrithm will be ran on the code.
"""


from dijkstra_node import DijkstraNode
import time

def equalize_lengths(grid_view):
    '''
    This function will ensure that every row will have the same
    length, to ensure that there wouldn't be any index out of bound error
    Arguments:
    grid_view: is a two array of the rid view of the grid that was inputted
    Return Value: returns the update gridview to ensure that every row
    has the same length to the highest length row
    '''
    max_len = max(len(row) for row in grid_view)
    return [row + ' ' * (max_len - len(row)) for row in grid_view]

def print_grid(maze, nodes, animate=False):
    '''
    This function prints the grid with node ditances, additionally,
    it can also check to see if you need to print the animation or not
    to ensure that it works for both instances.
    Arguments:
    maze: is a list of strings representing the grid layout
    nodes: is a 2d list of DijkstraNOde objects representing the current state of each cell
    whether reached or not reached
    animate: is a boolean indicating whether the grid should be printed in
    animation mode.

    Return Value: N/A
    '''


    # Iterate through each row of the maze
    for i, row in enumerate(maze):
        line = []  # To collect all cell strings for the current row

        # Iterate through each cell in the row
        for j, cell in enumerate(row):
            node = nodes[i][j]
            if cell == ' ':
                # Add spaces for empty cells
                line.append(f"{' ' * 3}")
            elif node.is_done():
                # Add distances aligned to the right with fixed width
                if node.get_dist() >=10:
                    line.append(str(node.get_dist()) + ' ')
                else:
                    line.append(str(node.get_dist()) + '  ')
            elif node.is_reached() and animate:
                # Add distances with a question mark for ongoing cells
                if node.get_dist() >=10:
                    line.append(str(node.get_dist()) + '?')
                else:
                    line.append(str(node.get_dist()) + '? ')
            elif cell == '#':
                # Add '#' with fixed width
                line.append("#  ")
            else:
                # Add other characters with fixed width
                line.append(f"{cell * 3}")

        # Join the row into a single string and print it
        if len(maze) == 1:
            print("".join(line))
        else:   
            print(" "+"".join(line))

    print()


def dijkstra_algorithm(maze, start_x, start_y, command):
    '''
    This function implements the Dijkstra's algorithm to find the shortest path
    in a grid. Additionally, you can either fill or animate the distances
    Arguments:
    maze: is a list of strings representing the grid layout
    start_x: is the staring x-coordinate value
    start_y: is the starting y-coordinate value
    command: is the command on which the funciton will either fill or animate
    Return Valu: N/A
    '''
    rows, cols = len(maze), len(maze[0])
    nodes = [[DijkstraNode() for _ in range(cols)] for _ in range(rows)]

    # Priority queue (min-heap) using a list
    todo_list = []
    todo_list.append((0, start_x, start_y))
    nodes[start_x][start_y].update_dist(0)

    if command == "animate":
        print(f"Searching from ({start_y}, {start_x}) outward.\n")
        print("STARTING GRID:")
        print_grid(maze, nodes)
        time.sleep(1)  # Sleep to let the user see the starting grid

        # Print the grid with the starting distance cell
        print("CURRENT GRID:")
        print_grid(maze, nodes, animate=True)
        print("TODO list:", todo_list)
        time.sleep(1)  # Sleep to let the user see the distance 0 cell

    # Directions for moving in 4-connected grid (up, down, left, right)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while todo_list:
        # Sort the list to get the smallest distance node
        todo_list.sort()
        dist, x, y = todo_list.pop(0)
        node = nodes[x][y]
        if node.is_done():
            continue
        node.set_done()

        # Iterate through each direction to explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '#':
                neighbor_node = nodes[nx][ny]
                new_dist = dist + 1
                if not neighbor_node.is_done() and (
                        not neighbor_node.is_reached() or new_dist < neighbor_node.get_dist()):
                    neighbor_node.update_dist(new_dist)
                    todo_list.append((new_dist, nx, ny))

        if command == "animate":
            print("\nCURRENT GRID:")
            print_grid(maze, nodes, animate=True)
            print("TODO list:",todo_list)
            time.sleep(0.5)  # Sleep for 0.5 seconds between each step

    if command == "fill":
        print_grid(maze, nodes)


def combine_and_print_flipped_tuples(todo_list):
    # Combine all tuples into a single list of elements
    combined_elements = []
    
    for tup in todo_list:
        # Append elements from each tuple, flipping the second and third elements
        combined_elements.append(tuple((tup[0], tup[2], tup[1])))

    # Convert the combined list into a single tuple
    
    # Print the combined tuple
    print("\nTODO list:", combined_elements)

def main():
    file_name = input("Please give the grid file: \n")
    contents = []
    try:
        with open(file_name, "r") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("ERROR: Could not open the grid file")
        return

    coordinate = input("Where to start?\n")
    start = coordinate.split()
    if len(start) == 2:
        try:
            x = int(start[1])
            y = int(start[0])
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return
    else:
        print("Invalid input. Please enter coordinates in the format x y.")
        return

    grid_view = [line.rstrip() for line in contents]  # Preserve trailing spaces and leading spaces
    grid_view = equalize_lengths(grid_view)

    operation = input("What type of operation?\n")

    if operation.lower() == 'fill':
        if grid_view[x][y] == '#':
            dijkstra_algorithm(grid_view, x, y, 'fill')
        else:
            print("The starting point must be a '#'.")
    elif operation.lower() == 'animate':
        if grid_view[x][y] == '#':
            dijkstra_algorithm(grid_view, x, y, 'animate')
            print("\n-------- All reachable spaces filled. This is the final map --------")
            dijkstra_algorithm(grid_view, x, y, 'fill')
        else:
            print("The starting point must be a '#'.")
    else:
        print("Invalid operation. Please choose 'fill' or 'animate'.")

if __name__ == "__main__":
    main()
