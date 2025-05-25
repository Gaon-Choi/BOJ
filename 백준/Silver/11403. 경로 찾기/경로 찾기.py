import sys
input = sys.stdin.readline

INF = float('inf')

def floyd_warshall(graph):
    size = len(graph)

    dist = [[INF] * size for _ in range(size)]

    # for i in range(size):
    #     dist[i][i] = 0

    for i in range(size):
        for j in range(size):
            if graph[i][j] == 1:
                dist[i][j] = 1

    for k in range(size):
        for i in range(size):
            for j in range(size):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    return dist

N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dist_matrix = floyd_warshall(matrix)

for i in range(N):
    for j in range(N):
        if dist_matrix[i][j] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()