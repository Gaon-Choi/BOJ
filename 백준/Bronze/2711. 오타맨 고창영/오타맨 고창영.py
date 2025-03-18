T = int(input())

result = []

for _ in range(T):
	idx, word = input().split()
	idx = int(idx) - 1
	result.append(word[0:idx] + word[idx+1:])


for elem in result:
	print(elem)