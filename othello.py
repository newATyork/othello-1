from Board import Board

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

        if (b.make_move(player_turn, x, y)):
            if (player_turn == "O"):
                b.insert_white(x, y)
            else:
                b.insert_black(x, y)
        else:
            print("Not valid move.")

        player_turn = "X" if player_turn != "X" else "O"

def get_input():
    print("Give me your input in x,y format (e.g, 5,2): ")
    x,y = input().split(",")
    return x,y

if __name__ == '__main__':
    main()
