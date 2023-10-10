'''
Homework 3, Exercise 4
Camilla Lucero
9/25/2023

This program simulates a semi-functioning tictactoe game. It can be noted that
this game does allow spots to be overridden and does not check for who wins!
'''
#displays tictacboard, parameters- listed lists
def displayBoard(ticTacToe):
    
    gridRows = len(ticTacToe)

    for row in range(gridRows):
        #get ammount of col
        gridCol = len(ticTacToe[row])

        #print
        for col in range(gridCol):

            if col != gridCol-1:
                print(ticTacToe[row][col],end= "\t|")

            else:
                print(ticTacToe[row][col], end=" \n")
    
        if row != gridRows-1:
             #print new line for next Row
            print("---------------------------")  


#gets valid integer input between 1 and 3
def getValidInt():

    #initialize return value and bool flag
    userInput = " "
    isCorrect = False

    #while we dont have a valid value
    while (isCorrect == False):

        #try to get integer, and print error if input is not integer
        try:
            userInput = int(input())
        except ValueError:
            print("Pleast Enter An Integer")  
        
        #if int, then check if number is between 1 and 3
        if str(userInput).isnumeric() == True :
            if userInput < 1 or userInput > 3:
                print("Please Enter A Valid Coordinant")
            else:
                isCorrect = True

    return userInput


#executes a player turn, parameters- listed list for board, the current player, and a list with coordinants
def playerTurn(ticTacToe, player, coordinants):

    characterToPlace = ' '

    #determine which character is placed
    if player == 1:
        characterToPlace = 'X'
    else:
        characterToPlace = 'O'

    #subtract 1 from coordiants and place
    coordinant1 = coordinants[0] - 1
    coordinant2 = coordinants[1] -1 
    
    ticTacToe[coordinant1][coordinant2] = characterToPlace


#tictacetoe list
ticTacToe = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

#determines which player plays first
whichPlayer = 1

#complete a 9 round game
for i in range(9):

    #display board
    displayBoard(ticTacToe)

    #initialize coordinants
    coordinants = [0,0]
    
    print("Enter a coordinant, like 3 [enter] 2 for the bottom middle spot...")
    #determine which player is playing 
    if(whichPlayer == 1):
        print("Player 1's turn: ")

        whichPlayer = 2
    else:
        print("Player 2's Turn: ")
    
        whichPlayer = 1
    
    #get coordinants
    for i in range(2):
        coordinants[i] = getValidInt()

    #play player's turn
    playerTurn(ticTacToe, whichPlayer, coordinants)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")