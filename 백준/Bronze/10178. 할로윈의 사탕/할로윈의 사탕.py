n = int(input())

result = []

for _ in range(n):
	c, v = map(int, input().split())
	result.append((c // v, c % v))

for elem in result:
	print("You get {p} piece(s) and your dad gets {r} piece(s).".format(p=elem[0], r = elem[1]))