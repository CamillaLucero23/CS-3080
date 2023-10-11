'''
Homework 4, Exercise 3
Camilla Lucero
10/11/2023

This program checks for password strength using Regex's. Strong password require a length of 8
characters, both an uppercase and lowercase, and at least one digit
'''
#import re
import re

#variables
isStrong = False #Boolean flag for loop
lengthCheckRegEx = re.compile(r"\w{1}") #regex for length check
numberCheckRegEx = re.compile(r"\d") #regex for number check
upperCaseCheckRegEx = re.compile(r"[A-Z]") #regex for upper case check
lowerCaseCheckRegEx = re.compile(r"[a-z]") #regex for lower case check


while(isStrong != True):
    #User input
    print("Enter a Strong Password (8 characters in length, Uppercase & lowercase, and atleast one digit): ")
    userInput = input()

    #perform checks on input
    lengthCheck = lengthCheckRegEx.findall(userInput)
    numberCheck = numberCheckRegEx.findall(userInput)
    upperCaseCheck = upperCaseCheckRegEx.findall(userInput)
    lowerCaseCheck = lowerCaseCheckRegEx.findall(userInput)

    #If length is less than 8, prompt
    if(len(lengthCheck) < 8):
        print("This password is too short.")

    else:
        #else check if there is a digit present
        if(len(numberCheck) == 0):
            print("Please include a digit in your password.")
        
        else:
            #else, check if there is both an upper and lower case
            if(len(upperCaseCheck) == 0 or len(lowerCaseCheck) == 0):
                print("Please include both an uppercase and a lowercase letter in your password")
            
            #else, the password is strong!
            else:
                print("Your password is strong!")
                isStrong = True


