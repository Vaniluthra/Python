'''
Problem:
A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding 
two numbers from right-to-left one digit at a time
You are required to implement the following function.
Int NumberOfCarries(int num1 , int num2);
The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are 
required to calculate and return the total number of carries generated while 
adding digits of two numbers ‘num1’ and ‘ num2’.
Assumption: num1, num2>=0
Example:
• Input
o Num 1: 451
o Num 2: 349
• Output
o 2
Explanation:
Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried 
and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.
'''

a=int(input())
b=int(input())
m=min(len(str(a)),len(str(b)))
c=0
for i in range(m):
    if a!=0 or b!=0:
        num1=a%10
        num2=b%10
        s=num1+num2
        if s/10>=1:
            c+=1
        a=a//10 
        b=b//10
print(c)
