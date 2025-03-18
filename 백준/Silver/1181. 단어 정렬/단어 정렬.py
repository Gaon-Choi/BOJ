import sys

n = int(sys.stdin.readline())

words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip())
    
words = list(set(words))
    
words.sort(key=lambda x : (len(x), x))

for elem in words:
    print(elem)