'''
Homework 2, Exercise 4
Camilla Lucero
09/13/2023
Program Desc. : 
'''

#Define "constants"
upperLimit = 20 # Upper limit fornum generation
numberOfGuesses = 10 #number of guesses the user can utilize

#generate random number
from random import randint
randomNum = randint(1,upperLimit)

#prompt & begin number search!
print("I'm thinking of a number between 1 and " + str(upperLimit) + ". You have " + str(numberOfGuesses) + " tries! Good Luck!")



