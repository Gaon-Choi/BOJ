def game(a):
    a=a.split()
    for x in range(0,5):
        a[x]=int(a[x])
    a.sort()
    total=a[1]+a[2]+a[3]
    if a[3]-a[1]>=4:
        return "KIN"
    else: return total

group=[]
n=int(input())
i=1
while i<=n:
    group.append(game(input()))
    i+=1
for u in range(0,n):
    print(group[u])