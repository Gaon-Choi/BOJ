def lcm(a, b):
	return (a * b) // gcd(a, b)

def gcd(a, b):
	num = 1
	for i in range(1, min(a, b) + 1):
		if a % i == 0 and b % i == 0:
			num = i
	return num

n = int(input())
result = []

for _ in range(n):
	a, b = map(int, input().split())
	result.append(lcm(a, b))

for elem in result:
	print(elem)