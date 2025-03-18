N = int(input())

result = []

for _ in range(N):
	name, dd, mm, yyyy = input().split()
	dd = int(dd); mm = int(mm); yyyy = int(yyyy)

	result.append([name, yyyy * 10000 + mm * 100 + dd])

result.sort(key = lambda x: x[1])

print(result[-1][0])
print(result[0][0])