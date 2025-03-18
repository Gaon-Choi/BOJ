def youngsik(t: int):
	return ((t // 30) + 1) * 10

def minsik(t: int):
	return ((t // 60) + 1) * 15

n = int(input())
arr = list(map(int, input().split()))

M = 0; Y = 0;

for elem in arr:
	M += minsik(elem)
	Y += youngsik(elem)

if M > Y:
	print("Y", Y)
elif M == Y:
	print("Y M", Y)
else:
	print("M", M)