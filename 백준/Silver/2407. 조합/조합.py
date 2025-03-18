def fact(n):
    result=1
    for i in range(1, int(n+1)):
        result=result*i
    return result

a=input()
a=a.split()
a_1=int(a[0]);a_2=int(a[1])
print(int(fact(a_1)//(fact(a_2)*fact(a_1-a_2))))