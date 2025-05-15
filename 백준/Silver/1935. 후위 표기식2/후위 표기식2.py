import sys
input = sys.stdin.readline

n = int(input())

expression = input().strip()

hash_ = dict()

for i in range(n):
    hash_[chr(ord('A') + i)] = int(input())

stk = []

for token in expression:
    if token == "*":
        e1, e2 = stk.pop(), stk.pop()
        stk.append(e1 * e2)
    elif token == "/":
        e1, e2 = stk.pop(), stk.pop()
        stk.append(e2 / e1)
    elif token == "+":
        e1, e2 = stk.pop(), stk.pop()
        stk.append(e1 + e2)
    elif token == "-":
        e1, e2 = stk.pop(), stk.pop()
        stk.append(e2 - e1)
    else:
        stk.append(hash_[token])

print(f"{stk[0]:.2f}")
