def permutation(arr, k):
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

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

arr = permutation(list(range(2, n + 1)), n - 1)

min_cost = 1e9

for i in range(len(arr)):
    total_cost = 0
    flag = False

    temp = [1] + arr[i] + [1]

    for p in range(len(temp) - 1):
        cost = matrix[temp[p] - 1][temp[p+1] - 1]

        if cost == 0:
            flag = True
            break

        total_cost += cost

    if flag:
        continue

    min_cost = min(min_cost, total_cost)

print(min_cost)