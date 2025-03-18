n = int(input())
arr = list(map(int, input().split()))

hashed = dict(zip(arr, [1] * n))

k = int(input())
queries = list(map(int, input().split()))

for elem in queries:
    print(1 if elem in hashed else 0)