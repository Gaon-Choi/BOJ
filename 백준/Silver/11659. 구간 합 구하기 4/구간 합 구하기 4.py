N, M = map(int, input().split())

arr = list(map(int, input().split()))

accum_sum = [0]

for i in range(len(arr)):
	accum_sum.append(arr[i] + accum_sum[-1])

result = []

for _ in range(M):
	i, j = map(int, input().split())

	result.append(accum_sum[j] - accum_sum[i - 1])

for elem in result:
	print(elem)