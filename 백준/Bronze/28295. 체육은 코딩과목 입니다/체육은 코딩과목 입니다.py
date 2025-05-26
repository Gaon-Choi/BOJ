direction = ["N", "E", "S", "W"]

dirr = 0

for _ in range(10):
    t = int(input())

    if t == 1:
        dirr += 1
    elif t == 3:
        dirr -= 1
    else:
        dirr += 2

while dirr < 0:
    dirr += 4

print(direction[dirr % 4])