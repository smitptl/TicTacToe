# TIc Tac Toe

import random

def drawBoard(board):
    # this function prints out the board that it was passed.

    # "board" is a  list of 10 strings representing the board(ignore index 0)

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputPlayerLetter():

    # let's the player type which letters they want to be.
    # returns a list with the player's letters as the first item, and the computer's letters as the second.

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    
