'''
Program to encrypt a given string, each charecter should be replaced with the charecter that comes next to it in the alphabet, 
also each number should be replaced with the number that comes next to it.
'''

def f(a,k):
    st=[]
    if (0>k>25):
        return 'invalid input'
    for i in a:
        if i.isalpha() or i.isnumeric():
            num=ord(i)
            char=chr(num+k)
            st.append(char)
            
        else:
            st.append(i)
    return ''.join(st)
a=input('enter string: ')
k=int(input('k: '))
r=f(a,k)
print(r)
