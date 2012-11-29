from Board import Board
import re
import pygame

def main():
    b = Board()
    game_over = False
    player_turn = "O"

    pygame.init()
    pygame.display.set_mode((800,600))

"""
        if move_made: # in case of invalid move
            player_turn = "X" if player_turn != "X" else "O"
            if player_turn == "X":
                if not b.has_valid_move("X"):
                    if not b.has_valid_move("O"):
                        game_over = True
                    else:
                        print("Black has no more moves.")
            if player_turn == "O":
                if not b.has_valid_move("O"):
                    if not b.has_valid_move("X"):
                        game_over = True
                    else:
                        print("White has no more moves.")
"""

def get_input():
    choice = ""
    while not re.match("^[0-8],[0-8]$", choice):
        print("Give me your input in x,y format (e.g, 5,2): ")
        choice = raw_input()
    x,y = choice.split(",")
    return x,y

if __name__ == '__main__':
    main()
