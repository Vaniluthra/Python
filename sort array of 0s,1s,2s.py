'''
Description
Program to sort an array containing 0,1 or 2
'''
a = list(map(int, input('Enter space separated list elements:').split()))
n = len(a)
c0 = c1 = 0
for i in a:
    if i == 0:
        c0 += 1
    elif i == 1:
        c1 += 1
for i in range(c0):
    a[i] = 0
for i in range(c0, c0 + c1):
    a[i] = 1
for i in range(c0 + c1, n):
    a[i] = 2
print(a)
