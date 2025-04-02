import sys
input = sys.stdin.readline

n = int(input())

size = 0
stack = []

for _ in range(n):
    query = input().split()
    
    command = int(query[0])
    elem = -1
    
    if command == 1:
        elem = int(query[1])
        stack.append(elem)
        size += 1
    elif command == 2:
        if size > 0:
            print(stack.pop())
            size -= 1
        else:
            print(-1)
    elif command == 3:
        print(size)
    elif command == 4:
        print(1 if size == 0 else 0)
    elif command == 5:
        if size > 0:
            print(stack[size - 1])
        else:
            print(-1)