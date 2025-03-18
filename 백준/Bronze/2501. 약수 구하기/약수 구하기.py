N, K = map(int, input().split())

curr_k = 0
answer = 0

for i in range(1, N+1):
    if N % i == 0:
        curr_k += 1
        if curr_k == K:
            answer = i
            break
        
print(answer if curr_k == K else 0)