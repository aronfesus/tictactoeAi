"""
Tic Tac Toe Player
"""
import copy
from curses import flash
from lib2to3.pgen2.token import MINUS
import math
from tkinter.tix import MAX
import numpy as np

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
        for col in range(len(board[0])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1

    return X if countX == countO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibble_actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possibble_actions.add((row, col))

    print(possibble_actions)
    return possibble_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("action: ")
    print(action)
    if action not in actions(board):
        raise Exception("Invalid action")

    borad_copy = copy.deepcopy(board)
    borad_copy[action[0]][action[1]] = player(board)

    return borad_copy


def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)
    



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True
        
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    elif winner(board) == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == "X":
        return maxValue(board, Max, Min)[1]
    else:
        return minValue(board, Max, Min)[1]


def maxValue(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = minValue(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]


def minValue(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = maxValue(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]; 




    

