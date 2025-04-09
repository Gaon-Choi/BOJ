def find(x):
    if x == uf[x]:
        return x
    
    root_node = find(uf[x])
    dist[x] += dist[uf[x]]
    uf[x] = root_node

    return root_node
        

def union(x, y):
    #X, Y = find(x), find(y)
    uf[x] = y
    dist[x] = abs(x - y) % 1000

T = int(input())

for _ in range(T):
    n = int(input())
    uf = list(range(n + 1))

    dist = [0] * (n + 1)

    while True:
        query = input().split()

        if "O" in query:
            break

        elif query[0] == "E":
            temp = 0
            v = int(query[1])
            find(v)
            print(dist[v])

        elif query[0] == "I":
            v, g = int(query[1]), int(query[2])

            union(v, g)

