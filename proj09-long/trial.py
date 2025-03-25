import heapq
import time


class DijkstraNode:
    """Models a single node in a graph, running Dijkstra's algorithm."""

    def __init__(self):
        self._dist = None  # not reached yet, treat as infinite distance
        self._done = False

    def is_done(self):
        return self._done

    def is_reached(self):
        return self._dist is not None

    def get_dist(self):
        assert self._dist is not None
        return self._dist

    def update_dist(self, new_dist):
        assert new_dist >= 0
        assert not self._done
        assert self._dist is None or new_dist < self._dist
        self._dist = new_dist

    def set_done(self):
        assert not self._done
        self._done = True


def read_map(file_name):
    """Reads the map from the given file and returns it as a 2D list."""
    with open(file_name, 'r') as f:
        grid = [list(line.rstrip()) for line in f]
    return grid


def print_map(grid, nodes, pending=None):
    """Prints the map with distances filled in or with animation status."""
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        line = []
        for c in range(cols):
            if grid[r][c] == '#':
                node = nodes[r][c]
                if pending and (r, c) in pending:
                    line.append(f"{node.get_dist():>2}?")
                elif node.is_reached():
                    line.append(f"{node.get_dist():>3}")
                else:
                    line.append('###')
            else:
                line.append('   ')
        print(''.join(line))
    print()  # Extra newline for spacing


def dijkstra_algorithm(grid, start, command):
    """Runs Dijkstra's algorithm on the grid and handles both 'fill' and 'animate' commands."""
    rows, cols = len(grid), len(grid[0])
    nodes = [[DijkstraNode() if grid[r][c] == '#' else None for c in range(cols)] for r in range(rows)]

    start_x, start_y = start
    nodes[start_x][start_y].update_dist(0)

    # Min-heap for the TODO list
    todo = [(0, start_x, start_y)]
    heapq.heapify(todo)

    while todo:
        # Get the next node to process
        dist, x, y = heapq.heappop(todo)
        current_node = nodes[x][y]

        if current_node.is_done():
            continue

        # Mark the node as done
        current_node.set_done()

        # If animating, print the current state of the grid and the TODO list
        if command == 'animate':
            print("CURRENT GRID:")
            print_map(grid, nodes, pending={(nx, ny) for _, nx, ny in todo})
            print(f"TODO list: {todo}\n")
            time.sleep(0.5)  # Pause for 0.5 seconds to animate

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '#':
                neighbor_node = nodes[nx][ny]
                new_dist = dist + 1
                if not neighbor_node.is_done() and (
                        not neighbor_node.is_reached() or new_dist < neighbor_node.get_dist()):
                    neighbor_node.update_dist(new_dist)
                    heapq.heappush(todo, (new_dist, nx, ny))

    # Print the final filled map if the command is "fill"
    if command == 'fill':
        print_map(grid, nodes)


def main():
    # Example usage:
    map_file = input("Enter the map file name: ")
    start_x = int(input("Enter the start x-coordinate: "))
    start_y = int(input("Enter the start y-coordinate: "))
    command = input("Enter the command ('animate' or 'fill'): ")

    grid = read_map(map_file)
    dijkstra_algorithm(grid, (start_x, start_y), command)


if __name__ == "__main__":
    main()
