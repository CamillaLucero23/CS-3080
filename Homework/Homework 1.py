'''
Homework 1
Camilla Lucero
8/28/2023
Program Desc. : 
'''
def compareResponseAndAnswer(response, answer):
    #if response matches answer, return the following boolean/ 1 or 0
    if response == answer:
        return 1
    else:
        return 0
    



#initial boolean
isAccessGranted = False

#while the boolean flag is false...
while isAccessGranted != True:
  
    #question 1 - math with random ints
    #generate 2 random ints
    from random import randint
    randomInt1 = randint(1,150)
    randomInt2 = randint(1,150)

    print("What is the sum of the following integers? " + str(randomInt1) + " + " + str(randomInt2))
    userResponse = input()

    #check if answer is correct, if so, continue, if not, break loop
    isCorrectAnswer = compareResponseAndAnswer(int(userResponse), randomInt1+randomInt2)
    if isCorrectAnswer :

        #question 2 - counting letters
        countingLettersWord = 'Archipelago' #Answer is 11 incase I am dumb and forget :)
        countingLettersLength = len(countingLettersWord)
        print("Count and input the number of letters in this word: " + countingLettersWord)
        userResponse = input()
        
        #check if answer is correct. if so, continue, if not, break loop
        isCorrectAnswer = compareResponseAndAnswer(int(userResponse), countingLettersLength)
        if isCorrectAnswer == 1 :

            #question 3,4,5 (iterates 3 times) - Evens and Odds Using a For Loop
            for i in range(3):
                #declare temp variable for if i is even or odd
                tempEvenOrOdd = i%2
                print("Is " + str(i+1) + " even or odd?")
                userResponse = input()

                #Translate words into a comparable remainder
                if (int(userResponse))

                #check if answer is correct. if so, continue, if not, break loop
                isCorrectAnswer = compareResponseAndAnswer(userResponse, tempEvenOrOdd)
                if isCorrectAnswer:

                    #question 6

            
    if isAccessGranted != True:
        print("Your Answer was incorrect, please try again from the beginning.")
        print("------------------------------------------------------------------------------------------")
       
  
        

        