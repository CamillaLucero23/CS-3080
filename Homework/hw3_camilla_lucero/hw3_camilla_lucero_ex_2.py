'''
Homework 3, Exercise 2
Camilla Lucero
9/25/2023

This program, given a string, counts the number of letter occurences in that string
and puts those stats in a dictionary, then prints the dictionary
'''
#string that the program counts
string = "The quick brown fox jumps over the lazy dog"

#dictionary for letter occurences
letterOccurences = {}


for i in range(len(string)):
    #get one letter from string
    currentLetter = string[i]

    #determine if letter is in dictionary
    if currentLetter not in letterOccurences:
        #if not, add to dictionary
        letterOccurences[currentLetter] = 1
    
    else:
        #if in dictionary, iterate
        letterOccurences[currentLetter] += 1


#import pretty print
import pprint

#print dictionary
pprint.pprint(letterOccurences)