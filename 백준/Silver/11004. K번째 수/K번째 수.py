text=input()
text=text.split()
a, b=int(text[0]), int(text[1])
series=input()
series=series.split()
for x in range(a):
    series[x]=int(series[x])
series.sort()
print(series[b-1])