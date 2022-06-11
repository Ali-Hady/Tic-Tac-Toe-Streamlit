import random
import numpy as np

def create_board():
    return np.zeros((3, 3))

board = create_board()

def place(board, player, position):
    if board[position] == 0:
        board[position] = player

place(board, 1, (0,0))

def possibilities(board):
    return list(zip(*np.where(board == 0)))

possibilities(board)

def random_place(board, player):
    options = possibilities(board)
    if options == []:
        return None
    placement = random.choice(options)
    place(board, player, placement)
    
random_place(board, 2)

def row_win(board, player):
    row_match = np.all(board==player, axis=0)
    return np.any(row_match)

def col_win(board, player):
    col_match = np.all(board==player, axis=1)
    return np.any(col_match)

def diag_win(board, player):
    diag1 = board.diagonal()
    diag1_check = np.all(diag1==player)
    diag2 = board[::-1].diagonal()
    diag2_check = np.all(diag2==player)
    return diag1_check or diag2_check

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


random.seed(1)
 
def play_game():
    board = create_board()
    res = -1
    
    while True:
        if evaluate(board) == -1: break
        for player in [1, 2]:
            if evaluate(board) == -1: break
            random_place(board, player)
        
        res = evaluate(board)
        
    return res