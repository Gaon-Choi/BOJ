a=int(input())
b=int(input())
c=int(input())
result=a*b*c
result=str(result)
counts=[]
for x in range(0,10):
    counts.append(result.count(str(x)))
    print(counts[x])