day=0
inin=input()
inin=inin.split()
x=int(inin[0])
month=[31,28,31,30,31,30,31,31,30,31,30,31]
week=['MON','TUE','WED','THU','FRI','SAT','SUN']
a=0
while a<x-1:
    day+=month[a]
    a+=1
y=int(inin[1])
day+=y
i=1
while i<=7:
    if day%7==0:
        print("SUN")
        break
    if day%7==i:
        print(week[i-1])
    i+=1