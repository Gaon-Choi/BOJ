t=input()
t=t.split()
x=int(t[0]);y=int(t[1]);z=int(t[2])
print((x+y)%z)
print((x%z+y%z)%z)
print((x*y)%z)
print(((x%z)*(y%z))%z)