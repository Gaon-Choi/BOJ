import sys
input = sys.stdin.readline

n = int(input())

hash = dict()

for _ in range(n):
    key, value = input().split()
    hash[value] = key

text = input()
ans = ""

stk = []

for c in text:
    stk.append(c)
    
    temp = "".join(stk)
    
    if temp in hash:
        ans += hash[temp]
        stk = []
        
print(ans)