n = int(input())
arr = []
idx = 0

for _ in range(n):
	age, name = input().split()
	age = int(age)
	arr.append([age, name, idx])
	idx += 1

arr.sort(key=lambda x : (x[0], x[2]))

for elem in arr:
	print(elem[0], elem[1])