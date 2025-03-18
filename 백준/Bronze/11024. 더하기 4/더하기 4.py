n = int(input())
result = []

for _ in range(n):
	result.append(sum(list(map(int, input().split()))))

for elem in result:
	print(elem)