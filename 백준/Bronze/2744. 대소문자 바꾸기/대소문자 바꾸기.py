text = input()
result = []

for c in text:
	if c.islower():
		result.append(c.upper())
	else:
		result.append(c.lower())

print(''.join(result))