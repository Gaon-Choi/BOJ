import sys
input = sys.stdin.readline

while True:
    text = input().rstrip()

    if text == ".":
        break

    stk = []

    flag = True

    for c in text:
        if c in {"(", "["}:
            stk.append(c)

        elif c == ")":
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                flag = False
                break

        elif c == "]":
            if stk and stk[-1] == "[":
                stk.pop()
            else:
                flag = False
                break

    if stk:
        flag = False

    print("yes" if flag else "no")
