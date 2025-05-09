import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

print("F" if 9 in arr else "S")