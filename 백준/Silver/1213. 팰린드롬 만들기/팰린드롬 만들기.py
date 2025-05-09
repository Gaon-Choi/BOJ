import sys
input = sys.stdin.readline

text = input().strip()

arr = [0] * 100

A = ord('A')

for c in text:
    arr[ord(c) - A] += 1

flag = 0
mid = ""
ans = ""

for i in range(ord('Z') - ord('A'), -1, -1):
    if arr[i] % 2 == 1:
        flag += 1
        mid = chr(i + ord('A'))
        arr[i] -= 1

    if flag >= 2:
        break

    for _ in range(arr[i] // 2):
        ans = chr(i + ord('A')) + ans + chr(i + ord('A'))

if len(mid) > 0:
    insert_idx = len(ans) // 2
    ans = ans[:insert_idx] + mid + ans[insert_idx:]

if flag >= 2:
    print("I\'m Sorry Hansoo")
else:
    print(ans)