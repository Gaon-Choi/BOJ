import sys
input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    arr = []
    max_height = 0

    idx = 0

    for _ in range(n):
        name, height = input().strip().split()
        height = float(height)
        max_height = max(max_height, height)
        arr.append((name, height))

    for elem in arr:
        if elem[1] == max_height:
            print(elem[0], end = " ")

    print()
