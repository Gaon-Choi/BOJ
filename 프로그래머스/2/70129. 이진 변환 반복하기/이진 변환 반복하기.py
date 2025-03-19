def solution(s):
    answer = []
    
    cnt = 0
    zeros = 0
    
    while s != '1':
        size = len(s)
        zero_cnt = s.count('0')
        
        s = str(bin(size - zero_cnt))[2:]
        cnt += 1
        zeros += zero_cnt
        
    answer.append(cnt)
    answer.append(zeros)
        
    
    return answer