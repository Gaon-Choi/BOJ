a = input()
b = input()

n = len(a)
m = len(b)

matrix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        elif a[i - 1] != b[j - 1]:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            
print(matrix[n][m])

if matrix[n][m] > 0:
    lcs = ""
    
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs += a[i - 1]
            i -= 1; j -= 1
        elif matrix[i][j - 1] > matrix[i - 1][j]:
            j -= 1
        else:
            i -= 1
    
    lcs = lcs[-1::-1]
    
    if len(lcs) > 0:
        print(lcs)