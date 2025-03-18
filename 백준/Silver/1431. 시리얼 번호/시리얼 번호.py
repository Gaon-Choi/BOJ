def calculate_digit_sum(serial):
	total = 0
	for c in serial:
		if c.isdigit():
			total += int(c)

	return total

N = int(input())

arr = []

for _ in range(N):
	arr.append(input())

arr.sort(key = lambda x : (len(x), calculate_digit_sum(x), x))

for elem in arr:
	print(elem)