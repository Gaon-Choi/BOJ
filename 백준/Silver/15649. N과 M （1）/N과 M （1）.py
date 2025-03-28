def permutations(arr, m):
    result = []
    permu = []

    visited = [False] * len(arr)

    def backtrack():
        if len(permu) == m:
            result.append(permu[:])

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True

                permu.append(arr[i])
                backtrack()
                permu.pop()

                visited[i] = False

    backtrack()

    return result

n, m = map(int, input().split())

arr = list(range(1, n + 1))

result = permutations(arr, m)

for res in result:
    print(*res)