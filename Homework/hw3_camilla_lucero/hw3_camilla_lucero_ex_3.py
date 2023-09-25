'''
Homework 3, Exercise 3
Camilla Lucero
9/25/2023

This program simulates the adding and deleting of items in a store's inventory
'''
#prints a store inventory list. Parameters - a list
def printInventory (inventory):
    #Title
    print("Store Inventory".center(25, "-"))
    

    inventorySize = len(inventory)
    #for numbger of items in inventory...
    for i in range(inventorySize):

        #print
        print(inventory[i][0] + " - " + str(inventory[i][1]))

    print()



#finds item in a list. Parameters - list, string. Returns index of item or -1 if item is not found
def findItem(inventory,item):

    inventorySize = len(inventory)
    index = 0
    itemFound = False

    #iterate until item is found or add one
    while index in range(inventorySize) and itemFound != True:
        itemFound = item in inventory[index]
        
        if itemFound == False:
            index += 1
    
    #if item is not found, make index -1
    if itemFound == False:
        index = -1
    
    return index



#adds item to a list of store inventory items. parameters - list, new item to add
def addItem (inventory, newItem):
    
    #find item
    itemIndex = findItem(inventory, newItem)

    #if item not found, make new item
    if itemIndex == -1:
        inventory.append([newItem , 1])
    #if item is found, increase inventory number by 1
    else:
        inventory[itemIndex][1] += 1



#deletes items from a list of stores inventory. parameters - list, item to delete
def deleteItem (inventory, item):

    #findItem
    itemIndex = findItem(inventory, item) 

    if itemIndex == -1:
        print("This item does not exist in the store's inventory!")

    elif inventory[itemIndex][1] == 0:
        print("There are no items of this type in inventory already!")

    else:

        inventory[itemIndex][1] -= 1


#store info 
storeInventory = [["Hand Sanitizer", 10], ["Soap", 6], ["Kleenex", 22], ["Lotion", 16], ["Razors", 12]]

#print Store inventory
printInventory(storeInventory)

#demonstrates adding items
print("addItem(\"Advil\")")
addItem(storeInventory, "Advil")
print("addItem(\"Lotion\")")
addItem(storeInventory, "Lotion")

#prints updated store inventory
print("Print updated Store inventory\n")
printInventory(storeInventory)

#demonstrates deleting items
print("deleteItem(\"Advil\") twice")
deleteItem(storeInventory, "Advil")
deleteItem(storeInventory, "Advil")
print("deleteItem(\"Soap\")")
deleteItem(storeInventory, "Soap")
print("deleteItem(\"Tylenol\")")
deleteItem(storeInventory, "Tylenol")

#prints updated store inventory
print("Print updated Store inventory\n")
printInventory(storeInventory)  