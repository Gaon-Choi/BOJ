if __name__ == '__main__':
    result = list()
    while True:
        a, b = (input()).split()
        a = int(a); b = int(b)
        # check it first (for ZeroDivisionError)
        if (a == 0 and b == 0): break
        if b % a == 0:
            result.append('factor')    # factor
        elif a % b == 0:
            result.append('multiple')    # multiple
        else:
            result.append('neither')   # neither

    for elem in result:
        print(elem)