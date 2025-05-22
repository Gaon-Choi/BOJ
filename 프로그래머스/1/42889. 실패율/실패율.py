def solution(N, stages):
    answer = []
    
    stages.sort(reverse = True)
    
    result = []
    
    for stage in range(1, N + 1):
        cnt = 0
        
        size = len(stages)
        
        if size == 0:
            result.append((0, stage))
            continue
        
        while stages and (stages[-1] == stage):
            cnt += 1
            stages.pop()
            
        result.append((cnt / size, stage))
        
    result.sort(key = lambda x : (-x[0], x[1]))
    
    for res in result:
        answer.append(res[1])
    
    return answer