arr = [0] * 10

text = input()

for c in text:
    num = int(c)

    if num in {6, 9}:
        arr[6] += 1
    else:
        arr[num] += 1
arr[6] = (arr[6] + 1) // 2
print(max(arr))