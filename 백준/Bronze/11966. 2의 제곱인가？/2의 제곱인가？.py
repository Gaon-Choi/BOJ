arr = [1]

for i in range(30):
	arr.append(arr[-1] * 2)

n = int(input())

print(1 if n in arr else 0)