n = int(input())

result = []

for _ in range(n):
    temp = []
    total = int(input())
    temp.append(total // 25)
    total = total % 25
    
    temp.append(total // 10)
    total = total % 10
    
    temp.append(total // 5)
    total = total % 5
    
    temp.append(total)
    
    result.append(temp)
    
for elem in result:
    print(" ".join(map(str, elem)))