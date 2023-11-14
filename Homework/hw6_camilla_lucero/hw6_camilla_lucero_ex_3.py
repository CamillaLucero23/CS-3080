'''
Homework 6, Exercise 3
Camilla Lucero
11/14/2023

This program experiments with threads, asking for a number of threads to start, starts them and prints their
info in a logging dubug format
'''
import threading
import logging
import time

def someFunc(i):
    #set up our log config.
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(lineno)d - %(message)s')

    #Print thread info
    logging.debug("Welcome, Thread " + str(i))

    #check for odd or even
    if i%2 == 0:
        logging.debug("Number " + str(i) + " is even.")
    
    else:
        logging.debug("Number " + str(i) + " is odd.")
    
    #required sleep
    time.sleep(3)

    logging.debug("Goodbye, Thread " + str(i))

#Prompt for number of threads
while True:
    print("How many threads would you like to start?")
    numThreads = input()
    
    #Check if input is an int and greater than 2...
    if isinstance(numThreads, int):
        #If not, then prompt
        print("Please enter an integer, not a string or floating point number.")

    elif int(numThreads) <= 2:
        #If not, then prompt
        print("Please enter an integer that is greater than 2.")   

    else:
        #If so, then break loop
        numThreads = int(numThreads)
        break

#Create & Start threads using someFunc()
for i in range(numThreads):

    #create a new thread and pass it i
    newThread = threading.Thread(target=someFunc, args=[i])

    #Start it >:)
    newThread.start()

#Once all threads are created, join them together
for i in range(numThreads):
    newThread.join()

