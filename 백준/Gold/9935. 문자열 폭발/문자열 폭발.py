stack = []

word = input()
bomb_word = input()
bomb_size = len(bomb_word)

size = 0

for c in word:
    if size >= bomb_size:
        if ''.join(stack[-bomb_size:]) == bomb_word:
            for _ in range(bomb_size):
                stack.pop()
                size -= 1

    stack.append(c)
    size += 1

if size >= bomb_size:
    if ''.join(stack[-bomb_size:]) == bomb_word:
        for _ in range(bomb_size):
            stack.pop()
            size -= 1

if stack:
    print("".join(stack))
else:
    print("FRULA")