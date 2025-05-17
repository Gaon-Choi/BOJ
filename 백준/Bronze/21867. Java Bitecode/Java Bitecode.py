import sys
input = sys.stdin.readline

n = int(input())
text = input().strip()

java = {"J", "A", "V", "A"}

is_empty = True

for i in range(n):
    if text[i] not in java:
        is_empty = False
        print(text[i], end="")

if is_empty:
    print("nojava")