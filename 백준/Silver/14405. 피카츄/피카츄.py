import sys
input = sys.stdin.readline

text = input().strip()

arr = []

for c in text:
    arr.append(c)

    if len(arr) >= 3:
        if arr[:3] in [["c", "h", "u"]]:
            arr.pop()
            arr.pop()
            arr.pop()

    elif len(arr) >= 2:
        if arr[:2] in [["p", "i"], ["k", "a"]]:
            arr.pop()
            arr.pop()

if arr:
    print("NO")
else:
    print("YES")