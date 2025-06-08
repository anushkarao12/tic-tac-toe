"""
Tic Tac Toe Player
"""

import math

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
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    str: The player who has the next turn (X or O).
    """
    # Count the number of moves made so far
    moves_made = sum([cell != EMPTY for row in board for cell in row])
    
    # If the number of moves is even, it's X's turn
    if moves_made % 2 == 0:
        return X
    # Otherwise, it's O's turn
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    set: A set of tuples (i, j) representing possible actions.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    action (tuple): A tuple (i, j) representing the move.
    
    Returns:
    list: A 2D list representing the resulting board.
    """
    i, j = action
    current_player = player(board)
    new_board = [row[:] for row in board]
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    str: The winner of the game (X or O), or None if no winner.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    bool: True if the game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    int: The utility of the board (1 if X wins, -1 if O wins, 0 otherwise).
    """
    winner_of_game = winner(board)
    if winner_of_game == X:
        return 1
    elif winner_of_game == O:
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    tuple: The optimal action (i, j) for the current player.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    best_action = None
    best_score = -float('inf') if current_player == X else float('inf')
    
    for action in actions(board):
        new_board = result(board, action)
        score = minimax_score(new_board, current_player)
        
        if current_player == X and score > best_score:
            best_score = score
            best_action = action
        elif current_player == O and score < best_score:
            best_score = score
            best_action = action
    
    return best_action

def minimax_score(board, player):
    """
    Returns the Minimax score for the given board and player.
    
    Args:
    board (list): A 2D list representing the Tic Tac Toe board.
    player (str): The player for whom to calculate the score (X or O).
    
    Returns:
    int: The Minimax score for the given board and player.
    """
    if terminal(board):
        return utility(board)
    
    if player == X:
        best_score = -float('inf')
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board, O)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board, X)
            best_score = min(best_score, score)
        return best_score
