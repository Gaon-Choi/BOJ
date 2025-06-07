def solution(files):
    answer = []
    
    temp_arr = []
    
    for idx, file in enumerate(files):
        head = ""
        num = ""
        tail = ""
        
        for c in file:
            if c.isdigit():
                if tail != "":
                    tail += c
                else:
                    num += c
            else:
                if num == "":
                    head += c
                else:
                    tail += c
        
        head = head.lower()
        
        temp_arr.append((file, head, int(num), tail, idx))
    
    temp_arr.sort(key = lambda x : (x[1], x[2], x[4]))
    
    for filename, head, num, tail, idx in temp_arr:
        answer.append(filename)
    
    return answer