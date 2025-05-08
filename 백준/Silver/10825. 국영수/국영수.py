import sys
input = sys.stdin.readline

n = int(input())

datas = []

for _ in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    datas.append((name, a, b, c))

datas.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for data in datas:
    print(data[0])