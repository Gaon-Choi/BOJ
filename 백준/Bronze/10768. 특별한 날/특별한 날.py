month = int(input())
day = int(input())

m = 2
d = 18

result = 0

if month < m:
    result = -1
elif month > m:
    result = +1
else:
    if day < d:
        result = -1
    elif day > d:
        result = +1
    else:
        result = 0
        
print("Before" if result == -1 else "Special" if result == 0 else "After")