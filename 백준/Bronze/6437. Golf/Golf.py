idx = 1

while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    print(f"Hole #{idx}")

    if b == 1:
        print("Hole-in-one.")

    else:
        diff = a - b

        if diff == 3:       print("Double eagle.")
        elif diff == 2:     print("Eagle.")
        elif diff == 1:     print("Birdle.")
        elif diff == 0:     print("Par.")
        elif diff == -1:    print("Bogey.")
        else:               print("Double Bogey.")

    print()
    idx += 1
    