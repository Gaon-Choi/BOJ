arr = []

for _ in range(9):
	arr.append(int(input()))

arr.sort()
total_sum = sum(arr)

answer = []

for i in range(9):
	for j in range(i + 1, 9):
		if arr[i] + arr[j] == total_sum - 100:
			answer = [i, j]

for idx, elem in enumerate(arr):
	if idx not in answer:
		print(elem)