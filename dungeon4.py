"""
This program allows the user to play a simple text-based adventure game.
In this game,the user will be able to move around the dungeon, display the map of the dungeon, be notified which directions they can and can't move and be notified once they reach they have reached the finish point.
"""

import sys
from copy import deepcopy
MAP_FILE = "C:\\Users\\abhir\\Downloads\\midgaard_map.txt"

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    # reads contents of text file
    with open(map_file, 'r') as file:
        alist = file.readlines() 
    grid = []
    index = 0
    # uses contents of a text file to return a nested list
    for row in alist:
        a_row = []
        item = alist[index].strip()
        for element in item:
            element.split()
            a_row.append(element)
        index += 1
        grid.append(a_row)
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    index = 0
    b_list = []
    # loop through every element in the grid
    for sub_list in grid:
        for element in sub_list:
            for letter in element:
                if letter == "S":
                    # append the coordinates of the start position to  b_list
                    b_list.append(index)
                    b_list.append(sub_list.index(element))
                else:
                    continue
        index += 1
    return b_list

def get_command() -> str:
    """
    Gets a command from the user.
    """
    command = input()
    return command  

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    new_grid = deepcopy(grid)
    emojis = [("-", "🧱"), ("S", "🏠"), ("F", "🏺"), ("*", "🟢"), ("@", "🧝")]
    new_grid[player_position[0]][player_position[1]] = "@"  # replace "S" with "@"
    for row in new_grid:
        a_row = ''
        for col in row:
                # loop through the list emojis to replace symbols with unicode characters
                for row in emojis: 
                        if col == row[0]:
                                col = row[1]                
                a_row += col
        print(a_row)  

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    size = []
    rows = len(grid)
    cols = len(grid[0])
    size.append(rows)
    size.append(cols)
    return size

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    if position[0] >= 0 and position[1] >= 0:
        if position[0] < grid_rows and position[1] < grid_cols:
            return True
        else:
            return False        
    else:
        return False
    

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:  # check if the position north of player's current position is inside the grid and if it is one of the allowed objects
        directions.append('north')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:  # check if the position south of player's current position is inside the grid and if it is one of the allowed objects
        directions.append('south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:  # check if the position west of player's current position is inside the grid and if it is one of the allowed objects
        directions.append('west')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:  # check if the position east of player's current position is inside the grid and if it is one of the allowed objects
        directions.append('east') 
    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    directions = look_around(grid, player_position)
    if direction in directions:
        if direction == "north":
            player_position[0] -= 1
        elif direction == "south":
            player_position[0] += 1 
        elif direction == "west":
            player_position[1] -= 1
        else:
            player_position[1] += 1  
        return True
    else:
        return False
    
def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    index = 0
    b_list = []
    # loop through grid to find coordinates of "F"
    for sub_list in grid:
        for element in sub_list:
            for letter in element:
                if letter == "F":
                    b_list.append(index)
                    b_list.append(sub_list.index(element))
                else:
                    continue
        index += 1
    # check if player has reached the finish point
    if player_position == b_list:
        return True
    else:
        return False

def display_help() -> None:
    """
    Displays a list of commands.
    """
    with open("C:\\Users\\abhir\\Downloads\\help.txt",'r') as file:
        lines = file.readlines()
        for line in lines:
            line.strip()
            print(line)


def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    start = find_start(grid)
    directions = look_around(grid,start)
    directions = ", ".join(directions)
    print(f"you can go {directions}.")
    command = get_command()
    while command != "escape":
        if command == "show map":
            display_map(grid, start)
            directions = look_around(grid,start)
            directions = ", ".join(directions)
            print(f"you can go {directions}.")  
        elif command == "help":
            display_help()
        elif command == "go north" or command == "go south" or command == "go west" or command == "go east":
            if move(command[3::], start, grid) == True:
                print(f"you moved {command[3::]}.")
                if check_finish(grid, start) == True:
                    print("Congratulations! You have reached the exit!")
                    sys.exit()
                directions = look_around(grid,start)
                directions = ", ".join(directions)
                print(f"you can go {directions}.")
            else:
                print("There is no way there.")
                directions = look_around(grid,start)
                directions = ", ".join(directions)
                print(f"you can go {directions}.")                
        else:
            print("I do not understand")
            directions = look_around(grid,start)
            directions = ", ".join(directions)
            print(f"you can go {directions}.")             
        command = get_command()
    else:
        sys.exit()
                 

if __name__ == '__main__':
    main()