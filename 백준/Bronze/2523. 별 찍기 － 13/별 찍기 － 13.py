n = int(input())

for star in range(1, n + 1):
	print("*" * star)

for star in range(n-1, -1, -1):
	print("*" * star)