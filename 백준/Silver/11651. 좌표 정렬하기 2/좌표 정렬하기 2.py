points = list()

num = int(input())
for _ in range(num):
    a, b = map(int, (input()).split())
    points.append([b, a])

points = sorted(points)
for y, x in points:
    print(x,y)