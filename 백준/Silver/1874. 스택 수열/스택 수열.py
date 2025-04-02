n = int(input())

stack = []
num = 1

flag = False

is_possible = True
result = []

for _ in range(n):
    elem = int(input())

    while num <= elem:
        stack.append(num)
        result.append("+")
        num += 1

    if stack and stack[-1] == elem:
        stack.pop()
        result.append("-")
    else:
        is_possible = False
        break
    

if is_possible:
    print(*result, sep="\n")
else:
    print("NO")