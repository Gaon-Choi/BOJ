cases = int(input())
anss = list()
for _ in range(cases):
    string = input()
    list_ = string.split()
    num = list_[0]
    list_.remove(num)
    num=float(num)
    for i in range(len(list_)):
        if list_[i] == '@': num *= 3
        if list_[i] == '%': num += 5
        if list_[i] == '#': num -= 7
    anss.append(num)
for x in anss:
    print("{:.2f}".format(x))