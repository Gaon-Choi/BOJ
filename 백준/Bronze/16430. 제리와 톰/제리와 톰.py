def gcd(m, n):
	answer = 1
	for i in range(1, min(m, n) + 1):
		if m % i == 0 and n % i == 0:
			answer = i

	return answer

a, b = map(int, input().split())
answer = gcd(b - a, b)

print((b - a) // answer, b // answer)