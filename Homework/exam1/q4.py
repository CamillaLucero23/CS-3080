testString = "It was a bright cold day in April, and the clocks were striking thirteen."


#count letter occurences
#dictionary for letter occurences
letterOccurences = {}
mostOccurencesAmmount = 1
mostOccurencesLetter =""
from string import punctuation

for i in range(len(testString)):
    #get one letter from string
    currentLetter = testString[i]

    #determine if letter is in dictionary
    if currentLetter not in letterOccurences:
        #if not, add to dictionary
        letterOccurences[currentLetter] = 1
    
    else:
        #if in dictionary, iterate
        letterOccurences[currentLetter] += 1

        if letterOccurences[currentLetter] > mostOccurencesAmmount and currentLetter not in punctuation and currentLetter != " ":
            mostOccurencesAmmount = letterOccurences[currentLetter]
            mostOccurencesLetter = currentLetter
    
print("The Letter "+ mostOccurencesLetter + " occures the most... Occurs " + str(mostOccurencesAmmount) + " times.")

import re
wordCounterRegEx = re.compile(r"\w+")
wordCount = wordCounterRegEx.findall(testString)
print("There are " + str(len(wordCount)) + " words in this string.")
