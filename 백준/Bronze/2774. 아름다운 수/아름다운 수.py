n = int(input())
result = []

for _ in range(n):
    num = set(list(input()))
    result.append(len(num))
    
for elem in result:
    print(elem)