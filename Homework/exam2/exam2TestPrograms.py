
#Question 1
def f(value, values):
    value = 1
    values[0] = 44

t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

print("-----------------------------------------------")

#question 2
import threading
import time

def someFunc():
    print('Doing something in someFunc')
    time.sleep(5)
    print('someFunc finished')

threadObj = threading.Thread(target=someFunc)
threadObj.start()

time.sleep(2)
threadObj.join()
print('End of program.')