'''
Homework 5, Exercise 2
Camilla Lucero
10/25/2023

This program 
'''

import math

#Integers function from lecture
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1


def pyt():
   limit = 100 # a temp limit to make sure the program doesnt spiral 

    #for a in an infinite pool of integers
   for a in integers():
       
       #for b in current a + 1 (since a has to be less than b)
       for b in range(a+1, a+limit):
           
           #get hypotoneuse from a and b
           c = math.sqrt((a * a) + (b * b))

           #check if it is an integer, not a float and is less than self imposed limit
           if c.is_integer() and c <= limit :
               #yield to caller
               yield (a,b,int(c))
        

#take function from lecture
def take(n, sequence):
    """Returns first n values from the given sequence."""
    sequence = iter(sequence) # Just in case it is an iterable object,
                    # not a generator or iterator
    result = []
    try:
        for i in range(n):
            result.append(next(sequence))
    except StopIteration:
        pass


    return result


from random import randint

#generate a random number based on upper and lower bounds
randomUpper = 20
randomLower = 1
n = randint(randomLower,randomUpper)

#display 'title'
print("The first " + str(n) + " pythagorean triples are....")

#print the generated list
print(take(n,pyt()))


