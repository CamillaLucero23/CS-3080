'''
Homework 5, Exercise 1
Camilla Lucero
10/24/2023

This program 
'''
#define reverse iterator class
class ReverseIter:

    #initializer
    def __init__(self, list):
        self.index = len(list) - 1 #Set "starting" index to the end of the object you are iterating
        self.list = list

    #iterator
    def _iter_(self):
        return self
    
    #define next
    def _next_(self):
        #Check if we are at the beginning of the list
        if self.index != 0:
            currentObject = self.index
            self.index -= 1 #If we aren't at beginning, then subtract one from the index

        else:
            raise StopIteration() #if we are at index 0, then stop iteration
        
    

iterationList = [1,2,3,4]

currentIter = ReverseIter(iterationList)
for i in range(len(iterationList) + 1):
    print(str(next(currentIter)))
