def is_good_word(word):
    stack = []

    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return len(stack) == 0

n = int(input())
cnt = 0

for _ in range(n):
    word = input()

    if is_good_word(word):
        cnt += 1

print(cnt)