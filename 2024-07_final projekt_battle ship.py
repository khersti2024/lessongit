import pandas as pd
import numpy as np
import random
import time

#short introduction in the game
introduction_start = """
Welcome to Battleship!

In this classic strategy game, you will compete against the computer. Your objective is to sink the opponent's fleet before yours is located and destroyed. Here are the basics:
  - Game Board: Each player has their own board, which measures 10x10 squares.
  - Ships: Each player has a set of ships of varying sizes. Your task is to strategically place these ships on your board.
  - Gameplay: You and the computer take turns guessing the locations of each other’s ships. Enter the coordinates where you wish to strike. A hit will be marked, and you’ll get another turn. A miss will pass the turn to your opponent.
  - Game Objective: The first to sink all of the opponent’s ships wins the game.

Good luck, and may the best strategy win!
"""
print(introduction_start)

#creating the two boards
def init_pandas_board(size):
    return pd.DataFrame(np.full((size, size), '-'))

def init_empty_computerboard(size):
    return pd.DataFrame(np.full((size, size), '*'))

board_size = 10
player_board = init_pandas_board(board_size)
computer_board = init_pandas_board(board_size)
empty_computer_board = init_empty_computerboard(board_size)
print("Player's board:")
print(player_board)

# possible ships
ships = {
    "big ship": {"size": 5, "number": 1},
    "middle schip": {"size": 3, "number": 2},
    "small ship": {"size": 2, "number": 3}
}

# placing the ships for the player on the board
def input_coordinates():
    start_x = int(input("Give your start x value: "))
    start_y = int(input("give your start y value: "))
    end_x = int(input("give your end x value: "))
    end_y = int(input("give your end x value: "))
    return start_x, start_y, end_x, end_y

#check for the correct ship size
def check_ship_size(start_x, start_y, end_x, end_y, ship_size):
    ship_length_horizontal = abs(end_x - start_x) + 1
    ship_length_vertical = abs(end_y - start_y) + 1
    if ship_length_horizontal == ship_size or ship_length_vertical == ship_size:
        return True
    elif ship_length_vertical == ship_size or start_x == end_x:
        return True
    else:
        print("Incorrect entry, no valid ship size")
        return False

#correct place of the ship
def place_ship(board, start_x, start_y, end_x, end_y):
    if start_x == end_x:
        board.loc[start_x, min(start_y, end_y):max(start_y, end_y)] = 'X'
    elif start_y == end_y:
        board.loc[min(start_x, end_x):max(start_x, end_x), start_y] = 'X'

def player_place_ships(board, ships):
    for ships, details in ships.items():
        for _ in range(details["number"]):
            valid = False
            while not valid:
                print(f"place your ship {ships} (size {details['size']}):")
                start_x, start_y, end_x, end_y = input_coordinates()
                if start_x > 9 or start_x < 0:
                    print("Invalid input")
                    continue
                if start_y > 9 or start_y < 0:
                    print("Invalid start y coordinate!")
                    continue
                if end_x > 9 or end_x < 0:
                    print("Invalid start x coordinate")
                    continue
                if end_y > 9 or end_y < 0:
                    print("Invalid end y coordinate")
                    continue
                if check_ship_size(start_x, start_y, end_x, end_y, details["size"]):
                    place_ship(board, start_x, start_y, end_x, end_y)
                    valid = True
                else:
                    print("Invalid coordinates. Please try again.")
    print("Updated player board:")
    print(board)
    


player_place_ships(player_board, ships)

# check if there isn't sth on the board
def check_if_free(board, x, y):
    if board.iloc[x, y] == "-":
        return True
    else:
        print("The field ist already filled, please try again")
        return False

# Computer ships
def generierte_koordinaten(size, schiff_laenge):
    vertikal = random.choice([True, False])
    if vertikal:
        start_x = random.randint(0, size - schiff_laenge)
        start_y = random.randint(0, size - 1)
        end_x = start_x + schiff_laenge - 1
        end_y = start_y
    else:
        start_x = random.randint(0, size - 1)
        start_y = random.randint(0, size - schiff_laenge)
        end_x = start_x
        end_y = start_y + schiff_laenge - 1
    return start_x, start_y, end_x, end_y

def platziere_schiff(board, schiff_laenge):
    platziert = False
    while not platziert:
        start_x, start_y, end_x, end_y = generierte_koordinaten(board.shape[0], schiff_laenge)
        if start_x > 9 or start_x < 0:
            continue
        if start_y > 9 or start_y < 0:
            continue
        if end_x > 9 or end_x < 0:
            continue
        if end_y > 9 or end_y < 0:
            continue
        if start_x == end_x:
            if all(board.loc[start_x, min(start_y, end_y):max(start_y, end_y)] == '-'):
                board.loc[start_x, min(start_y, end_y):max(start_y, end_y)] = 'S'
                platziert = True
        elif start_y == end_y:
            if all(board.loc[min(start_x, end_x):max(start_x, end_x), start_y] == '-'):
                board.loc[min(start_x, end_x):max(start_x, end_x), start_y] = 'S'
                platziert = True

ship_sizes = [5, 3, 3, 2, 2, 2]  

for schiff_laenge in ship_sizes:
    platziere_schiff(computer_board, schiff_laenge)

# checks
def player_turn(board, empty_board):
    valid_shot = False
    while not valid_shot:
        x = int(input("Enter your x value: "))
        y = int(input("Enter your y value: "))
        if x > 9 or x < 0:
            continue
        if y > 9 or y < 0:
            continue
        time.sleep(1)
        if board.iloc[x, y] == 'S':
            board.iloc[x, y] = 'X'
            print("Hit!")
            empty_board.iloc[x,y] = 'X' 
            print(empty_board)
            valid_shot = True
        elif board.iloc[x, y] == '-':
            board.iloc[x, y] = 'O'
            print("Missed!")
            empty_board.iloc[x,y] = 'O' 
            print(empty_board)
            valid_shot = True
        else:
            print("Already shot, try again.")

def computer_turn(board):
    valid_shot = False
    while not valid_shot:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
        if board.iloc[x, y] in ['-', 'S']:
            if board.iloc[x, y] == 'S':
                board.iloc[x, y] = 'X'
                print("Computer has hit!")
            else:
                board.iloc[x, y] = 'O'
                print("Computer has missed!")
            valid_shot = True


def check_c_win(player_board):
    return not player_board.isin(['X']).any().any()

def check_p_win(computer_board):
    return not computer_board.isin(['S']).any().any()

game_over = False
while not game_over:
    print("Player's turn.")
    player_turn(computer_board, empty_computer_board)
    if check_p_win(computer_board):
        print("Congrats, you have won!")
        game_over = True
        break
    
    print("updated player board:")
    print(player_board)
    
    print("computer's turn.")
    time.sleep(1)
    computer_turn(player_board)
    if check_c_win(player_board):
        print("computer has won")
        game_over = True
