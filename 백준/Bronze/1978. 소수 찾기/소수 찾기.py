def is_prime(n):
	if n == 1:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False
	return True

N = int(input())
arr = list(map(int, input().split()))

total = 0
for elem in arr:
	if is_prime(elem):
		total += 1

print(total)