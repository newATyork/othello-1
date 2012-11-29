from Board import Board
import re
import pygame
import random
import sys
import time

def main():
    b = Board()
    game_over = False
    player_turn = "O"

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    
    mode_chosen = False
    splash_screen = pygame.image.load("panda.jpg")
    background = pygame.image.load("board.jpg")
    white_piece = pygame.image.load("white_piece.png")
    black_piece = pygame.image.load("black_piece.png")
    player_1 = pygame.image.load("1_player.png")
    player_2 = pygame.image.load("2_player.png")
    box = pygame.image.load("box.png")
    current_mode_selected = 1

    # choosing player mode menu
    while True:
        # exit on exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # get enter input
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            print("mode " + str(current_mode_selected) + " selected")
            time.sleep(.1)
            
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            current_mode_selected = 2
            time.sleep(.1)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            current_mode_selected = 1
            time.sleep(.1)

        screen.blit(background, (0, 0, 800, 600))
        # x_increase and y_increase used to determined location of pieces
        # dat guess n' check [b'-']b
        x_increase = 42
        y_increase = 41.5
        for x in range(8):
            for y in range(8):
                if (random.random() < .5):
                    screen.blit(black_piece, (245+x_increase*x, 160+y_increase*y, 40, 40))
                else:
                    screen.blit(white_piece, (245+x_increase*x, 160+y_increase*y, 40, 40))

        if (current_mode_selected == 1):
            screen.blit(box, (90, 5))
        else:
            screen.blit(box, (440, 5))

        screen.blit(player_1, (100, 10))
        screen.blit(player_2, (450, 10))
                
        pygame.display.flip()

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

