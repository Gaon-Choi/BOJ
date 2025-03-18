N = int(input())

two = 0
five = 0

for i in range(1, N+1):
	while (i > 1):
		if i % 2 == 0:
			two += 1
			i = i // 2
		elif i % 5 == 0:
			five += 1
			i = i // 5
		else:
		    break

print(min(two, five))