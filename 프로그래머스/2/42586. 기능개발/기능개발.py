import math

def solution(progresses, speeds):
    answer = []
    
    remain_day = []
    
    for i in range(len(progresses)):
        remain_day.append(math.ceil((100 - progresses[i]) / speeds[i]))
      
    temp = []
    max_ = remain_day[0]
    
    for elem in remain_day:
        if max_ < elem:
            answer.append(len(temp))
            temp = []
            max_ = elem
        
        temp.append(elem)
    
    if temp:
        answer.append(len(temp))
    
    return answer