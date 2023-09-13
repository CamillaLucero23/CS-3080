'''
Homework 2, Exercise 3
Camilla Lucero
09/13/2023
Program Desc. : This program shows lots of examples of different types of list manipulations.
'''

def strList(list):
    #get len of list
    listLength = len(list)
    returnString = ""

    #concat lists into a string with comma seperation and return
    for i in range(listLength):
        if i != listLength - 1 :
            returnString += list[i] + ", "
        else:
            returnString += "and " + list[i]
    
    return returnString

objects = ["Wallet","Phone","Keys"]

print("Objects list: ", objects)

objects.sort()
print("Objects List Sorted: ", objects)

print("First item in Objects List: ", objects[0])

print("Every item, but First Item: ", objects[1:(len(objects))])

print("Last Item in Objects List: ", objects[-1])

print("Index of Keys: ", objects.index("Keys"))

objects.append("Tablet")
print("Append 'Tablet' to list: ", objects)

objects.insert(2, "Mask")
print("Insert 'Mask' into 2nd index: ", objects)

objects.remove("Phone")
print("Remove 'Phone' from list: ", objects)

objects.sort(reverse=True)
print("Reverse the list: ", objects)

objectsString = strList(objects)
print("Objects but String: " + objectsString)