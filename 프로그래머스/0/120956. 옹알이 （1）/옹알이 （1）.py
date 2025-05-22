def is_valid(word):
    valid_set = {"aya" : 0, "ye" : 0, "woo" : 0, "ma" : 0}
    
    idx = 0
    
    while idx < len(word):
        matched = False
        
        if word[idx : idx + 2] in valid_set:
            target = word[idx : idx + 2]
            valid_set[target] += 1
            idx += len(target)

            if valid_set[target] > 1:
                return False
            
            matched = True
        
        elif word[idx : idx + 3] in valid_set:
            target = word[idx : idx + 3]
            valid_set[target] += 1
            idx += len(target)

            if valid_set[target] > 1:
                return False
            
            matched = True
            
        if not matched:
            return False
    
    return True
    
    

def solution(babbling):
    answer = 0
    
    for elem in babbling:
        if is_valid(elem):
            answer += 1
    
    return answer