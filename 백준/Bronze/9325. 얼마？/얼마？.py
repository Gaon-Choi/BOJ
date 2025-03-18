n = int(input())

result = []

for _ in range(n):
	price = int(input())
	
	k = int(input())

	for _ in range(k):
		q, p = map(int, input().split())
		price += q * p
	
	result.append(price)

for p in result:
	print(p)