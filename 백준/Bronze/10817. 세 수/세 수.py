n=input()
n=n.split()
for x in range(0,3):
    n[x]=int(n[x])
n.sort()
print(n[1])