""" Game Rules - Classic three-in-a-row game with two players. 
    Each player is assigned the character of X or O
"""
# Constants
logo = """  __  .__                   __                            __                 
_/  |_|__| ____           _/  |______    ____           _/  |_  ____   ____  
\   __\  |/ ___\   ______ \   __\__  \ _/ ___\   ______ \   __\/  _ \_/ __ \ 
 |  | |  \  \___  /_____/  |  |  / __ \\  \___  /_____/  |  | (  <_> )  ___/ 
 |__| |__|\___  >          |__| (____  /\___  >          |__|  \____/ \___  >
              \/                     \/     \/                            \/  """
base_board = [' ' for x in range(10)]
char= [' ','X', 'O']

# TODO 1 - Create and print the board
def board(base_board):
    print(' ' + base_board[1] + ' | ' +
          base_board[2] + ' | ' + base_board[3])
    print('-----------')
    print(' ' + base_board[4] + ' | ' +
          base_board[5] + ' | ' + base_board[6])
    print('-----------')
    print(' ' + base_board[7] + ' | ' +
          base_board[8] + ' | ' + base_board[9])

# TODO 2 - Winning row function
# Board winning combinations
def winning_row(base_board, player_char):
    return (base_board[1] == player_char and base_board[2] == player_char and base_board[3] == player_char) or \
        (base_board[4] == player_char and base_board[5] == player_char and base_board[6] == player_char) or \
        (base_board[7] == player_char and base_board[8] == player_char and base_board[9] == player_char) or \
        (base_board[1] == player_char and base_board[4] == player_char and base_board[7] == player_char) or \
        (base_board[2] == player_char and base_board[5] == player_char and base_board[8] == player_char) or \
        (base_board[3] == player_char and base_board[6] == player_char and base_board[9] == player_char) or \
        (base_board[1] == player_char and base_board[5] == player_char and base_board[9] == player_char) or \
        (base_board[3] == player_char and base_board[5]
         == player_char and base_board[7] == player_char)

# TODO 3 - Player input, check occupied spaces and append an 'X' or 'O' to the board, based on location
def player_play(player):
    play = True
    if player == 1:
        player = char[player]
    else:
        player = char[player]
    while play:
        turn = input('Where would you like to move? (1-9): ')
        try:
            turn = int(turn)
            if 0 < turn < 10:
                if base_board[turn] == ' ':
                    base_board[turn] = (player)
                    play = False
                    return board(base_board)
                else:
                    print('This space is already occupied. Try again!')
            else:
                print('Please use a number from 1-9!')
        except:
            print('Please use a number in the range 1-9!')

# TODO 4 - Full board check function
def full_board(base_board):
    if base_board.count(' ') > 1:
        return False
    else:
        print('It\'s a Tie!')
        return True

# TODO 5 - Game initialisation. 
def game():
    print("\n \n \n \n")
    print(logo)
    print('Welcome to Tic-Tac-Toe, the classic three-in-a-row strategy game.')
    print(board(base_board))
    num = 0
    while not(full_board(base_board)):
        if num == 2:
            return full_board(base_board) == True
        if num == 0:
            num += 1
            print(f'It\'s Player {num}\'s turn.')
            player_play(num)
            if not winning_row(base_board, char[num]):
                continue
            else:
                print(f'Congratulations, Player {num} has won!')
                break
        elif num == 1:
            num += 1
            print(f'It\'s Player {num}\'s turn.')
            player_play(num)
            if not winning_row(base_board, char[num]):
                num -= 2
                continue
            else:
                print(f'Congratulations, Player {num} has won!')
                break
        else:
            break

# TODO 6 - Game while loop.
game()
while True:
    play_again = input('Would you like to play again? (Y/N): ')
    if play_again.upper() == 'Y':
        print('\n New Game Loading... \n')
        base_board = [' ' for x in range(10)]
        game()
    else:
        break
    
