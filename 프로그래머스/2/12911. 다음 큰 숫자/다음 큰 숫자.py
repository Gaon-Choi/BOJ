def solution(n):
    answer = 0
    
    cnt_origin = str(bin(n))[2:].count('1')
    
    temp = n + 1
    
    while True:
        cnt = str(bin(temp))[2:].count('1')
        
        if cnt_origin == cnt:
            answer = temp
            break
    
        temp += 1
    return answer