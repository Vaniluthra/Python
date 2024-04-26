''' 
Description
The function accepts a list of size n as its arguments, return the sum of second largest element from the even positions and second smallest from the odd position of given list
'''
def f(l,li):

    m=max(l)
    mi=max(li)
    
    l.remove(m)
    li.remove(mi)

    return max(l),max(li)

n=int(input('n:'))
t1,t2=[],[]
for i in range(n):
    inp=int(input())
    if i%2==0:
        t1.append(inp)
    else:
        t2.append(inp)
print(t1,t2)
r,r1=f(t1,t2)
