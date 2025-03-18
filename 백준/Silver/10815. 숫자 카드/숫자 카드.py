n = int(input())
arr1 = dict(zip(list(map(int, input().split())), [0] * n))

m = int(input())
arr2 = list(map(int, input().split()))

result = []

for elem in arr2:
	result.append(1 if elem in arr1 else 0)

for elem in result:
	print(elem, end=" ")