def printLine():
    print("------------------------------------------------------------------------------------------\n")


# Range() Function Test
print("Start Range(5)")
for i in range(5):
    print(str(i))

print("End Range(5)\n")
printLine()

#Importing Modules
import random
print("Random Number -> "+ str(random.randint(1,10)) +"\n")

printLine()

#Keyword Arguments
print("Cats","Dogs","Rats")
    #prints Cats Dogs Rats (seperated by default with a space)

print("cats","dogs","rats", sep=", " )
    #prints cats, dogs, rats (seperates terms with a comma and a space)

print("Hello", end=" ")
print("World")
    #prints Hello World (Replaces automatic /n with specified character/ string)

print('cats','dogs','mice', sep=", ", end = '.\n\n')
    #prints cats, dogs, mice.



def fun(a,b):
    print("a is " + str(a))
    print("b is " + str(b) + "\n")

    return a+b

fun (5, 18)

fun(a=5, b=18)

fun(b=18,a=5)