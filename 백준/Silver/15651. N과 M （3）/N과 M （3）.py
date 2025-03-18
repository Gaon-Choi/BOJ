def combination(arr, k):
	result = []

	def backtrack(start, path):
		if len(path) == k:
			result.append(path[:])
			return

		for i in range(start, len(arr)):
			path.append(arr[i])
			backtrack(0, path)
			path.pop()
	
	backtrack(0, [])
	return result

N, M = map(int, input().split())

arr = list(range(1, N + 1))

result = combination(arr, M)

for elem in result:
	print(" ".join(map(str, elem)))