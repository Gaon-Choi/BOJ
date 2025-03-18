n=1
f=int(input())
for x in range(1,f+1):
    if n%2==1:
        print("* "*(f-1),"*",sep='')
        n+=1
    else:
        print(" *"*f)
        n+=1