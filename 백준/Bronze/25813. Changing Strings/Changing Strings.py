import sys
input = sys.stdin.readline

word = list(input().strip())

f_idx, u_idx = 0, 0

size = len(word)

for i in range(size):
    if word[i] == 'U':
        u_idx = i
        break

for i in range(size):
    if word[size - i - 1] == 'F':
        f_idx = size - i - 1
        break

for i in range(u_idx):
    word[i] = "-"

for i in range(u_idx + 1, f_idx):
    word[i] = "C"

for i in range(f_idx + 1, size):
    word[i] = "-"

print("".join(word))
