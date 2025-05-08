import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = input()

stk = []

for i in range(n):
    while stk and int(stk[-1]) < int(number[i]) and k > 0:
        stk.pop()
        k -= 1

    stk.append(number[i])

if k == 0:
    print("".join(stk))
else:
    print("".join(stk[:-k]))