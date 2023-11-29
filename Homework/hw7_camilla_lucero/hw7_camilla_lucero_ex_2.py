'''
Homework 7, Exercise 2
Camilla Lucero
11/28/2023

This program 
'''
import functools

#Cache decorator
def cache(funct):
    cache.calculationStore = {}
    def wrapper (*args, **kwargs):
        cache.calculationStore.append
        
    
        

    return wrapper


def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls




#Fibonacci function
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)