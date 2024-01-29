'''
Create two threads. One thread is created using a function called printCubes(n) that prints the first 
n cubes (e.g., if n=5, it prints 1 8 27 64 125). The second thread is created using a function called 
printSquares(n) that prints the first n squares (e.g., if n=5, it prints 1 4 9 16 25). n is a random 
integer between 5 and 12 (both inclusive). Do not hard code the value of n. Use the same n value to pass
to these two threads. 

Make sure two threads using printCubes(n) and printSquares(n) are NOT printing values in a random order,
and you cannot use sleep() to enforce this. If you call printCubes(n) and printSquares(n) as functions 
instead of creating threads, you will lose at least 20pts.

Within each thread, also use the time module to measure how long each thread takes from start to finish, 
and print the execution time with 4 decimal points. Do not use the timer decorator provided in class. An 
example output:

The first 12 cubes: 1 8 27 64 125 216 343 512 729 1000 1331 1728 
printCubes(12) took 0.0001 secs to finish
The first 12 squares: 1 4 9 16 25 36 49 64 81 100 121 144 
printSquares(12) took 0.0001 secs to finish

Print the values in the exact same format as above. Please save your code as q6.py
'''

import threading
import time
from random import randint

#printCubes
def printCubes(n):
    #Start thetimer
    startTime = time.perf_counter()
    #begin generating our cubes
    cubes = [i**3 for i in range(1,n+1)]

    #once done generating, we can print them
    print("The first " + str(n) + " cubes are: ", end="")
    for i in range(len(cubes)):
        print(cubes[i], end=" ")
    print()

    #end the counter, calculate runtime, and print
    endTime = time.perf_counter()
    runTime = endTime - startTime
    print(f"printCubes({n}) took {runTime:.4f} seconds to run.")


#print squares
def printSquares(n):
    #start the timer
    startTime = time.perf_counter()
    #generate our squares
    squares = [i**2 for i in range(1,n+1)]

    #once done generating, we can print them
    print("The first " + str(n) + " squares are: ", end="")
    for i in range(len(squares)):
        print(squares[i], end=" ")
    print()
    
    #end the counter, calculate our runtime, and print
    endTime = time.perf_counter()
    runTime = endTime - startTime
    print(f"printSquares({n}) took {runTime:.4f} seconds to run.")
    
#get a random int
n = randint(5,12)

#intialize threads
cubesThread = threading.Thread(target=printCubes, args=(n,))
squaresThread = threading.Thread(target=printSquares, args=(n,))

#start cubes
cubesThread.start()
cubesThread.join() #we have to wait until the cubesThread joins back with the main thread to prevent overlap
                   # of values

#start squares
squaresThread.start()

