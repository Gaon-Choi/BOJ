num, base = map(int, input().split())

arr = list(map(str, range(0, 10)))

for i in range(ord('A'), ord('Z') + 1):
    arr.append(chr(i))

res = []

while num != 0:
    res.append(arr[num % base])
    num = num // base

res.reverse()

print("".join(res))