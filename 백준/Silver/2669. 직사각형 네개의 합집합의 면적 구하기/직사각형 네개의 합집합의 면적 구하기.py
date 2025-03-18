arr = [[False for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, (input()).split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x-1][y-1] = True
area = 0
for X in range(100):
    for Y in range(100):
        if arr[X][Y]:
            area += 1

print(area)