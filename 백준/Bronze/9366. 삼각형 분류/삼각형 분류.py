def is_triangle(a, b, c):
    hypotenuse = max(a, b, c)
    remain = sum([a, b, c]) - hypotenuse
    
    if remain > hypotenuse:
        return True
    else:
        return False
        
result = []

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if not is_triangle(a, b, c):
        result.append("invalid!")
    else:
        if a == b and b == c and c == a:
            result.append("equilateral")
        elif (a == b) or (b == c) or (c == a):
            result.append("isosceles")
        else:
            result.append("scalene")

for idx, elem in enumerate(result):
    print("Case #{idx}: {elem}".format(idx=idx+1, elem=elem))