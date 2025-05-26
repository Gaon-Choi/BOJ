total = 0

a, b = input().split()

a = a[-1::-1]
b = b[-1::-1]

for power, val in enumerate(a):
    total += (2 ** power) * int(val)

for power, val in enumerate(b):
    total += (2 ** power) * int(val)

res = ""

while total != 0:
    res += str(total % 2)
    total = total // 2

res = res[-1::-1]

while len(res) > 0 and res[0] == "0":
    res = res[1:]

if res == "":
    res += "0"
    
print(res)
