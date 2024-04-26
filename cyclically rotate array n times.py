'''
Description
Program to cyclically rotate an array n number of times
'''
m = list(map(int, input('Enter space separated list elements:').split()))
n = int(input('n= '))
n = n % len(m) if n >= len(m) else n
for i in range(n):
    m.insert(0,m[-1])
    m.pop()
print(m)
