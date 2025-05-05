def is_zero_or_five(num):
    for c in num:
        if not (c == '5' or c == '0'):
            return False
        
    return True

def solution(l, r):
    answer = []
    
    for n in range(l, r + 1):
        if n % 5 != 0:
            continue
        
        if is_zero_or_five(str(n)):
            answer.append(n)
            
    if not answer:
        answer.append(-1)
    
    return answer