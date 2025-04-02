def permutations(arr, k):
    result = []
    permu = []

    visited = [False] * len(arr)

    def backtrack():
        if len(permu) == k:
            result.append(permu[:])
            return

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True

                permu.append(arr[i])
                backtrack()
                permu.pop()

                visited[i] = False

    backtrack()

    return result

n = int(input())
arr = list(range(1, n + 1))

for res in permutations(arr, n):
    print(*res)