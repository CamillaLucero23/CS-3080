#question 1
a = [1, 2, 3]
b = []
b.append(a)
b.append(a)
b[1][2] = 4
print(b)
print(a)

print("-------------------------------------")
#question 2
exp = lambda var: [x*3 for x in range(var) if x%2 != 0]
print(exp(8))