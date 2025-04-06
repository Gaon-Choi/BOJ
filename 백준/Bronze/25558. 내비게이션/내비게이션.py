import math

def find_cost(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

n = int(input())

s1, s2, e1, e2 = map(int, input().split())

min_idx = 0
min_cost = math.inf

for num in range(n):
    t = int(input())

    arr = []

    for _ in range(t):
        arr.append(list(map(int, input().split())))

    arr = [[s1, s2]] + arr + [[e1, e2]]

    total_cost = 0

    for i in range(len(arr) - 1):
        total_cost += find_cost(arr[i], arr[i + 1])

    if min_cost > total_cost:
        min_cost = total_cost
        min_idx = num + 1

print(min_idx)