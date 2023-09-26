'''
Homework 3, Exercise 4
Camilla Lucero
9/25/2023

This program 
'''

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


def getValidInput(inputOptions):

    userInput = " "
    isCorrect = False


    while (isCorrect != True):

        print("Input Options: ")
        for i in range(len (inputOptions)):
             print(inputOptions[i], end= ", ")

        print()


        userInput = input()
        userInput = userInput.lower()
        isAlpha = userInput.isalpha()

        if isAlpha == False :
            print("Please Enter A String")

        else:

            for i in range(len(inputOptions)):

                if userInput == inputOptions:
                    isCorrect = True

            if isCorrect != True:

                print("Please Enter A Valid String")
                

       
    return userInput


def playerTurn(ticTacToe, player, where):

    characterToPlace = 'c'

    if player == 1:
        characterToPlace = 'X'
    else:
        characterToPlace = 'O'

    
ticTacToe = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

inputOptions = ("top left", "top middle", "top right", "middle left",
                 "middle middle", "middle right", "bottom left",
                   "bottom middle", "bottom right")

whichPlayer = 1

for i in range(9):
    displayBoard(ticTacToe)
   
    if(whichPlayer == 1):
        print("Player 1's turn: ")

        whichPlayer = 2
    else:
        print("Player 2's Turn: ")
    
        whichPlayer = 1
    
    userInput = getValidInput(inputOptions)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")