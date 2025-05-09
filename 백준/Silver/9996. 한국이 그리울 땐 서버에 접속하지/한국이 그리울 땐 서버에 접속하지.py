import sys
input = sys.stdin.readline

n = int(input())

regex = input().strip()

prefix, postfix = regex.split("*")

min_size = len(prefix) + len(postfix)

for _ in range(n):
    text = input().strip()

    if len(text) < min_size:
        print("NE")
        continue

    if text[:len(prefix)] == prefix and text[-len(postfix):] == postfix:
        print("DA")
    else:
        print("NE")