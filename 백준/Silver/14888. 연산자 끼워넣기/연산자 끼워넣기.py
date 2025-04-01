def permutations(arr, k):
    result = []
    tmp = []

    visited = [False] * len(arr)

    def backtrack():
        if len(tmp) == k:
            result.append(tmp[:])
            return
        
        prev = -1

        for i in range(len(arr)):
            if not visited[i] and prev != arr[i]:
                visited[i] = True
                prev = arr[i]

                tmp.append(arr[i])
                backtrack()
                tmp.pop()

                visited[i] = False

    backtrack()

    return result

n = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))

operations = (['+'] * ops[0]) + (['-'] * ops[1]) + (['*'] * ops[2]) + (['/'] * ops[3])

op_sequence = permutations(operations, len(operations))

max_result = -1e10
min_result = 1e10

for seq in op_sequence:
    tmp = arr[0]

    for i in range(1, len(arr)):
        if seq[i - 1] == "+":
            tmp += arr[i]
        elif seq[i - 1] == "-":
            tmp -= arr[i]
        elif seq[i - 1] == "*":
            tmp *= arr[i]
        elif seq[i - 1] == "/":
            if tmp < 0:
                tmp = -(-tmp // arr[i])
            elif arr[i] < 0:
                tmp = -(tmp // (-arr[i]))
            else:
                tmp = tmp // arr[i]

    max_result = max(max_result, tmp)
    min_result = min(min_result, tmp)

print(max_result)
print(min_result)