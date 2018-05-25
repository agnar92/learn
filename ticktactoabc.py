import random
board = [' ']*10
game_state = True
announce = ''

def display_board():

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    """
    OUPUT: = (Player 1 marker, Player 2 marker)
    :return:
    """

    marker = ''

    while marker != 'X' and marker != '0':
        marker = input('Player: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, possition):

    board[possition] = marker

def win_check(board, mark):
    return False


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    print(board[position] == ' ')
    return board[position] == ' '

def full_board_check(board):

    if '' in board[1:]:
        return False
    else:
        return True

def ask_player(mark):
    global board

    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9")
            continue

        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print("That sapce isn't empty")
            continue

def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True

def player_choise(mark):
    global board, game_state, announce
    announce = ''
    mark = str(mark)
    ask_player(mark)

    if win_check(board, mark):
        display_board()
        announce = mark + 'Wins'
        game_state = False

    display_board()

    if full_board_check(board):
        announce = 'Tie'
        game_state = False

    return game_state, announce

def play_game():
    reset_board()
    global announce

    X='X'
    O='O'

    while True:
        display_board()

        game_state, announce = player_choise(X)
        print(announce)
        if game_state == False:
            break

        game_state, announce = player_choise(O)
        print(announce)
        if game_state == False:
            break

        rematch = input('Would like to play again? y/n')
        if rematch == 'y':
            play_game()
        else:
            print("Thanks for playing")



def replay():

    choise = input("Play again? Enter Yes or No")
    return choise == 'Yes'


def main():
    print('Welcome to Tic Tac Toe')

    play_game()




if __name__ == '__main__':
    main()