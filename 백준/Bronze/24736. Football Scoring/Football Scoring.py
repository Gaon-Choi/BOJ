import sys
input = sys.stdin.readline

score = [6, 3, 2, 1, 2]

for _ in range(2):
    arr = list(map(int, input().split()))

    temp = 0

    for i in range(len(arr)):
        temp += arr[i] * score[i]

    print(temp, end=" ")