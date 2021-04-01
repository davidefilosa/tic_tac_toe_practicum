# create an array that contains the board values
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

game_still_going = True

winner = None

current_player = 'X'

# function that dispay the board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] )
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] )
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] )


# function to get player input
def handle_turn(player):
    position = input("Player {} enter a position from 1 to 9: ".format(player))

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        position = input("Invalid input. Player {} enter again a position from 1 to 9: ".format(player))
  
    position = int(position) - 1

    while board[position] != '-':
        position = input("Position already taken. Player {} enter again a position from 1 to 9: ".format(player))
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invalid input. Player {} enter again a position from 1 to 9: ".format(player))
        position = int(position) - 1

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there is a winner
        winner = row_winner
    elif column_winner:
        # there is a winner
        winner = column_winner
    elif diagonal_winner:
        # there is a winner
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():

    global game_still_going
    
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_still_going = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_still_going = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

def check_diagonals():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'

    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    


def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = True
    return


def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return current_player


# function to start the game
def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        change_player()

    if winner == 'X' or winner == 'O':
        print('{} WON!'.format(winner))
    elif winner == None:
        print('It´s a tie!')


play_game()