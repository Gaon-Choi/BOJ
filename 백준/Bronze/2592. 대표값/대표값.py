arr = []
hash = dict()

for _ in range(10):
	elem = int(input())
	arr.append(elem)
	if elem in hash:
		hash[elem] += 1
	else:
		hash[elem] = 1

print(sum(arr) // 10)
print(max(hash, key=hash.get))