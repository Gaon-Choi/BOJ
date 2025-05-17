def solution(s):
    answer = []
    set_ = set()
    
    temp_list = []
    
    s = s[1:-1]
    prev = "{"
    
    temp = ""
    
    for i in range(len(s)):
        if not temp and s[i] == ",":
            continue
            
        temp += s[i]
        
        if s[i] == "}":
            temp_list.append(temp)
            temp = ""
    
    temp_list.sort(key = lambda x : len(x))
    
    for tmp_set in temp_list:
        arr = list(map(int, tmp_set[1:-1].split(",")))
        
        for elem in arr:
            if elem not in set_:
                answer.append(elem)
                set_.add(elem)
    
    return answer