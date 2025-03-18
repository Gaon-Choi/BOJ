text = input()

num = 0

for t in text:
	if t in ["a", "e", "i", "o", "u"]:
		num += 1

print(num)