"""A script to play the reverse Tic-Tac-Toe game vs AI."""
import random
from typing import Tuple

import numpy as np

HUMAN_MARK = "o"
AI_MARK = "x"
EMPTY = " "


def display_board(board: np.ndarray):
    """Print the game board."""
    for i in range(10):
        print(" " + str(i), end="")
    print()
    for row_index, row in enumerate(board):
        for cell in row:
            print("|", end="")
            print(cell, end="")
        print("|" + str(row_index))
    print()


def get_human_choice(board: np.ndarray) -> Tuple[int, int]:
    """Get the human player's next move and check if it's valid."""
    valid_cell_chosen = False
    while not valid_cell_chosen:

        column_index = ask_for_coordinate("Column")
        row_index = ask_for_coordinate("Row")

        if is_free(board, row_index, column_index):
            valid_cell_chosen = True
        else:
            print("The cell is occupied. Please choose another.")

    return row_index, column_index


def ask_for_coordinate(coordinate_name: str) -> int:
    """Ask the human player to input a coordinate for the next move"""
    coordinate = None
    while coordinate not in [num for num in range(10)]:
        try:
            coordinate = int(input(f"{coordinate_name} (0-9)? "))
        except ValueError as exc:
            print(f"Wrong value: {exc}. Please, try again.")
    return coordinate


def is_free(board: np.ndarray, row_index, column_index) -> bool:
    """Return boolean value whether the cell is free or not."""
    return board[row_index][column_index] == EMPTY


def quit_if_finished(board: np.ndarray, mark: str):
    """Quit if the game is finished."""
    if check_win(board, mark):
        winner = "AI" if (mark == AI_MARK) else "human"
        print(f"The {winner} wins!")
        quit()

    if not has_free_space(board):
        print("The game ended in a draw.")
        quit()


def check_win(board: np.ndarray, mark: str) -> bool:
    """Return boolean value whether the player wins the game."""
    return (
        check_rows(board, mark)
        or check_columns(board, mark)
        or check_diagonals(board, mark)
    )


def check_rows(board: np.ndarray, mark: str) -> bool:
    """Check if there's a horizontal streak of 5 marks."""
    for row in board:
        last_cell = None
        streak_count = 0
        for cell in row:
            if cell == mark and cell == last_cell:
                streak_count += 1
            else:
                streak_count = 1
            if streak_count == 5:
                return True
            last_cell = cell
    return False


def check_columns(board: np.ndarray, mark: str) -> bool:
    """Check if there's a vertical streak of 5 marks."""
    rotated_by_90_board = np.rot90(board)
    return check_rows(rotated_by_90_board, mark)


def check_diagonals(board: np.ndarray, mark: str) -> bool:
    """Check if there's a diagonal streak of 5 marks."""
    diagonals = [
        board[::-1, :].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])
    ]
    diagonals.extend(
        board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1)
    )
    diagonals_board = np.array(diagonals, dtype=object)
    return check_rows(diagonals_board, mark)


def has_free_space(board: np.ndarray):
    """Return boolean value whether the game board is full of game marks."""
    return bool(np.count_nonzero(board == " "))


def place_mark(board: np.ndarray, mark: str, row_index, column_index):
    """Put a player mark to the specified cell."""
    board[row_index, column_index] = mark


def get_ai_choice(
    board: np.ndarray, point_of_interest_for_ai: Tuple[int, int]
) -> Tuple[int, int]:
    """Choose a move for the computer."""
    row_index, column_index = point_of_interest_for_ai
    step_away_distance = 0
    while True:
        step_away_distance += 1
        row_index += random.randint(-step_away_distance, step_away_distance)
        column_index += random.randint(-step_away_distance, step_away_distance)
        row_index = make_valid_coordinate(row_index)
        column_index = make_valid_coordinate(column_index)
        if is_free(board, row_index, column_index):
            return row_index, column_index


def make_valid_coordinate(coordinate: int) -> int:
    """Ensure that a cell coordinate is in 0-9 range."""
    if coordinate < 0:
        coordinate = 0
    elif coordinate > 9:
        coordinate = 9
    return coordinate


board = np.full((10, 10), EMPTY)
point_of_interest_for_ai = (5, 5)

while True:
    print("AI turn:")
    row_index, column_index = get_ai_choice(board, point_of_interest_for_ai)
    place_mark(board, AI_MARK, row_index, column_index)
    print(f"column {column_index}, row {row_index}")
    display_board(board)
    quit_if_finished(board, AI_MARK)

    print("Human turn:")
    row_index, column_index = get_human_choice(board)
    point_of_interest_for_ai = row_index, column_index
    place_mark(board, HUMAN_MARK, row_index, column_index)
    display_board(board)
    quit_if_finished(board, HUMAN_MARK)
