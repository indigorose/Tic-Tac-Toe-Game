""" Game Rules - Classic three-in-a-row game with two players. 
    Each player is assigned the character of X or O
"""
logo = """  __  .__                   __                            __                 
_/  |_|__| ____           _/  |______    ____           _/  |_  ____   ____  
\   __\  |/ ___\   ______ \   __\__  \ _/ ___\   ______ \   __\/  _ \_/ __ \ 
 |  | |  \  \___  /_____/  |  |  / __ \\  \___  /_____/  |  | (  <_> )  ___/ 
 |__| |__|\___  >          |__| (____  /\___  >          |__|  \____/ \___  >
              \/                     \/     \/                            \/  """


# TODO 1 - Create the board and print the board
base_board = [' ' for x in range(10)]
char= ['X', 'O']

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
def player_play(player):
    play = True
    if player == 1:
        player = char[0]
    else:
        player = char[1]
    while play:
        turn = input('Where would you like to move? (1-9): ')
        try:
            turn = int(turn)
            if 0 < turn < 10:
                if base_board[turn] == ' ':
                    play = False
                    base_board[turn] = (player, turn)
                else:
                    print('This space is already occupied. Try again!')
            else:
                print('Please use a number from 1 -9!')
        except:
            print('Please type a number!')

player_play(3,1)

# TODO 3 - Occupied space check
def check_space(position):
    if base_board[position] == "X" or "O":
        return "Player has already played here"

# TODO 4 - Player input
def player_turn():
    pass

# Board winning combinations
def winning_row(base_board, player_char):
    return (base_board[1] == player_char and base_board[2] == player_char and base_board[3] == player_char) or \
    (base_board[4] == player_char and base_board[5] == player_char and base_board[6] == player_char) or \
    (base_board[7] == player_char and base_board[8] == player_char and base_board[9] == player_char) or \
    (base_board[1] == player_char and base_board[4] == player_char and base_board[7] == player_char) or \
    (base_board[2] == player_char and base_board[5] == player_char and base_board[8] == player_char) or \
    (base_board[3] == player_char and base_board[6] == player_char and base_board[9] == player_char) or \
    (base_board[1] == player_char and base_board[5] == player_char and base_board[9] == player_char) or \
    (base_board[3] == player_char and base_board[5] == player_char and base_board[7] == player_char)

def game():
    print(logo)
    print("Welcome to Tic-Tac_toe, the classic two-player game.")
    player = input('Are you player 1 or player 2? (1-2): ')
    player_play(player=int(player))

# TODO 5 - Game while loop.
game_on = True

while game_on:
    game()
    continue_game = input("Would you like to play? (Y/N): ")
    if continue_game.upper() is "Y":
        player_turn()
    else:
        game_on == False