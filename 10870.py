def fib(th):
    if th == 0:
        return 0
    elif th == 1:
        return 1
    else:
        return fib(th-1) + fib(th-2)

num = int(input())
print(fib(num))