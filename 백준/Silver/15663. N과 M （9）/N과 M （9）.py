def permutations(arr, m):
    result = []
    permu = []

    visited = [False] * len(arr)

    def backtrack():
        if len(permu) == m:
            result.append(permu[:])
            return
        
        prev = -1
        
        for i in range(len(arr)):
            if not visited[i] and prev != arr[i]:
                visited[i] = True
                prev = arr[i]

                permu.append(arr[i])
                backtrack()
                permu.pop()

                visited[i] = False

    backtrack()

    return result

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

result = permutations(arr, m)

for res in result:
    print(*res)