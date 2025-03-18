cutline = int(input())

arr = list(map(int, input().split()))

print(sum(list(map(lambda x: min(x, cutline), arr))))