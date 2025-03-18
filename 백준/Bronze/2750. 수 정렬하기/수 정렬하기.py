n = int(input())

arr = []

for _ in range(n):
	arr.append(int(input()))

arr.sort()

for elem in arr:
	print(elem)