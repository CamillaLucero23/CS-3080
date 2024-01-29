'''
Define a string variable 

hello = 'Hello World!'
Create an @lowercase decorator that will convert this string to all lowercase 'hello world!'.
Note: you cannot hard code 'hello world!' in the decorator.

Use a regular function printStr(hello) that prints your string variable, and it will be decorated 
with your @lowercase decorator. Call the decorated printStr(hello) to test your result. Note the 
hello string must be passed to the decorated printStr() as an argument. 

Please save your code as q5.py
'''
#lowercase decorator
def lowercase(func):
    def wrapper(*args, **kwargs):
        #convert the first arguement into lower, since that is the string that was passed
        lowerCaseString = args[0].lower()
        #then give it to the function
        func(lowerCaseString)
    return wrapper

#printStr
@lowercase
def printStr(string):
    print(string)


hello = 'Hello World!'

printStr(hello)