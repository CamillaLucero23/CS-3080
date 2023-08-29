'''
Homework 1
Camilla Lucero
8/28/2023
Program Desc. : 
'''

#compares two values and returns a 1 if they are the same and 0 if they are not
def compareResponseAndAnswer(response, answer):
    #if response matches answer, return the following boolean/ 1 or 0
    if response == answer:
        return 1
    else:
        return 0

#Title Comment
print("Welcome To The 3080 Security System\nAnswer The following questions to gain access to the system.")
print("------------------------------------------------------------------------------------------")

#initial boolean flag for while
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
        if isCorrectAnswer:

            #question 3,4,5 (iterates 3 times) - Evens and Odds Using a For Loop
            #define correct answer counter for loop
            correctAnswerCount = 0
            for i in range(3):
                #declare temp variable for if i is even or odd
                tempEvenOrOdd = (i+1)%2
                print("Is " + str(i+1) + " even or odd? Enter e for even and o for odd")
                userResponse = input()

                 #Translate words into a comparable remainder
                if userResponse == "e" or userResponse == "E":
                    userResponse = 0
                elif tempEvenOrOdd != 0 and userResponse == "o" or userResponse == "O":
                    userResponse = tempEvenOrOdd
                elif userResponse != 0 or userResponse != tempEvenOrOdd:
                    print("Entered Response was not an e or o!")
                    break

                #check if answer is correct. if so, continue, if not, break loop
                isCorrectAnswer = compareResponseAndAnswer(userResponse, tempEvenOrOdd)
                if isCorrectAnswer:
                    correctAnswerCount+= 1
                    
                    #if answered 3 correct answer, exit from for
                    if correctAnswerCount == 3:
                        break
                else:
                    break

            if correctAnswerCount == 3:
                  #question 6 - Multiplication & Subraction
                    #random float variable
                    randomFloat = randint(1,150) / 2.5
                    floatQuestionResult = randomInt2*randomInt1-randomFloat


                    print("Solve the following problem: " + str(randomInt2) + " * " + str(randomInt1) + " - " + str(randomFloat))
                    userResponse = input()

                    #check if answer is correct. if so, continue, if not, break loop
                    isCorrectAnswer = compareResponseAndAnswer(float(userResponse), floatQuestionResult)
                    if isCorrectAnswer:
                        isAccessGranted = True
                        continue
                        
        #if answer is incorrect, prompt and repeat
        print("Your Answer was incorrect, please try again from the beginning.")
        print("------------------------------------------------------------------------------------------")
    
#access granted if all questions have been answered correctly
print("------------------------------------------------------------------------------------------")
print("Access Granted")
  
        

        