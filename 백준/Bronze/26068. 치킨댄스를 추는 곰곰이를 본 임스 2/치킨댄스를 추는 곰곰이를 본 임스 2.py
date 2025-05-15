import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

for _ in range(n):
    text = input().strip()

    if int(text[2:]) <= 90:
        cnt += 1

print(cnt)