n=int(input())
a=1
b=n-1
while b>=0:
    print(" "*b, "*"*a, " ", sep='')
    a+=2
    b-=1