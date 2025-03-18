m, n = map(int, input().split())
mat = [list(map(int, input().rstrip())) for _ in range(m)]
size = 1
maxima = 1
while (size <= min(m,n)):
    flag = False
    for i in range(n-size+1):
        for j in range(m-size+1):
            if ((mat[j][i] == mat[j+size-1][i]) and (mat[j][i] == mat[j][i+size-1])) and mat[j][i] == mat[j+size-1][i+size-1]:
                flag = True
    if flag: maxima = size
    size += 1
print(maxima**2)
