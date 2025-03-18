word = input()

min_word = 'z' * 50

for i in range(1, len(word) - 1):
	for j in range(i+1, len(word)):
		one = (word[:i])[-1::-1]
		two = (word[i:j])[-1::-1]
		three = (word[j:])[-1::-1]
		
		min_word = min([min_word, one + two + three])

print(min_word)
		