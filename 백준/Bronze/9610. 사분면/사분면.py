q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

n = int(input())

for _ in range(n):
	x, y = map(int, input().split())
	if x == 0 or y == 0:
		axis += 1
	elif x > 0:
		if y > 0:
			q1 += 1
		else:
			q4 += 1
	else:
		if y > 0:
			q2 += 1
		else:
			q3 += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)