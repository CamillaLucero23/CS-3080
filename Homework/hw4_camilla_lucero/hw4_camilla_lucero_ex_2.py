'''
Homework 4, Exercise 2
Camilla Lucero
10/10/2023

This progam searches for phone number and email addresses in respective given strings.
'''
#import regex
import re

#Phone Number Catch
#phone number test string
phoneNumberTestString = "(202) 225–3121, 1-800–252–2873 , 1 (800) 843–5763 , 455-5660 , 911, 327, 1 (800) 566 4666, 1 800 788 6887 ext 444"

#create regex
#((\d[ -.])?                      -> covers the optional funny 1 for american numbers
#((\(?\d{3}\)?)(\s|-|.))?         -> covers the area code, optional paranthesis, and seperator for next number 
#(\d{3}(\s|-|.)\d{4})             -> covers main required number (xxx-xxxx), with seperator between
#((\s*(ext|x|ext.)\s*)(\d{2,5}))? -> Covers if number has an extention afterwards
#|(\d{2,5}))                      -> if number is not a full number and just an extension, catch that instead
phoneNumRegEx = re.compile(r"((\d[ -.])?((\(?\d{3}\)?)(\s|-|.))?(\d{3}(\s|-|.)\d{4})((\s*(ext|x|ext.)\s*)(\d{2,5}))?|(\d{2,5}))")

#Find all numbers
foundNumbers = phoneNumRegEx.findall(phoneNumberTestString)

#Print found numbers
print("String to be searched: " + phoneNumberTestString)
print("Found items in this string are... ")

for i in range(len(foundNumbers)):
    print(foundNumbers[i][0]) #Print index 0 because that is where the full number is
    
print("-------------------------------------------------------------------------------------------")

#Email Catch
emailTestString = "clucero9@gmail.com, cluCero+_.-%@UCcs12.edu, clucero+_.-%@$uccs.edu ,john_doe@python.co.uk, clucero9@uccs^.com"

#create regex
#[A-Za-z0-9+%_.-]+ -> covers username and all possibilities
#@[A-Za-z0-9]+     -> grabs @ and domain name
#\.\w{3})          -> grabs dot and the ending 3 letters
emailRegEx = re.compile(r"([A-Za-z0-9+%_.-]+@[A-Za-z0-9]+\.\w{3})")

#find all email addresses
foundEmails = emailRegEx.findall(emailTestString)

#print found addresses
print("String to be searched: " + emailTestString)
print("Found emails in this string are... ")

for i in range(len(foundEmails)):
    print(foundEmails[i]) #Not stored in list, dont need to get first index!
print("-------------------------------------------------------------------------------------------")