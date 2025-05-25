import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left, right = 0, n - 1

max_solution = float('inf')
result = None

while left < right:
    solut = arr[left] + arr[right]

    if abs(solut) < max_solution:
        max_solution = abs(solut)
        result = [arr[left], arr[right]]

    if solut <= 0:
        left += 1
    else:
        right -= 1

print(*result)