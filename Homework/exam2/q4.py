'''
Generate a random integer between 1 and 10 (both inclusive) and store it in a variable n. 
Do not hard code n. Use a Generator expression (NOT an object/class or a generator function) 
to generate the first n negative odd numbers starting from -1. For example, your output for 
n = 5 would be:

The first 5 negative odd numbers are: -1 -3 -5 -7 -9

Print the values in the exact same format as above. Please save your code as q4.py
'''

from random import randint

#generate random number
n = randint(1,10)
print("Random Number n is " + str(n) )

#Generate negative numbers up to n
#We multiply by 2 in order to get up to n, since we are getting every ODD number up to 10. If we just did
#in range(n), then we would only get half of the numbers required
negative_numbers = [-abs(i) for i in range(n * 2) if i%2 != 0]

#Print them in a nice format :)
print("The first " +  str(n) + " negative, odd number(s) are:", end=" ")
for i in range(len(negative_numbers)):
    print(negative_numbers[i], end=" ")