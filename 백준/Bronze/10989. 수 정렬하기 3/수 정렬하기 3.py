import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * 10001

for _ in range(N):
	elem = int(input())
	arr[elem] += 1

for num, v in enumerate(arr):
    for _ in range(v):
        print(num)