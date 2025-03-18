def transform_num(n):
	converted_num = 0

	for c in str(n):
		converted_num += int(c)

	return converted_num

X = int(input())
cnt = 0

while True:
	if X < 10:
		break
	X = transform_num(X)
	cnt += 1
	

print(cnt)
print("YES" if X in [3, 6, 9] else "NO")