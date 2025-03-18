# 배(0), 등(1)

result = ["E", "A", "B", "C", "D"]

for _ in range(3):
	arr = list(map(int, input().split()))
	print(result[arr.count(0)])