'''
Homework 2, Exercise 4
Camilla Lucero
09/13/2023
Program Desc. : this program generates a random number based on two randomly generated bounds and asks the 
                user to guess the number is 10 tries. Depending on the user's guess, the program will print if an answer is too 
                high or low. if the user doesnt guess in 10 tries, the program reveals the answer. if they do guess,
                the program reveals how many tries the user took to guess.
'''
#Validates User Input 
def getValidUserInput():

   while True:
        #try getting input and converting into int
    try:
        return int(input())
    
    #except when the int conversion doesnt work, print error
    except ValueError:
        
        print("Please enter an integer.")

#compare two integers and prompt whether the guess was too high or too low and return false if so. If guess is the answer, return true
def compareInts (guess, answer):
   if guess > answer:
      print("Your guess is too high!")
      return False
   
   elif guess < answer:
      print("Your guess is too low!")
      return False
   else:
      return True
        
    

#Define "constants" 
from random import randint
randomLimit = 1000
numberOfGuesses = 10 #number of guesses the user can utilize
lower = randint(1,randomLimit) #Lower Limit for num generation
upper = randint(lower,randomLimit) # Upper limit fornum generation



#generate random number
randomNum = randint(lower,upper)

#prompt & begin number search!
print("I'm thinking of a number between " +str(lower) + " and " + str(upper) + ". You have " + str(numberOfGuesses) + " tries! Good Luck!")

#boolean flag & guess counter
isGuess = False
guessCounter = 0

#while number hasn't been guessed and the guess counter is not 10
while guessCounter != numberOfGuesses and isGuess == False:
    #prompt and get input
    print("Take a Guess...")
    userInput = getValidUserInput()

    #compare input & iterate counter/ escape loop 
    isGuess = compareInts(userInput,randomNum)

    #if guess was false, iterate counter
    if isGuess == False:
       guessCounter += 1

if isGuess == True:
   print("Congratualtions! You guessed my number in " + str(guessCounter) + " guesses!")

else:
   print("Sorry! My number was " + str(randomNum) + ".")

    