import sys
input = sys.stdin.readline

X, L, R = map(int, input().split())

if X <= L:
    print(L)
elif R <= X:
    print(R)
else:
    # L < X < R
    print(X)