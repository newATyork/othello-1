from Board import Board
import re

def main():
    b = Board()
    game_over = False
    player_turn = "O"

    while not game_over:
        b.display()
        print("It is %s 's turn." % ("white" if player_turn=="O" else "black"))
        x,y = get_input()
        x = int(x)
        y = int(y)
        move_made = False

        if (b.make_move(player_turn, x, y)):
            if (player_turn == "O"):
                b.insert_white(x, y)
            else:
                b.insert_black(x, y)
            move_made = True
        else:
            print("Not a valid move. Try again.")

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

def get_input():
    choice = ""
    while not re.match("^[0-8],[0-8]$", choice):
        print("Give me your input in x,y format (e.g, 5,2): ")
        choice = input()
    x,y = choice.split(",")
    return x,y

if __name__ == '__main__':
    main()
