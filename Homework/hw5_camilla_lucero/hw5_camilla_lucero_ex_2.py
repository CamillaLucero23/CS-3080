'''
Homework 5, Exercise 2
Camilla Lucero
10/25/2023

This program calculates n (set to 10 by default) pythagorean triples using generators
'''

#Integers function from lecture
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1


def pyt():
   limit = 100 # a limit to make sure the program doesnt spiral
   from math import sqrt

    #for a in an infinite pool of integers
   for a in integers():
       
       #for b starting @ current a + 1 (since a has to be less than b) and ending at self imposed limit 
       for b in range(a+1, limit + 1):
           
           #get hypotoneuse from a and b
           c = sqrt((a * a) + (b * b))

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


#number of triples the program will generate
numberOfTriples = 10

#display 'title'
print("The first " + str(numberOfTriples) + " pythagorean triples are....")

#print the generated list
print(take(numberOfTriples,pyt()))