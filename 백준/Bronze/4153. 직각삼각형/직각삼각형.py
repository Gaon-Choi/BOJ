def check(a, b, c):
    A = (a**2 + b**2 == c**2)
    B = (a**2 + c**2 == b**2)
    C = (b**2 + c**2 == a**2)
    return A or B or C

if __name__ == '__main__':
    boolean = list()
    while True:
        a, b, c = (input()).split()
        a=int(a); b=int(b); c=int(c)
        if a == b == c == 0:
            break
        else:
            boolean.append(check(a, b, c))
    for iter in boolean:
        if iter is True: print("right")
        else: print("wrong")