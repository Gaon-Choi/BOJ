import sys
input = sys.stdin.readline

text = ""

while True:
    tmp = input()
    if tmp == "":
        break
    
    text += tmp
  
words = dict()
    
for c in text:
    if not c.isalpha():
        continue
    if c in words:
        words[c] += 1
    else:
        words[c] = 1

tmp = -1

for key, value in list(words.items()):
    if value > tmp:
        tmp = value
        
words = list(sorted(list(words.items()), key = lambda x: x[0]))

for elem in words:
    if elem[1] == tmp:
        print(elem[0], end="")