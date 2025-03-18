import sys
n=int(sys.stdin.readline())
x=1
group=[]
while x<=n:
    s=sys.stdin.readline()
    s=s.split()
    s[0]=int(s[0]);s[1]=int(s[1])
    group.append(int(2+s[1]-s[0]))
    x+=1
for x in range(0,n):
    print(group[x])