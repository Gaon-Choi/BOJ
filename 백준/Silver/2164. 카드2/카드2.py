n = int(input())

arr = list(range(1, n + 1))
cnt = n
bottom = -1

while cnt != 1:
	bottom += 1
	cnt -= 1
	if cnt >= 1:
	    bottom += 1
	    elem = arr[bottom]
	    arr.append(elem)

print(arr[bottom])