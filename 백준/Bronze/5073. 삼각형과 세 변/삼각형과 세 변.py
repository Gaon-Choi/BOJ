result = []

while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    res = list(sorted([a, b, c]))
    if not res[-1] < res[0] + res[1]:
        result.append("Invalid")
        continue
    
    if a == b and b == c and c == a:
        result.append("Equilateral")
    elif a != b and b != c and c != a:
        result.append("Scalene")
    else:
        result.append("Isosceles")
        
for elem in result:
    print(elem)