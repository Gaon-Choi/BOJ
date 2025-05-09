import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def go(a, b):
    if b == 1:
        return a % c
    
    ret = go(a, b // 2)

    ret = (ret * ret) % c

    if b % 2 == 1:
        ret = (ret * a) % c

    return ret

print(go(a, b))
