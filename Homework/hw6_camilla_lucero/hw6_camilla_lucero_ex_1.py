'''
Homework 6, Exercise 1
Camilla Lucero
11/09/2023

This program reads all the files in the current working directory for filenames with 
american formatted dates (MM-DD-YYYY) and swaps all with an asian formatted date (YYYY-MM-DD)
'''
import re

#Compile regex for american dates
americanDateRegEx = re.compile(r"((0[1-9]||1[012])[-](0[1-9]||1\d||2\d||3[1])[-](\d{4}))")

import os

#Get current directory
print("Reading file names from the following directory: " + os.getcwd())

import shutil

#List Directory & iterate through to catch dates
for fileName in os.listdir():

    #I used length to catch whether the regex caught something
    catchRegExLength = 0 #Set length to 0
    catchRegExResult = americanDateRegEx.findall(fileName) #Find any datesw within this filename
   
   #Check if the length has changed... If so...
    if catchRegExLength < len(catchRegExResult):
        #Get each part of date
        month = catchRegExResult[0][1]
        day = catchRegExResult[0][2]
        year = catchRegExResult[0][3]

        #Reform into an asian date
        asianDate = "{0}-{1}-{2}".format(year,month,day)
        #Use replace command to replace the current date with the updated one in the filename
        newFileName = fileName.replace(catchRegExResult[0][0],asianDate)

        #And rename filenames
        shutil.move(fileName, newFileName)
    
    print("...")

print("Date Changes Complete! Check the directory that was read for the results!")

       
        
       

    
    








