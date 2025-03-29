n = int(input())

for _ in range(n):
    words = input().split()

    print(" ".join(map(lambda x: x[-1::-1], words)))