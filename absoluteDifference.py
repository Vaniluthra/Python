'''
Program to count the num of elements whose difference with a given 'num' is smaller that 'diff'
'''
arr=list(map(int,input('enter space separated values:').split()))
num=int(input())
diff=int(input())
c=0
for i in arr:
    if abs(num-i)<=diff:
        c+=1
print(c)
