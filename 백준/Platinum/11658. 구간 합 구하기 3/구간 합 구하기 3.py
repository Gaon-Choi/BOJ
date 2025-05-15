import sys
input = sys.stdin.readline

class FenwickTree2D:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

        self.tree = [[0] * (col + 1) for _ in range(row + 1)]

    def update(self, x: int, y: int, diff: int) -> None:
        i = x

        while i <= self.row:
            j = y

            while j <= self.col:
                self.tree[i][j] += diff
                j += (j & -j)

            i += (i & -i)

    def query(self, x: int, y: int) -> int:
        result = 0
        i = x

        while i > 0:
            j = y

            while j > 0:
                result += self.tree[i][j]
                j -= (j & -j)
            
            i -= (i & -i)

        return result
    
    def range_query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return self.query(x2, y2) - self.query(x1 - 1, y2) - self.query(x2, y1 - 1) + self.query(x1 - 1, y1 - 1)

n, m = map(int, input().split())

fenwick2d = FenwickTree2D(n, n)
arr = []

for x in range(1, n + 1):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

    for y in range(1, len(tmp) + 1):
        fenwick2d.update(x, y, tmp[y - 1])

for _ in range(m):
    query = list(map(int, input().split()))

    if query[0] == 0:
        x, y, c = query[1:]

        fenwick2d.update(x, y, c - arr[x - 1][y - 1])
        arr[x - 1][y - 1] = c

    else:
        x1, y1, x2, y2 = query[1:]
        print(fenwick2d.range_query(x1, y1, x2, y2))
        