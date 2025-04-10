def cut_100(matrix):
    result = []

    for i in range(min(100, len(matrix))):
        result.append(matrix[i][:min(100, len(matrix[0]))])

    return result

def do_specific_operation(matrix):
    for col in range(len(matrix)):
        hash_ = dict()

        for row in range(len(matrix[col])):
            if matrix[col][row] == 0:
                continue

            if matrix[col][row] in hash_:
                hash_[matrix[col][row]] += 1
            else:
                hash_[matrix[col][row]] = 1

        arr = []

        for k, v in hash_.items():
            arr.append([v, k])

        arr.sort(key = lambda x : (x[0], x[1]))

        temp_arr = []

        for i in range(len(arr)):
            temp_arr.append(arr[i][1])
            temp_arr.append(arr[i][0])

        matrix[col] = temp_arr[:]

    max_size = max(len(row) for row in matrix)

    for row in range(len(matrix)):
        size = max_size - len(matrix[row])
        
        for _ in range(size):
            matrix[row].append(0)



def do_operation():
    global matrix
    row, column = len(matrix), len(matrix[0])

    if row >= column:
        do_specific_operation(matrix)

    else:
        transpose_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose_matrix[j][i] = matrix[i][j]

        do_specific_operation(transpose_matrix)

        nrow, ncol = len(transpose_matrix), len(transpose_matrix[0])

        matrix = [[0] * nrow for _ in range(ncol)]

        for i in range(nrow):
            for j in range(ncol):
                matrix[j][i] = transpose_matrix[i][j]

    matrix = cut_100(matrix)


r, c, k = map(int, input().split())

matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().split())))

t = 0

while t <= 100:
    if 0 <= r - 1 < len(matrix) and 0 <= c - 1 < len(matrix[0]) and matrix[r - 1][c - 1] == k:
        break
        
    do_operation()

    t += 1

if t == 101:
    print(-1)
else:
    print(t)