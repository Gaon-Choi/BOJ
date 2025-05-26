import sys
input = sys.stdin.readline

n = int(input())
text = input().strip()

print(text[n - 5:])