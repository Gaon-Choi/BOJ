def rev(x):
	reversed = str(x)[-1::-1]
	
	result = 0
	w = len(reversed) - 1
	for c in range(len(reversed)):
		result += (10 ** w) * int(reversed[c])
		w -= 1

	return result

X, Y = map(int, input().split())

print(rev(rev(X) + rev(Y)))