if __name__ == '__main__':
    a, b, c = (input()).split()
    a, b, c = int(a), int(b), int(c)
    if (a == b and b == c):
        print(10000+a*1000)
    elif a == b and a != c:
        print(1000+a * 100)
    elif a == c and a != b:
        print(1000 + a * 100)
    elif b == c and a != c:
        print(1000 + b * 100)
    else:
        print(max(a, b, c) * 100)
