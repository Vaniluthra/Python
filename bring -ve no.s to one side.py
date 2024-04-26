'''
Description
Program to bring all negative numbers to one side of a list
'''
a = list(map(int, input('Enter space separated list elements:').split()))
c=0
for i in range(len(a)):
    
    if a[i] < 0:
        
        a[c],a[i]=a[i],a[c]
        c+=1
print(a)
