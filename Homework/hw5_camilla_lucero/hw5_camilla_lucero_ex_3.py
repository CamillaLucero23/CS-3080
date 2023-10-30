'''
Homework 5, Exercise 3
Camilla Lucero
10/26/2023

This program recreates the range function as a generator named genrange and tests what values it can handle
'''
# range converted into a geneator
def genrange(stop, start=0, step=1):

    #define variable to keep track of our index and set equal to our start
    index = start

    #while index is less than our stop value...
    while index < stop:
        #yield that index
        yield index
        #and increment index after
        index += step

#define some list to iterate through
testList = [1,23,65,85,6,5,9,165,72,36,75,48,81,121,72]
print("List to test genrange: ", end="")
print(testList)
print("----------------------------------------------")

#test with no start or step arguments, just stop
print("genrange with no start or step and stop being length of list:")
for i in genrange(len(testList)):
    print(testList[i], end=" ")

#test with start @ an index
print("\ngenrange with start @ index 6 and stop being length of list: ")
for i in genrange(len(testList), 6 ):
    print(testList[i], end=" ")


#test with a step
print("\ngenrange with step of 2, start @ index 4, and stop being length of list:")
for i in genrange(len(testList),4,2):
    print(testList[i], end=" ")

#test with different stop 
print("\ngenrange with stop of index 10:")
for i in genrange(10):
    print(testList[i], end=" ")