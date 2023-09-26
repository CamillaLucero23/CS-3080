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


def getValidInput():

    userInput = " "
    isCorrect = False
    attempts = 1


    while (attempts < 2):

        userInput = str(input())
        isNum = userInput.isalnum

        if isNum == False:
            print("Please Enter A Number.")
        
        elif userInput != 1 or userInput != 2 or userInput != 3:
            print("Please Enter A Valid Coordinant")
        
        else:
            if attempts >= 2:
                isCorrect = True
            
            attempts += 1

        
    return userInput


def playerTurn(ticTacToe, player, where):

    characterToPlace = ' '

    if player == 1:
        characterToPlace = 'X'
    else:
        characterToPlace = 'O'




    
ticTacToe = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

whichPlayer = 1

for i in range(9):
    displayBoard(ticTacToe)

    print("Enter a coordinant, like 2 2 for the middle spot...")
   
    if(whichPlayer == 1):
        print("Player 1's turn: ")

        whichPlayer = 2
    else:
        print("Player 2's Turn: ")
    
        whichPlayer = 1
    
    userInput = getValidInput()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")