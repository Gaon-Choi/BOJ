import sys

arr = []
size = 0
start = 0; end = -1

n = int(sys.stdin.readline())

result = []

for _ in range(n):
	command = sys.stdin.readline().split()

	if command[0] == "push":
		arr.append(int(command[1]))
		size += 1
		end += 1
	elif command[0] == "front":
		result.append(arr[start] if size > 0 else -1)
	elif command[0] == "back":
		result.append(arr[end] if size > 0 else -1)
	elif command[0] == "size":
		result.append(size)
	elif command[0] == "empty":
		result.append(1 if size == 0 else 0)
	elif command[0] == "pop":
		if size <= 0:
			result.append(-1)
		else:
			result.append(arr[start])
			size -= 1
			start += 1

for elem in result:
    print(elem)
