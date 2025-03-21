def solution(priorities, location):
    answer = 0
    
    priorities_ = []
    
    for idx, value in enumerate(priorities):
        priorities_.append([idx, value])
        
    result = []
    
    while priorities_:
        max_ = max(list(map(lambda x: x[1], priorities_)))
        
        if priorities_[0][1] >= max_:
            elem = priorities_.pop(0)
            result.append(elem)
        else:
            elem = priorities_.pop(0)
            priorities_.append(elem)
            
    for i in range(len(result)):
        if result[i][0] == location:
            answer = i + 1
            break
    
    return answer