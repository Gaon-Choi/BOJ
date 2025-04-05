import heapq

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

score = [0, 1, 10, 100, 1000]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

def find_optimal_place(student, friends):
    pq = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                continue

            fav_cnt = 0
            empty_cnt = 0

            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if is_reachable(nx, ny):
                    if matrix[nx][ny] == 0:
                        empty_cnt += 1
                    else:
                        if matrix[nx][ny] in friends:
                            fav_cnt += 1

            heapq.heappush(pq, (-fav_cnt, -empty_cnt, i, j))

    if pq:
        optim = heapq.heappop(pq)
        return optim[2], optim[3]

n = int(input())

friends = []
fhash = dict()

matrix = [[0] * n for _ in range(n)]

for _ in range(n ** 2):
    friend, n1, n2, n3, n4 = map(int, input().split())
    friends.append([friend, [n1, n2, n3, n4]])
    fhash[friend] = [n1, n2, n3, n4]

for f in friends:
    student, friends = f[0], f[1]

    x, y = find_optimal_place(student, friends)
    matrix[x][y] = student

answer = 0

for i in range(n):
    for j in range(n):
        student = matrix[i][j]
        friends = fhash[student]
        cnt = 0

        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy

            if is_reachable(nx, ny) and matrix[nx][ny] in friends:
                cnt += 1

        answer += score[cnt]

print(answer)