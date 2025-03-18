N = int(input())

result = []

for _ in range(N):
	n, m = map(int, input().split())
	total = 0
	for i in range(n, m + 1):
		total += str(i).count('0')
	result.append(total)

for elem in result:
    print(elem)