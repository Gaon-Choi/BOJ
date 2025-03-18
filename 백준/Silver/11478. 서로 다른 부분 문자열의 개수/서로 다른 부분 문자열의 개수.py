word = input()

sub_string = dict()

for i in range(len(word)):
	for j in range(i, len(word)):
		if word[i:j+1] not in sub_string:
			sub_string[word[i:j+1]] = 1

print(len(sub_string))