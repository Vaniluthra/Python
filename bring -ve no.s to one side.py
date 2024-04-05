a = list(map(int, input('enter space separated list elements:').split()))
c=0
for i in range(len(a)):
    
    if a[i] < 0:
        
        a[c],a[i]=a[i],a[c]
        c+=1
print(a)
