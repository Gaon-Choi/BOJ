N = int(input())

result = []

for _ in range(N):
	sentence = input()
	result.append(sentence[0].upper() + sentence[1:])

for elem in result:
	print(elem)