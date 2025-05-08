import sys
input = sys.stdin.readline

def is_valid(x, y, num):

    for i in range(9):
        if arr[x][i] == num:
            return False
        
    for j in range(9):
        if arr[j][y] == num:
            return False
        
    nx, ny = (x // 3) * 3, (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if arr[nx + i][ny + j] == num:
                return False
            
    return True

arr = []
blanks = []

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] == 0:
            blanks.append((i, j))

    arr.append(row)

def solve(idx):
    if idx == len(blanks):
        for row in arr:
            print(*row)
        exit(0)

    x, y = blanks[idx]

    for num in range(1, 10):
        if is_valid(x, y, num):
            arr[x][y] = num
            solve(idx + 1)
            arr[x][y] = 0

solve(0)