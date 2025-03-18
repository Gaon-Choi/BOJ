a=input()
a=a.split()
num_1=int(a[0]);num_2=int(a[1])
if num_1==num_2:
    print("==")
elif num_1>num_2:
    print(">")
else: print("<")