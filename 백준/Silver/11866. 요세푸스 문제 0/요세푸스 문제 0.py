from collections import deque

n, k = map(int, input().split())

queue = deque(list(range(1, n + 1)))

arr = []

for _ in range(n):
    queue.rotate(-(k-1))

    arr.append(queue.popleft())

print("<" + ", ".join(map(str, arr)) + ">")