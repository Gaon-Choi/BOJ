import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
    
arr.sort(reverse=True)

for elem in arr:
    print(elem)