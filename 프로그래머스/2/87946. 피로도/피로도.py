def solution(k, dungeons):
    answer = -1
    
    size = len(dungeons)
    
    remain_k = k
    visited = [False] * size
    
    def dfs(remain_k, term_cnt):
        nonlocal answer
        
        answer = max(answer, term_cnt)
        
        for i in range(size):
            min_fatigue, cost_fatigue = dungeons[i]
            if remain_k >= min_fatigue and (not visited[i]):
                visited[i] = True
                dfs(remain_k - cost_fatigue, term_cnt + 1)
                visited[i] = False
    
    
    dfs(remain_k, 0)
    
    return answer