import sys
input = sys.stdin.readline

cnt = 0

while True:
    text = input().strip()

    if text == "":
        break

    cnt += 1

print(cnt)