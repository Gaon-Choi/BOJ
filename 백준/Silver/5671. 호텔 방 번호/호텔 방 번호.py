import sys
input = sys.stdin.readline

while True:
    line = input()

    if not line:
        break

    a, b = map(int, line.split())

    cnt = 0

    for num in range(a, b + 1):
        set_ = set()
        flag = True

        for c in str(num):
            if c in set_:
                flag = False
                break
            set_.add(c)

        if flag:
            cnt += 1

    print(cnt)
            