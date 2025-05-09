import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, list(input().strip()))))

def go(x, y, size):
    flag = True

    prev = arr[x][y]

    for nx in range(x, x + size):
        for ny in range(y, y + size):
            if arr[nx][ny] != prev:
                flag = False
                break
        if not flag:
            break

    if flag:
        return str(prev)

    return "(" + go(x, y, size // 2) + go(x, y + size // 2, size // 2) + go(x + size // 2, y, size // 2) + go(x + size // 2, y + size // 2, size // 2) + ")"

print(go(0, 0, n))