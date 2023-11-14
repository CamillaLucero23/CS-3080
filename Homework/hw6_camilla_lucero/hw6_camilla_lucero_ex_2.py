'''
Homework 6, Exercise 2
Camilla Lucero
11/12/2023

This program searches through an indicated file and find any file with the indicated extention 
(pdf by default). Reports the absolute path of the file and how big it is. Also stores alls pdfs
into a folder in current working directory
'''

import os
import shutil

#The file extension we are looking for
fileExt = "pdf"

#Filepath for os.walk()
directoryFilePath = os.path.join('.','hw6_camilla_lucero','hw6_test_ex_2')

#create file to store pdf's in
allPdfsFilePath = os.path.join('.',"allPdfs")

#Check if file exists...
if not os.path.exists(allPdfsFilePath):
  #if it doesn't, then make it
  os.makedirs(allPdfsFilePath)
else:   
  #if it does, then prompt and exit
  print(os.path.abspath(allPdfsFilePath) + " already exists! Please delete this file and try again!")
  exit()

#Iterate through our indicated filepath
for (root, dirs, files) in os.walk(directoryFilePath):

  #Iterate through all files 
  for file in files:

    #Check if file ends with pdf
    if file.lower().endswith(fileExt.lower()):
      #if it does, then report the file's path and size
      print("PDF found!")
      
      #copy file, first we need the relative path
      currentFileRelPath = os.path.join(root,file)
      shutil.copy(currentFileRelPath ,allPdfsFilePath)

      currentFileAbsPath = os.path.abspath(currentFileRelPath) #get the file's absolute path

      print("This file is located at: " + currentFileAbsPath)
      print("This file is " + str(os.path.getsize(currentFileAbsPath)) + " bytes")
      print("----------------------------------------------------------------------")


  
  

  
    
