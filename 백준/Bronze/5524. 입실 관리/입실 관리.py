N = int(input())

arr = []

for _ in range(N):
	text = input()
	arr.append(text.lower())

for elem in arr:
	print(elem)