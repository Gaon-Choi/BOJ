a=set()
for x in range(1,31):
    a.add(x)
for x in range(28):
    i=int(input())
    a.remove(i)
print(min(a), max(a), sep='\n', end='')