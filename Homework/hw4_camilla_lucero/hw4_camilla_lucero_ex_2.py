'''
Homework 4, Exercise 2
Camilla Lucero
10/10/2023


'''
#import regex
import re

stringToTest = "(202) 225–3121 , 1–800–252–2873 , 1 (800) 843–5763 , 911"

#create regex
phoneNumRegEx = re.compile(r'''
                           (\d)?  #funny little american number at the front(optional)
                           (\s|-|\.)? #Seperator (Optional)
                           (\(?\d{3}\)?)? #area code (Optional)
                            (\s|-|\.)? #Seperator (Optional)
                           \d{3} #3 Numbers (Required)
                            (\s|-|\.)? #Seperator (Required)
                           \d{4} #4 Numbers (Required)
                           (\s*(ext|x|ext.)\s*\d{2,5})? #extension (optional)
                            ''', re.VERBOSE)

foundNumbers = phoneNumRegEx.findall(stringToTest)



