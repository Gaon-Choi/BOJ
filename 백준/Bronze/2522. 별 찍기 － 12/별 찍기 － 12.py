n=int(input())
a=n-1
b=1
while a>=0:
    print(" "*a, "*"*b," ",sep="")
    a-=1
    b+=1
a+=2;b-=2
while a<=n-1:
    print(" "*a, "*"*b," ",sep="")
    a+=1
    b-=1