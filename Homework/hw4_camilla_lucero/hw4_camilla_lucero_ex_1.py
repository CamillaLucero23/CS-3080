'''
Homework 4, Exercise 1
Camilla Lucero
10/10/2023

This program calculates Circumfrence of a circle created by half the diagonal of a rectangle with width 
of 10, and length of 20. This program also have functions for circles, rectangles, and squares.
'''

#import math because... well duh
import math

#classes
#rectangle class
class Rectangle():

    #intialize
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #Calculate Area
    def calculateArea(self):
        return self.length * self.width
    
    #Calculate Perimeter
    def calculatePerimeter(self):
        return (2 * (self.length + self.width))
    
    #Calculate Diagonal
    def calculateDiagonal(self):
        return math.sqrt((self.length + self.width))
    
#square class
class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)


#circle class
class Circle():

    #intialize
    def __init__(self,radius):
        self.radius = radius

    #calculate Area
    def calculateArea(self):
        return (math.pi * math.exp2(self.radius))
    
    # get diameter
    def getDiameter(self):
        return self.radius * 2
    
    #calculate perimeter
    def calculateCircumfrence(self):
        return 2 * self.radius * math.pi
    
#define a rectanglg
rectangle = Rectangle(20,10) #make a rectangle with a length of 20 and width of 10

#calculate diagonal and make circle
diagonalRectangle = rectangle.calculateDiagonal()

circle = Circle((diagonalRectangle/2))

#calculate circumfrence and print
circleCircum = circle.calculateCircumfrence()

print("Circumfrence of a circle created by half the diagonal of a rectangle with width of 10, and length of 20 is..."+ str(circleCircum))
