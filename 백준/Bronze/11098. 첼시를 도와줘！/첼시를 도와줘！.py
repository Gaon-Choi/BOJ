N = int(input())

result = []

for _ in range(N):
	team = int(input())
	max_score = -1
	maxima = None
	for _ in range(team):
		C, name = input().split()
		C = int(C)
		max_score = max(max_score, C)
		if max_score == C:
			maxima = name

	result.append(maxima)

for elem in result:
	print(elem)