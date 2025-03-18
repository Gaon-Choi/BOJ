matrix = []
result = 0

for _ in range(8):
    matrix.append(list(input()))
    
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'F' and (i + j) % 2 == 0:
            result += 1
            
print(result)