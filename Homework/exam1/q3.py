'''
Generate a random integer between 1 and 7 (both inclusive) and store it in a variable n. 
Display the first n squares that are NOT divisible by 2 (excluding 0, as we consider 0 
being divisible by 2). For example: if the random integer n is 5, 
the output should be 1 9 25 49 81, i.e., including 5 numbers. Note that the result is not 1 9 25. 
'''

from random import randint
randomLower = 1
randomUpper = 7
n = randint(randomLower,randomUpper)
nonEvenSquares = []
x = 1

while len(nonEvenSquares) != n:
    temp = x**2
    if temp%2 != 0:
        nonEvenSquares.append(temp)
    
    x+=1

print("n is " + str(n))
print("The first " + str(n) + " square(s) that are not divisible by 2 are:")
for i in range(len(nonEvenSquares)):
    print(nonEvenSquares[i], end= " ")