n = int(input())
arr = list(map(int, input().split()))
sumarr = [0]

for i in range(n):
    sumarr.append(sumarr[i] + arr[i])

t = int(input())

result = []

for _ in range(t):
    start, end = list(map(int, input().split()))

    result.append(sumarr[end] - sumarr[start - 1])

print(*result, sep = '\n')