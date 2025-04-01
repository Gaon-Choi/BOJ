def solution(s):
    answer = []
    
    hash_dict = dict()
    
    for idx, c in enumerate(s):
        if c in hash_dict:
            answer.append(idx - hash_dict[c])
        else:
            answer.append(-1)
        
        hash_dict[c] = idx
    
    return answer