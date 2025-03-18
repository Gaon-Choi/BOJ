a=int(input())
b=input()
b=b.split()
for x in range(0, a):
    b[x]=int(b[x])
b.sort()
print(b[0]*b[a-1])