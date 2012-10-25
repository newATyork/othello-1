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
            ['_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_',],
            ['_','_','_','O','X','_','_','_',],
            ['_','_','_','X','O','_','_','_',],
            ['_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_',],
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
        elif (self.grid[x][y] == '_'):
            raise Exception("Trying to flip empty piece (%d, %d)." % (visual_x, visual_y))

    def insert_white(self, y, x):
        x -= 1
        y -= 1
        if (self.grid[x][y] != '_'):
            raise Exception
        else:
            self.grid[x][y] = 'O'

    def insert_black(self, y, x):
        x -= 1
        y -= 1
        if (self.grid[x][y] != '_'):
            raise Exception
        else:
            self.grid[x][y] = 'X'

    def get_piece(self, y, x):
        """ Returns the piece at the given location. Provide x,y """
        x -= 1
        y -= 1
        return self.grid[x][y]

    def display(self):
        """ Displays the board state as ASCII """
        print("    [1] [2] [3] [4] [5] [6] [7] [8]\n")
        for index, column in enumerate(self.grid):
            current_line = "[%s] " % str(index+1)
            for cell in column:
                current_line += "["+cell+"] "
            print(current_line)
            if (index < 7):
                print("") # skip a line

    def make_move(self, player, x, y):
        """ Alters the board if move is valid.
        
        Returns true if the player is allowed to make move, returns
        false otherwise.

        e.g, if make_move("O", 3, 2):
            # continue game

        """
        valid_move = False

        if (self.get_piece(x, y) != "_"):
            return False

        # get the combinations of directions (-1,-1), (-1,0), etc as i,j.
        for i in range(-1,2):
            for j in range(-1,2):
                if (i == 0 and j == 0):
                    pass # don't check the piece itself
                if x+i < 9 and y+j < 9 and x+i > 0 and y+i > 0:
                    # make sure we're not looking at a border
                    piece = self.get_piece(x+i, y+j)
                    if piece != player and piece != "_":
                        # if the adjacaent piece is an opponent piece
                        c_x = x + i
                        c_y = y + j
                        while c_x < 9 and c_y < 9 and c_x > 0 and c_y > 0:
                            # check each direction using i,j from 
                            # origin x,y until you reach a border
                            if (self.get_piece(c_x, c_y) == player):
                                # the move was valid, now we flip pieces
                                valid_move = True
                                # f_x and f_y is for tracking which piece to flip
                                f_x, f_y = c_x - i, c_y - j
                                opposite_player = 'X' if player=='O' else 'O'
                                while self.get_piece(f_x, f_y) == opposite_player:
                                    print("flipping %d, %d" % (f_x, f_y))
                                    self.flip_piece(f_x, f_y)
                                    f_x -= i
                                    f_y -= j
                            c_x += i
                            c_y += j

        return valid_move

    def move_is_valid(self, player, x, y):
        """ Returns True if move is valid. 
        
        This function is mostly ripped from make_move() and could
        be rewritten for efficiency.
        
        """
        if (self.get_piece(x, y) != "_"):
            return False
        
        # get the combinations of directions (-1,-1), (-1,0), etc as i,j.
        for i in range(-1,2):
            for j in range(-1,2):
                if (i == 0 and j == 0):
                    pass # don't check the piece itself
                if x+i < 9 and y+j < 9 and x+i > 0 and y+i > 0:
                    # make sure we're not looking at a border
                    piece = self.get_piece(x+i, y+j)
                    if piece != player and piece != "_":
                        # if the adjacaent piece is an opponent piece
                        c_x = x + i
                        c_y = y + j
                        while c_x < 9 and c_y < 9 and c_x > 0 and c_y > 0:
                            # check each direction using i,j from 
                            # origin x,y until you reach a border
                            if (self.get_piece(c_x, c_y) == player):
                                # the move was valid, now we flip pieces
                                return True
                            c_x += i
                            c_y += j

        return False

    def has_valid_move(self, player):
        for x in range(1,9):
            for y in range(1,9):
                if self.move_is_valid(player, x, y):
                    return True
        return False
