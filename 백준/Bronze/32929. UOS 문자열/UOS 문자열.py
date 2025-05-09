import sys
input = sys.stdin.readline

n = int(input())
uos = "UOS"
print(uos[(n - 1) % 3])