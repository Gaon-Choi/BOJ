n = int(input())
gap = n - 1

for i in range(n):
	print(" " * gap, "* " * (i + 1), sep="")
	gap -= 1