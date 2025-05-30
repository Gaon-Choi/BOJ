def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x : x[1])

    p = -1
    
    for i in range(len(targets)):
        if p <= targets[i][0]:
            p = targets[i][1]
            answer += 1
    
    return answer