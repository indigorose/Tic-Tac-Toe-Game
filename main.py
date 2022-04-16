""" Game Rules - Classic three-in-a-row game with two players. 
    Each player is assigned the character of X or O
"""

# TODO 1 - Create the board and print the board
base_board = [" " for x in range(10)]


def board(base_board):

    print(' ' + base_board[1] + ' | ' +
          base_board[2] + " |" + base_board[3])
    print("-----------")
    print(' ' + base_board[4] + " | " +
          base_board[5] + " |" + base_board[6])
    print("-----------")
    print(' ' + base_board[7] + " | " +
          base_board[8] + " | " + base_board[9])


board(base_board)

# TODO 2 - Append an "X" or "O" to the board, based on location

# TODO 3 - Game functionality, ask for player input.

# TODO 4 - Check board for characters, remaining space, who has won?

# TODO 5 - Game while loop.
