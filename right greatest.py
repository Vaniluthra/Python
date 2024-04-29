'''

'''
a=list(map(int,input('enter space separated values:').split()))
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]<a[j]:
            a[i]=a[j]
            break
        if j==n-1:
            a[i]=-1
a[-1]=-1
print(a)
