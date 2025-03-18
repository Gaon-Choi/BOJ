arr = []

for _ in range(9):
	arr.append(list(map(int, input().split())))

max_i = 0
max_j = 0
max_elem = -1

for i in range(9):
	for j in range(9):
		if arr[i][j] > max_elem:
			max_elem = arr[i][j]
			max_i = i + 1
			max_j = j + 1

print(max_elem)
print(max_i, max_j)