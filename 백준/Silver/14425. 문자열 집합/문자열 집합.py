import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hash = dict()

for _ in range(n):
    hash[input()] = 1
    
count = 0

for _ in range(m):
    word = input()
    
    if word in hash:
        count += 1
        
print(count)