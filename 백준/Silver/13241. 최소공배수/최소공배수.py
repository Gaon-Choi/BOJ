import sys
input = sys.stdin.readline

def gcd(a, b):
    ans = 1

    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i

    return ans

a, b = map(int, input().split())

gcd = gcd(a, b)

print(a * b // gcd)