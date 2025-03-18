arr = []

temp_i = -1
temp_j = -1

for _ in range(9):
	arr.append(int(input()))

total_sum = sum(arr)

flag = False

for i in range(9):
	for j in range(i + 1, 9):
		if total_sum - 100 == arr[i] + arr[j]:
			temp_i = i
			temp_j = j
			flag = True
			break
	if flag:
	    break

answer = []

for idx, elem in enumerate(arr):
	if idx == i or idx == j:
		continue
	
	answer.append(elem)

answer.sort()

for elem in answer:
	print(elem)