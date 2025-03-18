a=input()
a=a.split()
n=int(a[0]);num=int(a[1])
b=input()
b=b.split()
for x in range(0,n):
    b[x]=int(b[x])
group=[]
i=0
while i<n:
    if b[i]<num:group.append(b[i])
    i+=1
for u in range(0,len(group)):
    print(group[u],end=" ")