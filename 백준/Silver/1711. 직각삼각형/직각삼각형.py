import sys

n = int(sys.stdin.readline())

points = []
cnt = 0

for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            b = (points[j][0] - points[k][0]) ** 2 + (points[j][1] - points[k][1]) ** 2
            c = (points[k][0] - points[i][0]) ** 2 + (points[k][1] - points[i][1]) ** 2
            
            if a + b == c or a + c == b or b + c == a:
                cnt += 1
                
print(cnt)