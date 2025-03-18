text = input()

arr = []

for i in range(len(text)):
	arr.append(text[i:])

arr.sort()

for elem in arr:
	print(elem)