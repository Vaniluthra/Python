m = [1, 2, 3, 4, 5, 6, 7]
n=int(input('n= '))
n = n % len(m) if n >= len(m) else n
for i in range(n):
    m.insert(0,m[-1])
    m.pop()
print(m)
