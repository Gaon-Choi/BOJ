import sys
input = sys.stdin.readline

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

#az + bx = cx
#ay * by = cy
#ax + bz = cz

print(cx - az, cy // ay, cz - ax)