n = int(input())

for _ in range(n):
	arr = list(map(int, input().split()))
	arr.sort()	# 정렬
	print(arr[-3])