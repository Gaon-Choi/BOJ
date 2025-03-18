n = int(input())

gap = 0
star = 2 * n - 1

for i in range(n):
	print(" " * gap, "*" * star, sep="")
	gap += 1
	star -= 2

gap -= 2
star += 4

for i in range(n - 1):
	print(" " * gap, "*" * star, sep="")
	gap -= 1
	star += 2