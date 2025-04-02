num = 2

while True:
    word = input()

    if word == "Was it a cat I saw?":
        break

    result = ""

    for idx, c in enumerate(word):
        if idx % num == 0:
            result += c

    print(result)

    num += 1