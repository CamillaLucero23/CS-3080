'''
Homework 2, Exercise 1 
Camilla Lucero
09/12/2023
Program Desc. : This program asks the user for an integer and runs it through the Collatz sequence untill
                that number is = 1
'''

#collatz def
def collatz(number):

    #determine if number is even or odd
    isEven = number % 2
    
    #if even...
    if isEven == 0:
        #print and return it's //2 factor
        result = number//2

        print(str(result))
        return result
    #if odd...
    else :
        #print and return 3 * number + 1
        result = 3 * number + 1

        print(str(result))
        return result
    

#prompt for input & start the Collazt Sequence
print("Enter an integer to start The Collazt Sequence:")
userInput = int(input())
collatzReturn = userInput

while collatzReturn != 1:
    collatzReturn = collatz(collatzReturn)
