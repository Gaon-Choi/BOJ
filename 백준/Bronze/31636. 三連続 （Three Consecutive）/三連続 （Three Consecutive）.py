import sys
input = sys.stdin.readline

n = int(input())
text = input().strip()

cnt = 0

flag = False

for c in text:
    if c == "o":
        cnt += 1
    else:
        cnt = 0

    if cnt == 3:
        flag = True
        print("Yes")
        break

if not flag:
    print("No")
    