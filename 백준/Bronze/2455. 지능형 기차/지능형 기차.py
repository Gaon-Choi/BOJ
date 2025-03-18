import sys

arr = []

curr = 0

for _ in range(4):
    off, on = map(int, sys.stdin.readline().split())
    
    curr -= off
    arr.append(curr)
    
    curr += on
    arr.append(curr)
    
print(max(arr))