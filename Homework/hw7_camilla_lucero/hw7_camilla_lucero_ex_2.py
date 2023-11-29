'''
Homework 7, Exercise 2
Camilla Lucero
11/28/2023

This program experiments with optimizing the fibonacci sequence using a cache decorator that stores values 
that have not been calculated before in the sequence, while just returning values that have been calculated before.
---------------------------------------------------------------------------------------------------------------------
Conclusion :
Number of calls to fibonacci(), without caching (First 20 numbers) = 35,400 function calls
Number of calls to fibonacci(), with caching (First 20 numbers) = 56 function calls

You greatly reduce the amount of function calls when using this caching system compared to when it is not
used. This is due to the amount of recalculating the function needs to do to get back up to numbers as high as
4181 (the 20th number of the sequence). 
'''

import functools

#Taken from lecture!
#count calls decorator
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        #i dont need this function to remind me of wrapper calls, so i comment this out!
        #print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        #print("")
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

#Cache decorator
def cache(funct):
    #create our dictionary to hold the results
    cache.results = {}
    
    def wrapper (*args, **kwargs):
        #check if our argument is in our dictionary
        if args in cache.results:
            #if so, just return the value, don't index since we've already calculated!
            return cache.results[args]
        else:
            #else, if it isn't, then calculate that number and put it into the cache 
            returnValue = funct(*args)
            cache.results[args] = returnValue
            #Then return that value
            return returnValue 
    return wrapper

@countCalls
@cache #Comment this out when we want to see the difference between caching and not!
#Taken from Homework!
#Fibonacci function
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    

#----------------------------------------------------------
#This is used to dictate how many fib numbers we want
numFib = 20 
print("Printing the first " + str(numFib) + " numbers of the Fibonacci Sequence...")

#Iterate & grab up to numFib numbers in the fibbonacci sequence
for i in range(numFib):

    #Grab value & Print afterwards
    returnValue=fibonacci(i)
    print(returnValue, end=" ")
print(" ")
print("-------------------------")

#Report how many calls were made to fibonacci()
print("Number of fibonacci() calls = ", end="")
print (fibonacci.numCalls)

