result = []

while True:
	text = input()
	if text == "#":
		break

	text = text.lower()
	
	temp = 0

	temp += text.count("a")
	temp += text.count("e")
	temp += text.count("i")
	temp += text.count("o")
	temp += text.count("u")

	result.append(temp)

for elem in result:
	print(elem)