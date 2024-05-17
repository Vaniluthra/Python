'''
Determine if a given integer n is an Armstrong number of order 3, meaning if it is equal to the sum of the cubes of its digits.
'''

n = int(input("Enter a number: "))
s = 0
t = n

while t > 0:
   d = t % 10
   s += d ** 3
   t //= 10

if n == s:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
