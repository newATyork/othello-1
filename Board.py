""" Todo:
    - Create clearer exceptions
"""

class Board:
    """Class for othello board manipulations.

    Grid is stored in a 2-dimensional array.
    
    B represents blank
    O represents white
    X represents black

    The grid starts at 1 and goes to 8 rather
    than starting at 0 for convenience.

    """
    def __init__(self):
        self.grid = [
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
        ]

    def flip_piece(self, y, x):
        x -= 1
        y -= 1
        if (self.grid[x, y] == 'B'):
            raise Exception

    def insert_white(self, y, x):
        x -= 1
        y -= 1
        if (self.grid[x][y] != 'B'):
            raise Exception
        else:
            self.grid[x][y] = 'O'

    def insert_black(self, y, x):
        x -= 1
        y -= 1
        if (self.grid[x][y] != 'B'):
            raise Exception
        else:
            self.grid[x][y] = 'X'

    def display(self):
        for index, column in enumerate(self.grid):
            current_line = ""
            for cell in column:
                current_line += "["+cell+"] "
            print(current_line)
            if (index < 7):
                print("") # skip a lin e
