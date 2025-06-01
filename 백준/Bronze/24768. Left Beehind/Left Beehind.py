import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    if a + b == 13:
        print("Never speak again.")
    else:
        if a > b:
            print("To the convention.")
        elif a == b:
            print("Undecided.")
        else:
            print("Left beehind.")
