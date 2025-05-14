import sys
input = sys.stdin.readline

def combination(arr, k):
    result = []
    comb = []

    def backtrack(start):
        if len(comb) == k:
            result.append(comb[:])
            return
        
        for i in range(start, n):
            comb.append(arr[i])
            backtrack(i + 1)
            comb.pop()

    backtrack(0)

    return result

while True:
    query = list(map(int, input().split()))

    if query == [0]:
        break

    n, arr = query[0], query[1:]

    result = combination(arr, 6)

    for res in result:
        print(*res)

    print()