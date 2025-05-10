import sys
input = sys.stdin.readline

text = input().strip()

if ("M" in text) and ("O" in text) and ("B" in text) and ("I" in text) and ("S" in text):
    print("YES")
else:
    print("NO")