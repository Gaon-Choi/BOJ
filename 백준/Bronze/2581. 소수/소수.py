import math

def is_prime(n):
	if n <= 1:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False

	return True

M = int(input())
N = int(input())

min_prime = 0
sum_prime = 0

for num in range(M, N + 1):
	if is_prime(num):
		if min_prime == 0:
			min_prime = num
		sum_prime += num

if min_prime == 0:
	print(-1)
else:
	print(sum_prime)
	print(min_prime)