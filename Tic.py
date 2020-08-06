from IPython.display import clear_output

def display_board(board):
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |   ')

def player_input():
    while(1):
        n = input("Enter the marker player 1 wants to choose (X or O): ")
        if n in ['X','O']:
            break
    if n == 'X':
        return ['X','O']
    else:
        return ['O','X'] 

def place_marker(board, marker, position):
    while(position in range(1,10)):
        if board[position] == ' ':
            board[position] = marker
            return board
        else:
            print('Wrong position. Enter position again: ')
            position = int(input())

def win_check(board, mark):
    if board[1] == mark:
        if board[2] == board[3] == mark:
            return True
        elif board[4] == board[7] == mark:
            return True
        elif board[5] == board[9] == mark:
            return True
    elif board[7] == mark:
        if board[8] == board[9] == mark:
            return True
        elif board[5] == board[3] == mark:
            return True
    elif board[5] == mark:
        if board[8] == board[2] == mark:
            return True
        elif board[4] == board[6] == mark:
            return True
    elif board[9] == board[6] == board[3] == mark:
        return True

def replay():
    while(1):
        n = input('Do players want to play the game? (Yes or No)')
        if n in ['Yes' , 'No']:
            return n == 'Yes'

print('Welcome to Tic Tac Toe!')

while replay():
    clear_output()
    mark = player_input()
    test_board = [' ']*10

    while True:
        while True:
            pos = int(input('Enter the position player 1 want to place the mark: '))
            if pos in  range(1,10):
                break
        test_board = place_marker(test_board, mark[0],pos)
        clear_output()
        display_board(test_board)
        if win_check(test_board , mark[0]):
            print('Player 1 has won the game. Congrats.')
            break
        if ' ' not in test_board[1:]:
            print('Game Over')
            break
        
        while True:
            pos = int(input('Enter the position player 2 want to place the mark: '))
            if pos in  range(1,10):
                break
        place_marker(test_board, mark[1],pos)
        clear_output()
        display_board(test_board)
        if win_check(test_board , mark[1]):
            print('Player 2 has won the game. Congrats.')
            break
print('Thank You for using this software,do share any any updates regarding the same.\nPeace.')
#game
