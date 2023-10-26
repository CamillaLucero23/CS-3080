'''
Homework 5, Exercise 1
Camilla Lucero
10/24/2023

This program uses an iterator to iterate through a list in reverse order (Last object to first)
'''
#define reverse iterator class
class ReverseIter:

    #initializer
    def __init__(self, list):
        self.index = len(list) #Set "starting" index to the end of the object you are iterating
        self.list = list

    #iterator
    def __iter__(self):
        return self
    
    #define next
    def __next__(self):
        #Check if we are at the beginning of the list
        if self.index != 0:
            currentObject = self.index
            self.index -= 1 #If we aren't at beginning, then subtract one from the index
            return currentObject

        else:
            raise StopIteration() #if we are at index 0, then stop iteration
        
#define list to iterate
iterationList = [1,2,3,4,5,6,7,8,9,10]

print("List to iterate: ", end= " ")
print(iterationList, end= "\n------------------\n")

print("Using an Iterator, iterate the list backwards....")
iter = ReverseIter(iterationList)
for i in range(len(iterationList) + 1):
    print(str(next(iter)))
