import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b // gcd(a, b)

A, B, T = map(int, input().split())

print("yes" if (lcm(A, B) <= T) else "no")
