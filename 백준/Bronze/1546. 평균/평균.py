num=int(input())
a=input()
a=a.split()
for x in range(0, num):
    a[x]=int(a[x])
a.sort(reverse=True)
max=int(a[0])
sum=0
for x in range(0, num):
    sum+=(int(a[x])/max)*100
print(sum/num)