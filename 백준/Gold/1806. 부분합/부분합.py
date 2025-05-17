import sys
input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

left, right = 0, 0
curr_sum = 0
min_length = n + 1

while True:
    if curr_sum >= s:
        min_length = min(min_length, right - left)
        curr_sum -= arr[left]
        left += 1
    
    elif right == n:
        break

    else:
        curr_sum += arr[right]
        right += 1

if min_length == n + 1:
    print(0)
else:
    print(min_length)
