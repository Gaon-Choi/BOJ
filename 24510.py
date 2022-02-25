ans = list()

num = int(input())
for _ in range(num):
    elem = 0
    text = input()
    for i in range(len(text)-2):
        if text[i:i+3] == 'for':
            elem += 1
        if text[i:i+5] == 'while':
            elem += 1
    ans.append(elem)
print(max(ans))