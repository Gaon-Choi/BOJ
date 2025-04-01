num = int(input())

while True:
    n = int(input())

    if n == 0:
        break

    if n % num == 0:
        print(n, " is a multiple of ", num, ".", sep="")
    else:
        print(n, " is NOT a multiple of ", num, ".", sep="")