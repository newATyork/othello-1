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
        print("    [1] [2] [3] [4] [5] [6] [7] [8]\n")
        for index, column in enumerate(self.grid):
            current_line = "[%s] " % str(index+1)
            for cell in column:
                current_line += "["+cell+"] "
            print(current_line)
            if (index < 7):
                print("") # skip a lin e

    def valid_move(self, player, x, y):
        """ Returns true if the player is allowed to make move

        e.g, if valid_move("O", 3, 2):
            do_move

        """
        return True
