arr = list(range(1, 21))

for _ in range(10):
	start, end = map(int, input().split())
	start -= 1

	arr = arr[:start] + arr[start:end][-1::-1] + arr[end:]

for elem in arr:
	print(elem, end=" ")