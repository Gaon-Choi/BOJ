import sys
input = sys.stdin.readline

step = 1

while True:
    n, *arr = list(map(int, input().split()))

    if n == 0:
        break

    if n % 2 != 0:
        print(f"Case {step}: {arr[n // 2]:.1f}")
    else:
        print(f"Case {step}: {(arr[n // 2] + arr[(n // 2) - 1]) / 2:.1f}")
    
    step += 1
