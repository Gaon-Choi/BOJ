def solution(numbers):
    answer = ''
    
    numbers.sort(key = lambda x: str(x) * 3, reverse = True)
    
    for c in numbers:
        answer += str(c)
        
    zero_idx = 0
    
    for i in range(len(answer)):
        if answer[i] == "0":
            zero_idx += 1
        else:
            break
    
    if zero_idx > 0:
        return '0'
    
    return answer