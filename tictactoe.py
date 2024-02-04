"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
def print_board(board):
    for row in board:
        for cell in row:
            print(cell,end = ' ')
        print()

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    The player function should take a board state as input, and return which player’s turn it is (either X or O).

    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

    """
    count_X = 0
    count_O = 0
    for row in board:
        for piece in row:
            if piece == X:
                count_X += 1
            elif piece == O:
                count_O += 1
    if count_O == count_X:
        return X
    return O 
    


def actions(board):
    """
    The actions function should return a set of all of the possible actions that can be taken on a given board.

    Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    Possible moves are any cells on the board that do not already have an X or an O in them.
    Any return value is acceptable if a terminal board is provided as input.

    """
    actions = []
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                actions.append((row,cell))
    return actions

                



def result(board, action):
    """
    The result function takes a board and an action as input, and should return a new board state, without modifying the original 
    board.

    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, and letting the player 
    whose turn it is make their move at the cell indicated by the input action.

    Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different 
    board states during its computation. This means that simply updating a cell in board itself is not a correct implementation 
    of the result function. You’ll likely want to make a deep copy of the board first before making any changes.

    """
    board_copy = deepcopy(board)
    row  = action[0]
    cell = action[1]

    if board_copy[row][cell] == EMPTY:
        if player(board_copy) == X:
            board_copy[row][cell] = X
        else: 
            board_copy[row][cell] = O
    else:
        raise Exception("Invalid data")
    return board_copy


def winner(board):
    """
    The winner function should accept a board as input, and return the winner of the board if there is one.

    If the X player has won the game, your function should return X. If the O player has won the game, your function should 
    return O.
   
    One can win the game with three of their moves in a row horizontally, vertically, or diagonally.

    You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, 
    since that would be an invalid board state).
    If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should
    return None.


    """
    #Check if X won
    def rows(icon):
        for row in board:
            if row.count(icon) == 3:
                return icon
        return None
    def cols(icon):
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == icon:
                return icon
        return None
    
    def diagonal_1(icon):
        if board[0][0] == board[1][1] == board[2][2] == icon:
            return icon
        return None
    
    def diagonal_2(icon):
        if board[0][2] == board[1][1] == board[2][0] == icon:
            return icon
        return None
    if rows(X) or cols(X) or diagonal_1(X) or diagonal_2(X):
        return X
    elif rows(O) or cols(O) or diagonal_1(O) or diagonal_2(O):
        return O
    return None


def terminal(board):
    """
    The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.

    If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, 
    the function should return True.
    
    Otherwise, the function should return False if the game is still in progress.


    """
    #check if there are any empty spots
    def empty_spots(board):
        for row in board:
            for cell in row:
              
                if cell == None:
                    return False
        return True
    
    return (empty_spots(board) or winner(board) != None)
        
            

def utility(board):
    """
    The utility function should accept a terminal board as input and output the utility of the board.

    If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, 
    the utility is 0.
    You may assume utility will only be called on a board if terminal(board) is True.

    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def minimax(board):
    """
    the minimax function should take a board as input, and return the optimal move for the player to move on that board.

    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.

    """  
    # alpha = -math.inf 
    # beta = math.inf
    def max_value(board,depth ,alpha = -math.inf, beta = math.inf):
        value = -math.inf
        if terminal(board) or depth == 0:
            return utility(board), None
        
        for action in actions(board):
            new_value, _ = min_value(result(board, action),depth -1,alpha,beta)
            if new_value > value:
                print(depth)
                value = new_value
                best_action = action
            alpha = max(alpha,value)
            if beta <= alpha:
                break
        return value, best_action
    
    def min_value(board,depth ,alpha = -math.inf, beta = math.inf):
        value = math.inf
        if terminal(board) or depth == 0:
            return utility(board), None
        for action in actions(board):
            new_value, _ = max_value(result(board, action),depth - 1,alpha,beta)
            if new_value < value:
                value = new_value
                best_action = action
            beta = min(beta,value)
            if beta <= alpha:
                break
        return value,best_action
    
    if player(board) == X:
        return max_value(board,8)[1]
    else:
        return min_value(board,8)[1]



print(len(actions(initial_state())))