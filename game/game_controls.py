from pygame import Surface
from gui.gui_utils import end_message

def get_winner(board: list[list[int]]):
    # Diagonals
    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) \
            or (board[0][2] == board[1][1] and board[1][1] == board[2][0])) and board[1][1] is not None:
        return board[1][1]
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Columns
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    return None

def check_win(board: list[list[int]], window: Surface):
    winner = get_winner(board)
    if winner != None:
        end_message(window, f"Game finished. {'X' if winner==-1 else 'O'} wins!!")
        return True
    return False

def select(row: int, col: int, board: list[list[int]], turn: int, window: Surface):
    if board[row][col] == None:
        board[row][col] = turn
        return True, check_win(board, window)
    return False, False
