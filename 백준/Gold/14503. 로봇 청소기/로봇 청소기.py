def is_reachable(x, y):
    return 0 <= x < n and 0 <= y and m and matrix[x][y] == 0

def count_surroundings(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if is_reachable(nx, ny) and not visited[nx][ny]:
            return True
        
    return False

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

n, m = map(int, input().split())

curr_x, curr_y, curr = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

total_count = 0

while True:
    if not visited[curr_x][curr_y]:
        visited[curr_x][curr_y] = True
        total_count += 1

    if count_surroundings(curr_x, curr_y):
        # 반시계 90도 회전
        curr = (curr - 1) % 4

        if is_reachable(curr_x + dxs[curr], curr_y + dys[curr]) and not visited[curr_x + dxs[curr]][curr_y + dys[curr]]:
            curr_x += dxs[curr]
            curr_y += dys[curr]

    else:
        if is_reachable(curr_x - dxs[curr], curr_y - dys[curr]):
            curr_x -= dxs[curr]
            curr_y -= dys[curr]
        else:
            break
 
print(total_count)