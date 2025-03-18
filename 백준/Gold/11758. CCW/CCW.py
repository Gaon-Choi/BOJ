p1x, p1y = map(int, input().split())    # a
p2x, p2y = map(int, input().split())    # b
p3x, p3y = map(int, input().split())    # c

ab = [p2x - p1x, p2y - p1y]
bc = [p3x - p2x, p3y - p2y]

ccw = ab[0] * bc[1] - ab[1] * bc[0]

if ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)