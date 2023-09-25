'''
Homework 3, Exercise 1
Camilla Lucero
9/25/2023

This program prints the contents of a nested list
'''
#grid value for homework description
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#get ammount of rows
gridRows = len(grid)


#print grid
for row in range(gridRows):
    #get ammount of col
    gridCol = len(grid[row])

    #print
    for col in range(gridCol):
        print(grid[row][col], end= " ")
    
    #print new line for next column
    print()     