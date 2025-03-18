T = int(input())
result = []

for _ in range(T):
	N = int(input())
	scores = dict()
	for _ in range(N):
		univ, score = input().split()
		score = int(score)

		scores[univ] = score

	result.append(max(scores, key=scores.get))

for elem in result:
	print(elem)