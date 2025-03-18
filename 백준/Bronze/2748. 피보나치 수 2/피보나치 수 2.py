fibbo = [0, 1]

n = int(input())

for _ in range(n):
	fibbo.append(fibbo[-1] + fibbo[-2])

print(fibbo[n])