n=input()
n=n.split()
a=n[0];b=n[1]
a=list(a);b=list(b)
a_1=a[2]+a[1]+a[0]
b_1=b[2]+b[1]+b[0]
a_1=int(a_1);b_1=int(b_1)
print(max(a_1,b_1))