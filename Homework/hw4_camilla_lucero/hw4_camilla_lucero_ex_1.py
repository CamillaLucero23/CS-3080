'''
Homework 4, Exercise 1
Camilla Lucero
10/10/2023

This program...
'''

#import math because... well duh
import math

#classes
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
        return 2(self.length + self.width)
    
    #Calculate Diagonal
    def calculateDiagonal(self):
        return math.sqrt((self.length + self.width))
    

class Square(Rectangle):

