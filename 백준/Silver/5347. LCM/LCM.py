def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    ans = 1

    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i

    return ans


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))