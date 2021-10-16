import random

import numpy as np

HUMAN_MARK = "o"
AI_MARK = "x"
EMPTY = " "


def display_board(board):
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


def get_player_choice(board):
    """Get human player's next move and check if it's valid."""
    valid_position_chosen = False
    while not valid_position_chosen:

        column_index = ask_for_coordinate("Column")
        row_index = ask_for_coordinate("Row")

        if is_free(board, row_index, column_index):
            valid_position_chosen = True
        else:
            print("The cell is occupied. Please choose another.")

    return row_index, column_index


def ask_for_coordinate(coordinate: str):
    """Ask the human player to input a coordinate for the next move"""
    index = None
    while index not in [num for num in range(10)]:
        try:
            index = int(input(f"{coordinate} (0-9)? "))
        except ValueError as exc:
            print(f"Wrong value: {exc}. Please, try again.")
    return index


def is_free(board, row_index, column_index):
    """Return boolean value whether the cell is free or not."""
    return board[row_index][column_index] == EMPTY


def quit_if_finished(board, mark):
    """Quit if the game is finished."""
    if check_win(board, mark):
        winner = "AI" if (mark == AI_MARK) else "human"
        print(f"The {winner} wins!")
        quit()

    if not has_free_space(board):
        print("The game ended in a draw.")
        quit()


def check_win(board, mark):
    """Return boolean value whether the player wins the game."""
    return (
        check_rows(board, mark)
        or check_columns(board, mark)
        or check_diagonals(board, mark)
    )


def check_rows(board, mark):
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


def check_columns(board, mark):
    """Check if there's a vertical streak of 5 marks."""
    rotated_by_90_board = np.rot90(board)
    return check_rows(rotated_by_90_board, mark)


def check_diagonals(board, mark):
    """Check if there's a diagonal streak of 5 marks."""
    diagonals = [
        board[::-1, :].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])
    ]
    diagonals.extend(
        board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1)
    )
    diagonals_board = np.array(diagonals, dtype=object)
    return check_rows(diagonals_board, mark)


def has_free_space(board):
    """Return boolean value whether the game board is full of game marks."""
    return bool(np.count_nonzero(board == " "))


def place_marker(board, mark, row_index, column_index):
    """Put a player mark to appropriate position."""
    board[row_index, column_index] = mark


def make_ai_move():
    """Place a mark for the computer."""
    made_move = False
    while not made_move:
        row_index = random.randint(0, 9)
        column_index = random.randint(0, 9)
        if is_free(board, row_index, column_index):
            made_move = True
            place_marker(board, AI_MARK, row_index, column_index)


board = np.full((10, 10), EMPTY)

while True:
    print("AI turn:")
    make_ai_move()
    display_board(board)
    quit_if_finished(board, AI_MARK)

    print("Human turn:")
    row_index, column_index = get_player_choice(board)
    place_marker(board, HUMAN_MARK, row_index, column_index)
    display_board(board)
    quit_if_finished(board, HUMAN_MARK)
