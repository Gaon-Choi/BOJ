n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

blocks = [
    # 블록 1
    [
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
    ]
    
    # 블록 2
    ,[
        [1,1,0,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]

    # 블록 3
    ,[
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0],
    ]
    ,[
        [0,1,1,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [0,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,1,0,0],
        [0,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ]

    # 블록 4
    ,[
        [1,0,0,0],
        [1,0,0,0],
        [1,1,0,0],
        [0,0,0,0],
    ]
    ,[
        [0,0,1,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,1,1,0],
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0],
    ]
    ,[
        [0,1,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,1,1,0],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    # 블록 5
    ,[
        [1,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [0,1,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    ,[
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0],
    ]
    ,[
        [1,1,1,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
]

sum_total = 0

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def get_max(x, y):
    max_sum = 0

    for shape in blocks:
        temp_sum = sum([
            matrix[x + dx][y + dy]
            for dx in range(4)
            for dy in range(4)
            if is_reachable(x + dx, y + dy) and shape[dx][dy] == 1
        ])

        max_sum = max(max_sum, temp_sum)

    return max_sum

result = 0

for i in range(n):
    for j in range(m):
        result = max(result, get_max(i, j))

print(result)