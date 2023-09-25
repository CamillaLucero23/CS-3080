'''
Homework 3, Exercise 4
Camilla Lucero
9/25/2023

This program 
'''

def displayeBoard(ticTacToe):
    

ticTacToe = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

whichPlayer = 1

for i in range(9):
    if(whichPlayer == 1):
        print("Player 1's turn: ")
        whichPlayer = 2
    else:
        print("Player 2's Turn: ")
        whichPlayer = 1