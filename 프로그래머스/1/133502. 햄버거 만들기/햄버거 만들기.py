def solution(ingredient):
    answer = 0
    
    stk = []
    size = 0
    
    for c in ingredient:
        stk.append(c)
        size += 1
        
        if size >= 4:
            if stk[-4:] == [1, 2, 3, 1]:
                stk.pop()
                stk.pop()
                stk.pop()
                stk.pop()
                answer += 1
                size -= 4
             
    if size >= 4:
        if stk[-4:] == [1, 2, 3, 1]:
            stk.pop()
            stk.pop()
            stk.pop()
            stk.pop()
            answer += 1
            size -= 4
    
    return answer