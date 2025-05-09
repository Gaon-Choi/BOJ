import sys
input = sys.stdin.readline

p = int(input())

watt, volt = map(int, input().split())

print(1 if (watt // volt >= p) else 0)