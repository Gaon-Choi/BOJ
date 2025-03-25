import math

n = int(input())

iroot = math.isqrt(n)

if iroot ** 2 != n:
    iroot += 1

print(iroot)