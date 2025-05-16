def solution(babbling):
    answer = 0
    
    able_list = {"aya", "ye", "woo", "ma"}
    
    for data in babbling:
        temp = ""
        prev = ""
        is_ = True
        
        for c in data:
            temp += c
            
            if temp in able_list:
                if prev == temp:
                    is_ = False
                    break
                else:
                    prev = temp
                    temp = ""
                    
        if temp in able_list:
            if prev == temp:
                is_ = False
            else:
                temp = ""
            
        if len(temp) > 0:
            is_ = False
            
        if is_:
            answer += 1
                    
    return answer