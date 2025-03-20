def solution(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    arr = [1, 2]
    
    for i in range(2, n + 1):
        arr.append((arr[i - 1] + arr[i - 2]) % 1000000007)
    
    answer = arr[n - 1] % 1000000007
    
    return answer