import sys
input = sys.stdin.readline

M, K = map(int, input().split())

print("Yes" if M % K == 0 else "No")
