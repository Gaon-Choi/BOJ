import sys
input = sys.stdin.readline

text = input().strip()

result = ""

cnt = 0

for c in text:
    if c == ".":
        while cnt != 0:
            if cnt - 4 >= 0:
                result += "AAAA"
                cnt -= 4
            elif cnt - 2 >= 0:
                result += "BB"
                cnt -= 2
            else:
                print(-1)
                exit(0)

        result += c

    else:
        cnt += 1

while cnt != 0:
    if cnt - 4 >= 0:
        result += "AAAA"
        cnt -= 4
    elif cnt - 2 >= 0:
        result += "BB"
        cnt -= 2
    else:
        print(-1)
        exit(0)

print(result)
