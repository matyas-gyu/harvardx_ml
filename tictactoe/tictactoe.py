"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]== X:
                countX += 1
            if board[row][col]==O:
                countO += 1
    
    if countX == countO:
        return X
    elif countX > countO:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possiblemoves = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]== EMPTY:
                possiblemoves.add((row,col))

    return possiblemoves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid")
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy    

def checkrow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkcol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def leftcheckdig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def rightcheckdig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkrow(board, X) or checkcol(board, X) or leftcheckdig(board, X) or rightcheckdig(board, X):
        return X
    elif checkrow(board, O) or checkcol(board, O) or leftcheckdig(board, O) or rightcheckdig(board, O):
        return O

    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]== EMPTY:
                return False
            
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maxval(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minval(result(board, action)))  
    return v
    
def minval(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxval(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    #Player is X
    elif player(board) ==X:
        plays = []
        #Loop over all, return the results and action tupple
        for action in actions(board):
            plays.append([minval(result(board, action)), action])
        #Sorts the list in descending order to choose max
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    #Player is O
    elif player(board) ==O:
        plays = []
        #Loop over all, return the results and action tupple
        for action in actions(board):
            plays.append([maxval(result(board, action)), action])
        #Sorts the list in ascending order to choose min
        return sorted(plays, key=lambda x: x[0])[0][1]


