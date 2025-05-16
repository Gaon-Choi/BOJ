def solution(d, budget):
    answer = 0
    
    remain = budget
    
    d.sort()
    
    for elem in d:
        if elem <= remain:
            remain -= elem
            answer += 1
        else:
            break
    
    return answer