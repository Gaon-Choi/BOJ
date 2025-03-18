n = int(input())

arr = list(range(1, n + 1))

result = []

while len(arr) > 0:
    result.append(arr.pop(0))

    if arr:
        elem = arr.pop(0)
        arr.append(elem)

for elem in result:
    print(elem, end = " ")