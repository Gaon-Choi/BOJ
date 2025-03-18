N, M = map(int, input().split())

m1 = []
m2 = []

for _ in range(N):
	m1.append(list(map(int, input().split())))

for _ in range(N):
	m2.append(list(map(int, input().split())))

result = [[0] * M for _ in range(N)]

for i in range(N):
	for j in range(M):
		result[i][j] = m1[i][j] + m2[i][j]

for i in range(N):
	for j in range(M):
		print(result[i][j], end=" ")
	print()