'''
Problem:
Swap first and last char of each word in a sentence
'''

s = input()
sp = s.split()

for i in range(len(sp)):
    si = list(sp[i])
    si[0], si[-1] = si[-1], si[0]
    sp[i] = ''.join(si)

print(sp)
