import sys

N = int(input())
arr = []

for _ in range(N):
	arr.append(int(sys.stdin.readline()))

arr.sort()

for elem in arr:
	print(elem)