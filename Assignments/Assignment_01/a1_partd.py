
from maze import Maze

def find_path(the_maze, from_cell, to_cell):
    visited = []  # Set to keep track of visited cells
    path = []  # List to store the path

    # Recursive helper function
    def find_path_recursive(current_cell):
        visited.append(current_cell)  # Mark the current cell as visited
        path.append(current_cell)  # Add the current cell to the path

        if current_cell == to_cell:
            # Base case: If starting cell/current cell is destination cell
            return True

        neighbors = []  # List to store the neighboring cells
        left_cell = the_maze.get_left(current_cell)
        if left_cell != -1 and left_cell not in visited: # If left_cell isn't a wall and has not been visited
            neighbors.append(left_cell)
        right_cell = the_maze.get_right(current_cell)
        if right_cell != -1 and right_cell not in visited:
            neighbors.append(right_cell)
        up_cell = the_maze.get_up(current_cell)
        if up_cell != -1 and up_cell not in visited:
            neighbors.append(up_cell)
        down_cell = the_maze.get_down(current_cell)
        if down_cell != -1 and down_cell not in visited:
            neighbors.append(down_cell)

        for neighbor in neighbors: # Call function for all neighbors
            if find_path_recursive(neighbor):
                return True

        path.pop()  # Remove the current cell from the path
        return False

    if find_path_recursive(from_cell):
        return path
    else:
        return []  # No path found