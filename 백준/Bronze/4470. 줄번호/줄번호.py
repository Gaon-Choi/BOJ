import sys
input = sys.stdin.readline

n = int(input())

for line in range(1, n + 1):
    text = input().rstrip()

    print(f"{line}. {text}")