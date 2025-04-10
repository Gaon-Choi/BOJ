def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

clouds = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    d, s = map(int, input().split())

    d -= 1

    for c in range(len(clouds)):
        clouds[c][0] = (clouds[c][0] + s * dxs[d]) % n
        clouds[c][1] = (clouds[c][1] + s * dys[d]) % n

    for cloud in clouds:
        x, y = cloud
        arr[x][y] += 1

    temp = []

    for cloud in clouds:
        x, y = cloud
        points = 0

        for dx, dy in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            if is_reachable(x + dx, y + dy) and (arr[x+dx][y+dy] > 0):
                points += 1

        if points > 0:
            temp.append((x, y, points))

    for x, y, p in temp:
        arr[x][y] += p

    temp_cloud = {(cloud[0], cloud[1]) for cloud in clouds}

    clouds.clear()

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and ((i, j) not in temp_cloud):
                clouds.append([i, j])
                arr[i][j] -= 2

print(sum([sum(row) for row in arr]))