result = []

while True:
	boy, girl = map(int, input().split())

	if boy == 0 and girl == 0:
		break

	result.append(boy + girl)

for elem in result:
	print(elem)