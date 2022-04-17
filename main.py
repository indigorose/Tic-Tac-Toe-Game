""" Game Rules - Classic three-in-a-row game with two players. 
    Each player is assigned the character of X or O
"""

# TODO 1 - Create the board and print the board
base_board = [" " for x in range(10)]
player_1_char = "X"
player_2_char = "O"

def board(base_board):

    print(' ' + base_board[1] + ' | ' +
          base_board[2] + ' | ' + base_board[3])
    print('-----------')
    print(' ' + base_board[4] + ' | ' +
          base_board[5] + ' | ' + base_board[6])
    print('-----------')
    print(' ' + base_board[7] + ' | ' +
          base_board[8] + ' | ' + base_board[9])

board(base_board)

# TODO 2 - Append an "X" or "O" to the board, based on location
def player_play(position, player):
    if check_space(position):
        return player_turn()
    if player == 1:
        base_board[position] = player_1_char
    else:
        base_board[position] = player_2_char
    return board(base_board)

player_play(3,1)

# TODO 3 - Occupied space check
def check_space(position):
    if base_board[position] == "X" or "O":
        return "Player has already played here"

# TODO 4 - Player input
def player_turn():
    pass

# Board winning combinations
def winning_row(player_char):
    return (base_board[1] == player_char and base_board[2] == player_char and base_board[3] == player_char) or \
    (base_board[4] == player_char and base_board[5] == player_char and base_board[6] == player_char) or \
    (base_board[7] == player_char and base_board[8] == player_char and base_board[9] == player_char) or \
    (base_board[1] == player_char and base_board[4] == player_char and base_board[7] == player_char) or \
    (base_board[2] == player_char and base_board[5] == player_char and base_board[8] == player_char) or \
    (base_board[3] == player_char and base_board[6] == player_char and base_board[9] == player_char) or \
    (base_board[1] == player_char and base_board[5] == player_char and base_board[9] == player_char) or \
    (base_board[3] == player_char and base_board[5] == player_char and base_board[7] == player_char)
    
# TODO 5 - Game while loop.
game_on = True

def game():
    """Load the welcome ascii, welcome message and board.
        Ask player 1 for their first move. 
        Check the board and add position if position is clear. 
        Ask player 2 for their move, check the board and add position if clear. 
        Load the updated board and repeat the playing loop. 
        Break the loop if the following positions are full with the same character.
    """
    pass
