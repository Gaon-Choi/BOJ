import sys

def gcd(a, b):
    ans = 1
    
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
            
    return ans

m, n = map(int, sys.stdin.readline().split(":"))

gcd_mn = gcd(m, n)

print(str(m // gcd_mn) + ":" + str(n // gcd_mn), sep="")