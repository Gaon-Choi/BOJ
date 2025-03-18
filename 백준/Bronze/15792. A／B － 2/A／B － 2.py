a, b = map(int, input().split())

answer = ""

answer += str(int(a // b)) + "."

for _ in range(1001):
    a -= (a // b) * b
    a *= 10
    answer += str(int(a // b))
    
print(answer)