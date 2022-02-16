# Gaon Choi

def _sum_(mystack):
    SUM = 0
    for i in mystack:
        SUM += i
    return SUM


if __name__ == '__main__':
    mystack = list()
    iter = int(input())
    for x in range(iter):
        num = int(input())
        if num != 0:
            mystack.append(num)
        else: mystack.pop()
    print(_sum_(mystack))