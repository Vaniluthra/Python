def s(st,ch1,ch2):
    st2=st
    st2=list(st2)
    st=list(st)
    for i in range(len(st2)):
        if st2[i]==ch1:
            st[i]=ch2
        if st2[i]==ch2:
            st[i]=ch1
    return ''.join(st)
st=int(input())
ch1=int(input())
ch2=int(input())

res=s(st,ch1,ch2)
print(res)
