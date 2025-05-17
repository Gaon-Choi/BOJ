def solution(lines):
    answer = 0
    
    arr = [0] * 201
    
    offset = 100
    
    for line in lines:
        start, end = line
        
        for i in range(start + offset, end + offset):
            arr[i] += 1
            
    for c in arr:
        if c >= 2:
            answer += 1
    
    return answer