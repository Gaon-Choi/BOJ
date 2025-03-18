n = int(input())

result = []

for step in range(n):
	arr = list(map(int, input().split()))
	arr.pop(0)
	arr.sort()

	largest_gap = 0

	for i in range(len(arr) - 1):
		largest_gap = max(largest_gap, abs(arr[i+1]-arr[i]))

	result.append([max(arr), min(arr), largest_gap])

for step, elem in enumerate(result):
	print("Class {step}".format(step=step + 1))
	print("Max {maxima}, Min {minima}, Largest gap {lgap}".format(maxima=elem[0], minima=elem[1], lgap=elem[2]))