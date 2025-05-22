def solution(n, lost, reserve):
    answer = 0
    
    # 도난 이후에도 여분의 옷이 있는 학생
    reserve_set = set(reserve) - set(lost)
    # 도난당한 학생 중 여분의 옷이 있는 학생은 제외 -> 옷이 진짜 없는 학생
    lost_set = set(lost) - set(reserve)
    
    for l in lost_set:
        if l - 1 in reserve_set:
            reserve_set.remove(l - 1)
            answer += 1
            continue
        
        if l + 1 in reserve_set:
            reserve_set.remove(l + 1)
            answer += 1
            
    answer = n - len(lost_set) + answer
    
    return answer