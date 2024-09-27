import copy
import sys
import time

def slowprint(s): ## Slowprint function for crawling messages
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.5/10)

gameBoard = ['1','2','3','4','5','6','7','8','9']

def main():
    _board_ = copy.deepcopy(gameBoard)
    board_Rows = [_board_[0:3],_board_[3:6],_board_[6:]]
    board_Columns = [_board_[0::3],_board_[1::3],_board_[2::3]]
    board_Diagonals = [_board_[0::4],_board_[2:7:2]]
    player_1, player_2 = new_Game()
    counter = 1
    while True:
        turn(player_1, player_2, counter, board_Rows, board_Columns, board_Diagonals)
        counter += 1

def new_Game(): ## Initiates values for name of players
    player_1 = input('\nEnter name of Player 1: ').strip()
    player_2 = input('\nEnter name of Player 2: ').strip()
    return player_1, player_2

def turn(p1,p2,turn_Count,rows,columns,diagonals): ## Sets up player turns and keeps track of rounds
    slowprint(f"\nRound {turn_Count}. {p1}'s turn.")
    board(rows)
    move(p1,'O',rows)
    update_ColumnsDiagonals(rows,columns,diagonals)
    board(rows)
    victory_Check(p1,rows,columns,diagonals)
    if turn_Count == 5:
        print("\nGame has ended in a tie.")
        restartGame()
    slowprint(f"\nRound {turn_Count}. {p2}'s turn.")
    board(rows)
    move(p2,'X',rows)
    update_ColumnsDiagonals(rows,columns,diagonals)
    board(rows)
    victory_Check(p2,rows,columns,diagonals)

def move(p,mark,rows): ## Let's player choose spot on board to mark and updates the board
    while True: 
        place = input(f'\n{p}, enter a number (1-9) to mark board: ')
        if place == '1' and rows[0][0] == '1':
            rows[0][0] = mark
            return rows
        elif place == '2' and rows[0][1] == '2':
            rows[0][1] = mark
            return rows
        elif place == '3' and rows[0][2] == '3':
            rows[0][2] = mark
            return rows
        elif place == '4' and rows[1][0] == '4':
            rows[1][0] = mark
            return rows
        elif place == '5' and rows[1][1] == '5':
            rows[1][1] = mark
            return rows
        elif place == '6' and rows[1][2] == '6':
            rows[1][2] = mark
            return rows
        elif place == '7' and rows[2][0] == '7':
            rows[2][0] = mark
            return rows
        elif place == '8' and rows[2][1] == '8':
            rows[2][1] = mark
            return rows
        elif place == '9' and rows[2][2] == '9':
            rows[2][2] = mark
            return rows
        else: 
            slowprint("\nInvalid entry. Try again.")
            continue

def update_ColumnsDiagonals(rows, columns, diagonals): ## Updates columns and diagonals
    
    columns[0] = [rows[0][0], rows[1][0], rows[2][0]]
    columns[1] = [rows[0][1], rows[1][1], rows[2][1]]
    columns[2] = [rows[0][2], rows[1][2], rows[2][2]]
    diagonals[0] = [rows[0][0], rows[1][1], rows[2][2]]
    diagonals[1] = [rows[0][2], rows[1][1], rows[2][0]]

def board(rows): ## prints the board

    print('\n',rows[0][0],'|',rows[0][1],'|',rows[0][2])
    print('-----------')
    print('',rows[1][0],'|',rows[1][1],'|',rows[1][2])
    print('-----------')
    print('',rows[2][0],'|',rows[2][1],'|',rows[2][2])

def restartGame():
    while True: 
        restart = input(f"\nPlay again? [Y]es or [N]o: ")
        if restart.lower() == 'y' or restart.lower() == 'yes' : 
            main()
        elif restart.lower() == 'n' or restart.lower() == 'no': 
            exit()
        else: 
            slowprint("\nInvalid entry. Try again.")
            continue

def victory(p): ## Declares winner and gives option to quit program or play again
    slowprint(f"\n{p} wins!")
    restartGame()

def victory_Check(p,rows,columns,diagonals): ## Checks after each move if player has won
    for row in rows : 
        if row.count('O') == 3 or row.count('X') == 3 : 
            victory(p)
    for column in columns : 
        if column.count('O') == 3 or column.count('X') == 3 : 
            victory(p)
    for diagonal in diagonals: 
        if diagonal.count('O') == 3 or diagonal.count('X') == 3 : 
            victory(p)

main()