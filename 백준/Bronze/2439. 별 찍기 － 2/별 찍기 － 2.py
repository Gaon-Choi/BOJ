n=int(input())
x=n
while x>=1:
    print(" "*(x-1),"*"*(n-x+1),sep='')
    x-=1