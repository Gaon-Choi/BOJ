n=int(input())
a=0;b=0
group=[]
for _ in range(n):
    group.append(int(input()))
for x in range(n):
    if group[x]==0:
        a+=1
    else: b+=1
if a>b: print("Junhee is not cute!")
else: print("Junhee is cute!")