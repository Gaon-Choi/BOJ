import sys

num = int(sys.stdin.readline())

points = list()

for _ in range(num):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x, y])

points.sort(key = lambda x: (x[0], x[1]))

for elem in points:
    print(elem[0], elem[1])