def f(total,arr):
    s,c=0,0
    flag=False
        
    while s<=total:
        
        flag=True
        c+=1
        s=s+arr[i]

    if flag==False:
        return 0
    return c

total=int(input('r: '))

arr= list(map(int,input('enter space separated list elements:').split()))

res=f(total,arr)
print(res)
