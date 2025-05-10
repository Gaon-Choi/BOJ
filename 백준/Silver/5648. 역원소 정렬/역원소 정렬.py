import sys

res = []

flag = True

for line in sys.stdin:
    arr = line.strip().split()

    if not arr:
        continue

    if flag:
        arr = arr[1:]
        flag = False

    for elem in arr:
        temp = ""

        for c in elem[-1::-1]:
            if temp == "" and c == "0":
                continue
            temp += c

        res.append(int(temp))

for num in sorted(res):
    print(num)