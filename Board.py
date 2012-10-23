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
            ['B','B','B','O','X','B','B','B',],
            ['B','B','B','X','O','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
            ['B','B','B','B','B','B','B','B',],
        ]

    def flip_piece(self, y, x):
        visual_x = y
        visual_y = x
        x -= 1
        y -= 1
        if (self.grid[x][y] == 'X'):
            self.grid[x][y] = 'O'
        elif (self.grid[x][y] == 'O'):
            self.grid[x][y] = 'X'
        elif (self.grid[x][y] == 'B'):
            raise Exception("Trying to flip empty piece (%d, %d)." % (visual_x, visual_y))

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

    def get_piece(self, y, x):
        x -= 1
        y -= 1
        return self.grid[x][y]

    def display(self):
        print("    [1] [2] [3] [4] [5] [6] [7] [8]\n")
        for index, column in enumerate(self.grid):
            current_line = "[%s] " % str(index+1)
            for cell in column:
                current_line += "["+cell+"] "
            print(current_line)
            if (index < 7):
                print("") # skip a lin e

    def make_move(self, player, x, y):
        """ Alters the board if move is valid.
        
        Returns true if the player is allowed to make move, returns
        false otherwise.

        e.g, if make_move("O", 3, 2):
            # continue game

        """
        # find adjacent pieces of opposite color
        adjacent_pieces = []
        valid_move = False

        for i in range(-1,2):
            for j in range(-1,2):
                if (i == 0 and j == 0):
                    pass # don't check the piece itself
                if x+i < 9 and y+j < 9 and x+i > 0 and y+i > 0:
                    piece = self.get_piece(x+i, y+j)
                    if piece != player and piece != "B":
                        c_x = x+i
                        c_y = y+j
                        while c_x < 9 and c_y < 9 and c_x > 0 and c_y > 0:
                            if (self.get_piece(c_x, c_y) == player):
                                valid_move = True
                                f_x = c_x + i
                                f_y = c_y + j
                                while self.get_piece(f_x, f_y) != player:
                                    print("flipping %d, %d" % (f_x, f_y))
                                    self.flip_piece(f_x, f_y)
                                    f_x += i
                                    f_y += j
                            c_x += i
                            c_y += j

        return valid_move
