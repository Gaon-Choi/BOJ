import sys
input = sys.stdin.readline

def collatz(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

n = int(input())

result = [n]

while n != 1:
    n = collatz(n)

    result.append(n)

    if n == 1:
        break

for res in result:
    print(res, end = " ")
