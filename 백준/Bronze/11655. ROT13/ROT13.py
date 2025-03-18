text = input()

result = str()

for c in text:
	if c.isalpha():
		if ord('A') <= ord(c) and ord(c) <= ord('Z'):
			result += chr(ord('A') + (ord(c) + 13 - ord('A')) % 26)
		else:
			result += chr(ord('a') + (ord(c) + 13 - ord('a')) % 26)
	else:
		result += c

print(result)