def solution(record):
    answer = []
    
    name_dict = dict()
    
    for r in record:
        temp = r.split(" ")
        
        if temp[0] == "Leave":
            continue
            
        name_dict[temp[1]] = temp[2]
        
    for r in record:
        temp = r.split(" ")
        behavior, uid = temp[0], temp[1]
        
        if behavior == "Enter":
            answer.append(f"{name_dict[uid]}님이 들어왔습니다.")
        elif behavior == "Leave":
            answer.append(f"{name_dict[uid]}님이 나갔습니다.")
            
    return answer