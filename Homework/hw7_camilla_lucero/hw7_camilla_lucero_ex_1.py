'''
Homework 7, Exercise 1
Camilla Lucero
11/28/2023

This program experiments with a decorator and setting decorator arguments. 
'''
import time
import functools

#slowdown's rate is automatically set to 1
def slowDown(func=None,rate=1):
    #let the execution sleep...
    print("Sleep for " + str(rate) + " second(s)... Shhhh")

    #this is the actual decorator that handles the function call!, needed because if we do
    #slowDown(funct, rate), we would get errors when trying to change just rate
    def actualdecorator(func):
        
        """Sleep rate second before calling the function"""
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(rate)

            print("Wake up!")
            return func(*args, **kwargs)
        return wrapperSlowDown
    return actualdecorator

#We implement a new varaible to control the rate at which we wait in our decorator.
slowDownTimer = 3 # this is where you change the rate!
#we cant have negative seconds!!
if slowDownTimer < 1:
    slowDownTimer = 1

#slowDown function, taken from lecture!
@slowDown (rate=slowDownTimer) #set the rate we would like for the function to sleep before executing
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)

countdown(5)